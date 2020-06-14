from jinja2 import Template,FileSystemLoader,Environment

class AnsibleTemplates:
    def __init__(self,templatename):
        self.templatename = templatename

    def rendertemplatefile(self,ambiente,gateway_ip,tomcat,oracle):
        # adicionar algumas validações
        loadtemplatejinja = FileSystemLoader(searchpath='./template_files/')
        templateEnv = Environment(loader=loadtemplatejinja)
        template = templateEnv.get_template(self.templatename)
        generatedfile = template.render(ambiente=ambiente,gateway_ip=gateway_ip,tomcat=tomcat,oracle=oracle)
        return generatedfile

    def createansiblefile(self,renderedfile,filename):
        #adicionar algumas validações
        #a de append
        with open(filename, mode='a') as configfile:
            configfile.write(renderedfile)
