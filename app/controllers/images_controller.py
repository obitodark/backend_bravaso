from sqlalchemy import desc
from app import db
from app.models.image_model import ImagesModel
from app.schemas.images_schema import ImagesResponseSchema
from app.utils.bucket import Bucket
from app.controllers.product_images_controller import ProductImagesController
from app.controllers.users_images_controller import UsersImagesController


class ImagesController:
    def __init__(self):
        self.model = ImagesModel
        self.schema = ImagesResponseSchema
        self.products_image=ProductImagesController()
        self.bucket = Bucket('ecomerce-bravaso', 'images')
        # self.data1=self.model.where(category_id=data['id_category'],subcategory_id=data['id_subcategory']).order_by('id').paginate(
        #                 per_page=data['per_page'], page=data['page'] )

        self.__allowed_extensions = ['jpg', 'jpeg', 'png', 'webp']

    def all(self):
        try:
            records = self.model.where(status=True).all()
            response = self.schema(many=True)
            return {
                'data': response.dump(records)
            }
        except Exception as e:
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, 500

    def getById(self, id):
        try:
            if record := self.model.where(id=id).first():
                response = self.schema(many=False)
                return {
                    'data': response.dump(record)
                }, 200
            return {
                'message': 'No se encontro la imagen en mencion'
            }, 404
        except Exception as e:
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, 500
    
    # def create(self,data):
    #     try: 
          
    #         filename, stream = self.__validateExtensionImage(data['image'])
    #         image_url = self.bucket.uploadObject(stream, filename)
    #         data['image'] = image_url
    #         new_record = self.model.create(**data)
    #         db.session.add(new_record)
    #         db.session.commit()
    #         response = self.schema(many=False)
                    
    #         return {
    #             'messsage': 'El producto se creo con exito',
                
    #             'data': response.dump(new_record)
    #         }, 201
    #     except Exception as e:
    #         # db.session.rollback()
    #         return {
    #             'message': 'Ocurrio un error',
    #             'error': str(e)
    #         }, 500

    


    def createById(self,id, data):
        try: 
          
            filename, stream = self.__validateExtensionImage(data['image'])
            image_url = self.bucket.uploadObject(stream, filename)
            data['image'] = image_url

            new_record = self.model.create(**data)
          
            
            db.session.add(new_record)
            db.session.commit()
             
            response = self.schema(many=False)
            if id!='none' :
                id_prod=id.split('_')[0]
                model=id.split('_')[1]
                if model=='prod':
                 ProductImagesController().create({'image_id':response.dump(new_record)['id'],'product_id':id_prod})
                elif model=='user':
                 UsersImagesController().create({'image_id':response.dump(new_record)['id'],'user_id':id_prod})
            return {
                'messsage': 'El producto se creo con exito',
                
                'data': response.dump(new_record)
            }, 201
        except Exception as e:
            # db.session.rollback()
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, 500

    def update(self, id, data):
        try:
            if record := self.model.where(id=id).first():
                
                    # if(key==null):
                    # 0    
                    
            #    if data['name']==None:
            #     data.pop('name')
                      


                  
                # data = {k: v for k, v in data.items() if v is not None}
                if data['image']:
                    filename, stream = self.__validateExtensionImage(
                        data['image']
                    )
                    image_url = self.bucket.uploadObject(stream, filename)
                    data['image'] = image_url
                else:
                    data.pop('image')

                # for clave,valor in data.items():
                #     if  valor==None:
                       
                #         data.pop(str(clave))
                #         print(data)    
                record.update(**data)
                db.session.add(record)
                db.session.commit()

                response = self.schema(many=False)
                return {
                    'messsage': 'El imagen se ha actualizado con exito',
                    'data': response.dump(record)
                }, 200
            return {
                'message': 'No se encontro el imagen en mencion'
            }, 404
        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, 500
    def delete(self, id):
        try:
            if record := self.model.where(id=id).first():
                if record.status:
                    record.update(status=False)
                    db.session.add(record)
                    db.session.commit()
                return {
                    'message': 'Se deshabilito el imagen con exito'
                }, 200
            return {
                'message': 'No se encontro el imagen en mencion'
            }, 404
        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, 500

    def __validateExtensionImage(self, image):
        filename = image.filename
        stream = image.stream
        extension = filename.split('.')[1]

        if extension not in self.__allowed_extensions:
            raise Exception('El tipo de archivo usado, no esta permitido')

        return filename, stream   
   
    def countImages(self):  
           records = self.model.where(status=True).all()
           response = self.schema(many=True)

           return len(response.dump(records))