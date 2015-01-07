from django import template 
register = template.Library() 

@register.filter(name='filename')
def filename(value, arg):
	vl = value.path.split(arg)
	return vl[len(vl)-1]
