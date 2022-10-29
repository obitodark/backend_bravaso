from sqlalchemy import desc
from app import db
from app.models.products_model import ProductsModel
from app.schemas.products_schema import ProductsResponseSchema
from app.utils.bucket import Bucket


class ProductsController:
    def __init__(self):
        self.model = ProductsModel
        self.schema = ProductsResponseSchema
        # self.bucket = Bucket('ecomerce-bravaso', 'products')
        # self.data1=self.model.where(category_id=data['id_category'],subcategory_id=data['id_subcategory']).order_by('id').paginate(
        #                 per_page=data['per_page'], page=data['page'] )

        # self.__allowed_extensions = ['jpg', 'jpeg', 'png', 'webp']

    def all(self):
        try:
            records = self.model.where(status=True).order_by('id').all()
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
                'message': 'No se encontro el producto en mencion'
            }, 404
        except Exception as e:
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, 500

    def create(self, data):
        try:
            # filename, stream = self.__validateExtensionImage(data['image'])
            # image_url = self.bucket.uploadObject(stream, filename)
            # data['image'] = image_url

            new_record = self.model.create(**data)
            db.session.add(new_record)
            db.session.commit()

            response = self.schema(many=False)

            return {
                'messsage': 'El producto se creo con exito',
                'data': response.dump(new_record)
            }, 201
        except Exception as e:
            db.session.rollback()
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
                # if data['image']:
                #     filename, stream = self.__validateExtensionImage(
                #         data['image']
                #     )
                #     image_url = self.bucket.uploadObject(stream, filename)
                #     data['image'] = image_url
                # else:
                #     data.pop('image')

                # for clave,valor in data.items():
                #     if  valor==None:
                       
                #         data.pop(str(clave))
                #         print(data)    
                record.update(**data)
                db.session.add(record)
                db.session.commit()

                response = self.schema(many=False)
                return {
                    'messsage': 'El producto se ha actualizado con exito',
                    'data': response.dump(record)
                }, 200
            return {
                'message': 'No se encontro el producto en mencion'
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
                    'message': 'Se deshabilito el producto con exito'
                }, 200
            return {
                'message': 'No se encontro el producto en mencion'
            }, 404
        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, 500

    def filterByCategory(self,page,perpage,data):
        try:
            #    self.base= self.__filter(id_category,id_sucategory,page, per_page)['results']
            #    print(self.base)
            return self.__filter(data,page,perpage)
        except Exception as e:
                return {
                    'message': 'Ocurrio un error',
                    'error': str(e)
                },500



    # def __validateExtensionImage(self, image):
    #     filename = image.filename
    #     stream = image.stream
    #     extension = filename.split('.')[1]

    #     if extension not in self.__allowed_extensions:
    #         raise Exception('El tipo de archivo usado, no esta permitido')

    #     return filename, stream

    def __filter(self,data,pag,perpag):
           type="id"

        #    if  data['id_brands']==0:
        #             records =self.data1
        #    else :
        #             records = self.data1.where(brand_id=data['id_brands']).order_by("id").paginate(
        #                 per_page=data['per_page'], page=data['page']
        #             )

           


            # Paginate
            # page -> la pagina actual
            # per_page -> total de registros x pagina
            # total -> total de registros
            # pages -> total de paginas
            # items -> Lista de objetos



        #    for clave,valor in data.items():
        #             if  valor==0:
        #                 data.pop()

          

           if data['price']==0:
            type="id"
           if data['price']==1:
            type="price"
          


           if  data['id_brands']==0:
                    records = self.model.where(category_id=data['id_category'],subcategory_id=data['id_subcategory'],status=True).filter(self.model.name.ilike(f"%{data['search']}%"),).order_by(type).paginate(
                        per_page=perpag, page=pag
                    )
           else :
                    records = self.model.where(  category_id=data['id_category'],subcategory_id=data['id_subcategory'],brand_id=data['id_brands'],status=True).filter(self.model.name.ilike(f"%{data['search']}%"),).order_by(type).paginate(
                         per_page=perpag, page=pag
                    )
           if data['price']==2: 
             type="price"
             if  data['id_brands']==0:
                    records = self.model.where(category_id=data['id_category'],subcategory_id=data['id_subcategory'],status=True).filter(self.model.name.ilike(f"%{data['search']}%"),).order_by(desc(type)).paginate(
                         per_page=perpag, page=pag
                    )
             else :
                    records = self.model.where(category_id=data['id_category'],subcategory_id=data['id_subcategory'],brand_id=data['id_brands'],status=True).filter(self.model.name.ilike(f"%{data['search']}%"),).order_by(desc(type)).paginate(
                        per_page=perpag, page=pag
                    )         


           response = self.schema(many=True)
           return {
                'results': response.dump(records.items),
                'pagination': {
                    'totalRecords': records.total,
                    'totalPages': records.pages,
                    'perPage': records.per_page,
                    'currentPage': records.page
                }
            }
   
