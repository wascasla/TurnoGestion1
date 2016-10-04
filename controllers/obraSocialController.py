#controlador obras sociales
#encabezado = {'descripcion': 'Descripcion'}
#@auth.requires_login()
@auth.requires_membership('admin')
def administrar_os():	
    grid = SQLFORM.grid(db.obraSocial,user_signature=False,csv=False)
    return dict(grid=grid)