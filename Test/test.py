#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 13:53:17 2019

@author: rosto
"""
import sys
sys.path.append("..")
import form
import builder
import row
import container
import column
from size import Size


cont = container.Container()
riga = row.Row()
colonna_form = column.Column()
colonna_form.add_col_size(12, Size.PICCOLO)
colonna_form.add_col_size(6, Size.MEDIO)

riga.add_child(colonna_form)
cont.add_child(riga)

f = form.Form(action_url="/login")

f.add_child(form.InputField("id_nome",label="Nome",inp_type=form.InputType.TEXT))
f.add_child(form.InputField("id_cognome", label="Email",inp_type=form.InputType.EMAIL))
f.add_child(form.InputField("id_psw", label="Password",inp_type=form.InputType.PASSWORD))
#f.add_child(form.InputField("id_cognome", label="Data prenotazione stampante 3D",inp_type=form.InputType.DATE))
f.add_child(form.SubmitButton(label="Accedi"))

colonna_form.add_child(f)

b = builder.Builder(cont)
b.imposta_titolo("Login gestore Fablab Imperia")

print(b)

