from app import db
from app.models.favourite_model import FavoriteModel
from app.schemas.favorite_schema import FavoriteResponseSchema
from flask_jwt_extended import current_user

class FavouriteController:
    def __init__(self):
        self.model=FavoriteModel
        self.schema=FavoriteResponseSchema
        self.user_id=current_user['id']
       

    def all(self):
        try:
            record=self.model.where(user_id=self.user_id).all()
            response=self.schema(many=True)
            data = response.dump(record)
            cant=0
            if record:
                
                for item in data:
                    cant=cant+1
            return{
                'data': response.dump(record),
                'total':cant
            }

        except Exception as e: 
            return self._getError(e,500)
              

    def create(self,data):
        try:
            if record := self.model.where(
                user_id=self.user_id,
                product_id=data['product_id']
            ).first():
              
                record.update(**data)
            else:   
                data['user_id']=self.user_id
                record=self.model.create(**data)
            db.session.add(record)
            db.session.commit()
            return self._success('se creo exitosamente')
        except Exception as e:
            db.session.rollback()
            return self._getError(e,500)      

    def delete(self,product_id):
        try:
            if record:=self.model.where(
                product_id=product_id,
                user_id=self.user_id
              
            ).first():
                record.delete()
                db.session.commit()
                return self._success('se elimino exitosamente')
            return self._notExist()    
        except Exception as e:
            return self._getError(e,500)




    def _getError(self,error,typeError):
        return {
                'message': 'Ocurrio un error',
                'error': str(error)
            },typeError 


    def _success(self,message):
        return {
            'message':f'{message}'
        },200   

    def _notExist(self):
        return {
            'message':'No se encontro el producto en mencion'
        },404       