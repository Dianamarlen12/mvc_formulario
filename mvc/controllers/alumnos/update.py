import web

render = web.template.render("mvc/views/personas/", base="template)

class Update():

    def GET(self):
        try:
            return render.update() # renderizando formulario.html
        except Exception as e:
            return "Error " + str(e.args)

    def POST(self):
        try:
            form = web.input()
            print(form)
            print(form.aligned-number)
            print(form.aligned-name)
            print(form.aligned-apepate)
            print(form.aligned-apemate)
            print(form.stacked-state)
            print(form.party)
            print(form.checkbox-radio-option-two)
            print(form.stacked-state)
        except Exception as e:
            return "Error " + str(e.args)