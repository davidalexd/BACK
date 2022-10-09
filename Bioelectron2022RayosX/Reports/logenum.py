class LogEnumFormatos():
    FORMATO_CREATED = 'Nuevo formato creado por '
    FORMATO_UPDATED = 'Formato actualizado por '
    FORMATO_REMOVED = 'Formato removido por '
    FORMATO_ENABLED = 'Formato inhabilitado por '

class LogEnumCategoryFormatos():
    CATEGORY_FORMATO_CREATED = 'Nueva categoría de formato creada por '
    CATEGORY_FORMATO_UPDATED = 'Categoría de formato actualizada por '
    CATEGORY_FORMATO_REMOVED = 'Categoría de formato removida por '
    CATEGORY_FORMATO_ENABLED = 'Categoría de formato inhabilitada por '

def OrganizacionLog(author,instance,message,relacion):
    relacion.objects.create(model=instance,model_user=author.request.user,context=message+author.request.user.username)


