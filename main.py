# 1 verificar uma api que utilize imagens
# 2 fazer o download/upload da imagem
# 2 selecionar uma imagem


from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label



class Tracer(App):
    def build(self):
        box = BoxLayout(orientation="vertical")
        label = Label(text="Bem vindo ao Tracer", font_size=70)
        box.add_widget(label)

        box2 = BoxLayout(orientation="vertical")
        button = Button(text="Clique aqui para selecionar a imagem na internet", font_size=30)
        box.add_widget(button)

        label2 = Label(text="Peso do Animal", font_size=30)
        box.add_widget(label2)
        box.add_widget(box2)
        return box

Tracer().run()