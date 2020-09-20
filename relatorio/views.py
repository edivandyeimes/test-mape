from .models import Consulta, Exame
from django.shortcuts import render
from django.urls import reverse
from django.db import connection



# funcao que retorna o relatorio com todas as consultas medicas.
def relatorio(request):
    context = {} 
    cursor = connection.cursor()
    cursor.execute("""SELECT con.nome_medico, con.numero_guia, con.data_consulta, 
    con.valor_consulta,sum(ex.valor_exame) as soma_exame, count(ex.numero_guia_consulta) 
    FROM consulta as con, exame as ex 
    WHERE con.numero_guia = ex.numero_guia_consulta 
    GROUP BY con.numero_guia ORDER BY soma_exame DESC""")
    results = cursor.fetchall()  

    context['consulta_list'] = results
    return render(request, 'consulta_list.html', context)



# funcao de filtro para os dados do relatorio.
# filtra por nome do medico e/ou por periodo.
def relatorio_filtro(request):
    context = {}
    sql = ""
    med = request.GET.get('med')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    if med is not None:
        sql = """SELECT con.nome_medico, con.numero_guia, con.data_consulta, con.valor_consulta, 
            sum(ex.valor_exame) as soma_exame, count(ex.numero_guia_consulta) 
            FROM consulta as con, exame as ex 
            WHERE con.numero_guia = ex.numero_guia_consulta AND con.nome_medico = '"""+ med +"""' """

        if start_date is not None and start_date != '' and end_date is not None and end_date != '':
            sql = sql+"AND con.data_consulta BETWEEN '"+str(start_date)+"' AND '"+str(end_date)+"' "
        sql = sql+"GROUP BY con.numero_guia ORDER BY soma_exame DESC"
    
    else:
        if start_date is not None and start_date != '' and end_date is not None and end_date != '':
            sql = """SELECT con.nome_medico, con.numero_guia, con.data_consulta, con.valor_consulta, 
                sum(ex.valor_exame) as soma_exame, count(ex.numero_guia_consulta) 
                FROM consulta as con, exame as ex 
                WHERE con.numero_guia = ex.numero_guia_consulta 
                AND """+"con.data_consulta BETWEEN '"+str(start_date)+"' AND '"+str(end_date)+"' "+"""
                GROUP BY con.numero_guia ORDER BY soma_exame DESC"""
    
    if sql is not None and sql != "":
        cursor = connection.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        context['consulta_list'] = results
        return render(request, '_filtro_med.html', context)
    
    else:
        return render(request, 'consulta_list.html', context)

    