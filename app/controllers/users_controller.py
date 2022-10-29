from app import db
from app.models.users_model import UserModel
from app.schemas.users_schema import UsersResponseSchema


class UsersController:
    def __init__(self):
        self.model = UserModel
        self.schema = UsersResponseSchema

    # def all(self, page, per_page):
    #     try:category_id=id_category,subcategory_id=id_sucategory
    #         # Paginate
    #         # page -> la pagina actual
    #         # per_page -> total de registros x pagina
    #         # total -> total de registros
    #         # pages -> total de paginas
    #         # items -> Lista de objetos
    #         records = self.model.where(status=True).order_by('id').paginate(
    #             per_page=per_page, page=page
    #         )
    #         response = self.schema(many=True)
    #         return {
    #             'results': response.dump(records.items),
    #             order_by('id').paginate(
    #             per_page=per_page, page=page
    #         )
    #         }
    #     except Exception as e:
    #         return {
    #             'message': 'Ocurrio un error',
    #             'error': str(e)
    #         }

    def ListUser(self):
        try:
                              
            records = self.model.where(status=True).order_by('id').all()
            response = self.schema(many=True)
            return {
                'results': response.dump(records)
                
            }
        except Exception as e:
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }

    def  validateUsername(self,username):

        try: 
             record=self.model.where(username=username).first()
             if not record :
           
                 return {
                    
                    'message': 'El username disponible',
                  },200
             return {
                    'message': 'El username ya exite  ,Eliga otra',
                } ,226  
        except Exception as e:
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, 500

    def  validateEmail(self,email):
        try:
             record= self.model.where(email=email).first()
             if not record :
                 return {
                    
                    'message': 'El Email disponible',
                  },200
             return {
                    'message': 'El Email ya esta registrado  ,Eliga otra',
                },226


        except Exception as e:
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, 500     

    def  validateDni(self,dni):
        try:
             record= self.model.where(dni=dni).first()
             if not record :
                 return {
                    
                    'message': 'El Dni disponible',
                  },200
             return {
                    'message': 'El  Dni  ya esta registrado  ,Eliga otra',
                },226


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
                'message': 'No se encontro el usuario mencionado'
            }, 404
        except Exception as e:
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, 500

    def create(self, data):
        try:

            # if record := self.model.where(email =data.email).first():
            #      return {
            #             'data': 'el correo ya exite'
            #         }, 200   
            
               
                
             
            
            new_record = self.model.create(**data)
            new_record.hashPassword()
            db.session.add(new_record)
            db.session.commit()

            response = self.schema(many=False)

            return {
                'message': 'El usuario se creo con exito',
                'data': response.dump(new_record)
            }
        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }

    def update(self, id, data):
        try:
            if record := self.model.where(id=id).first():
                record.update(**data)
                db.session.add(record)
                db.session.commit()

                response = self.schema(many=False)
                return {
                    'messsage': 'El usuario se ha actualizado con exito',
                    'data': response.dump(record)
                }, 200
            return {
                'message': 'No se encontro el usuario mencionado'
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
                    'message': 'Se deshabilito el usuario con exito'
                }, 200
            return {
                'message': 'No se encontro el usuario mencionado'
            }, 404
        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, 500
