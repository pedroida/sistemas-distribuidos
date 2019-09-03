# coding=utf-8
import Pyro4

uri = input("URI Object? ").strip()
tickets = []
answer = "s"

ticket_generator = Pyro4.Proxy(uri)


def get_question_phrase():
    return "Deseja receber uma etiqueta? s/n " if (len(tickets) == 0) else "Deseja receber uma nova etiqueta? s/n "


def get_new_ticket():
    tickets.append(ticket_generator.generate())


while answer == "s":
    answer = raw_input(get_question_phrase()).strip()

    if answer == "s":
        get_new_ticket()

    print("suas etiquetas: {} \n".format(tickets))

if answer == "n":
    print("Requisição de etiquetas finalizada. Suas etiquetas são:\n{}".format(tickets))
else:
    print("Reposta inválida!")
