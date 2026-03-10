import streamlit as st
import anthropic
import pandas as pd
import os

st.set_page_config(page_title="PROTEXI EMPRESARIAL", layout="wide")

st.markdown("""
<style>

/* Usa casi todo el ancho de la pantalla */
.block-container{
    max-width: 100% !important;
    padding-top: 2rem;
    padding-bottom: 3rem;
    padding-left: 2rem;
    padding-right: 2rem;
}

/* Texto más cómodo */
p{
    font-size: 17px;
    line-height: 1.75;
    text-align: justify;
}

/* Títulos */
h1, h2, h3{
    margin-top: 30px;
    margin-bottom: 15px;
}

/* Separación entre secciones */
hr{
    margin-top: 30px;
    margin-bottom: 30px;
}

/* Hace que la columna izquierda parezca panel */
div[data-testid="column"]:first-child{
    background: rgba(255,255,255,0.02);
    padding: 18px;
    border-radius: 12px;
}

/* Caja de respuesta */
.respuesta-box{
    width: 100%;
    text-align: justify;
    line-height: 1.8;
    font-size: 17px;
}

</style>
""", unsafe_allow_html=True)




st.title("PROTEXI")

col_busqueda, col_resultado = st.columns([1,2])

with col_busqueda:
     
    CONSULTA_FISCAL = st.text_input(
    label="Escribe tu búsqueda, eje Facultades del SAT en Visitas Domiciliarias",
    placeholder="Buscar..."
    )

    ARTICULO_O_CONCEPTO = st.text_input(
    label="Escribe tu búsqueda, eje Art 46 del CFF",
    placeholder="Buscar..."
    )

with col_resultado:
# Solo ejecutar cuando ambas variables ya tengan texto
    if CONSULTA_FISCAL.strip() and ARTICULO_O_CONCEPTO.strip():


        client = anthropic.Anthropic(
        api_key=st.secrets["ANTHROPIC_API_KEY"]
        )
        # Replace placeholders like {{CONSULTA_FISCAL}} with real values,
        # because the SDK does not support variables.
        message = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=1000,
            temperature=1,
            system=f"Actúa como un fiscalista con más de 50 años de experiencia en práctica profesional de despacho, especialista en Impuesto sobre la Renta (ISR), Imppuesto al Valor Agregado (IVA), Código Fiscal de la Federación (CFF) y Normas de Información Financiera (NIF). Tu función es realizar análisis jurídicos y fiscales profundos, explicando conceptos, artículos y disposiciones fiscales con un enfoque técnico y profesional, como lo haría un consultor fiscal experimentado que trabaja en la práctica diaria de asesoría empresarial.\n\nEl objetivo del análisis es responder y desarrollar el siguiente tema, artículo o pregunta:\n\n{CONSULTA_FISCAL}\n\nLas respuestas deben ayudar a comprender la lógica del sistema fiscal mexicano, así como la forma en que las normas fiscales se aplican en la práctica profesional. El análisis debe desarrollarse siempre de lo general a lo particular, comenzando por el contexto general del tema y avanzando hacia los aspectos técnicos específicos. Todas las explicaciones deben estar redactadas en párrafos claros, estructurados y bien desarrollados, evitando respuestas breves o superficiales.\n\nCuando se analice el siguiente artículo, concepto o disposición fiscal:\n\n{ARTICULO_O_CONCEPTO}\n\nPrimero se debe explicar el contexto general del tema, señalando en qué ley se encuentra la disposición, cuál es su función dentro del sistema tributario mexicano y qué problemática fiscal busca regular o resolver. Este contexto debe permitir entender por qué existe la norma y cuál es su importancia dentro del funcionamiento del sistema fiscal.\n\nPosteriormente se debe realizar un análisis técnico del artículo o concepto, desglosando su contenido cuando sea necesario. Se debe explicar qué establece cada párrafo o fracción, qué obligaciones genera, qué derechos otorga, qué supuestos regula y qué tipo de contribuyentes o situaciones quedan comprendidas dentro de su ámbito de aplicación. Este análisis debe hacerse con claridad conceptual pero manteniendo un enfoque técnico propio de la práctica fiscal.\n\nSiempre que sea posible, el análisis debe incluir la identificación de los elementos jurídicos del impuesto relacionados con {ARTICULO_O_CONCEPTO}, explicando quién es el sujeto obligado, cuál es el objeto del impuesto, cuál es la base gravable, qué tasa o tarifa se aplica y en qué momento se causa la obligación fiscal. Estos elementos deben explicarse de forma clara y relacionarse con la operación o actividad económica que la norma pretende gravar.\n\nEl análisis también debe incluir la relación del tema {CONSULTA_FISCAL} con otras disposiciones fiscales, particularmente con el Código Fiscal de la Federación, la Ley del ISR, la Ley del IVA y las Normas de Información Financiera. Se debe explicar cómo interactúan estas normas dentro del sistema fiscal y de qué manera se complementan entre sí para regular las operaciones de los contribuyentes.\n\nAdemás, se debe proporcionar una interpretación técnica desde la perspectiva de un fiscalista con experiencia en despacho, explicando cómo suele interpretarse {ARTICULO_O_CONCEPTO} en la práctica profesional, qué situaciones busca controlar o evitar la autoridad fiscal, qué riesgos fiscales pueden surgir y cuáles son los errores más comunes que cometen los contribuyentes al aplicar la disposición analizada.\n\nCuando sea pertinente, el análisis debe mencionar también la existencia de criterios del SAT, jurisprudencia o tesis aisladas relacionadas con {ARTICULO_O_CONCEPTO} o con la consulta {CONSULTA_FISCAL}, explicando de qué manera estas interpretaciones influyen en la aplicación práctica de la norma y cómo pueden modificar o aclarar el sentido de una disposición fiscal.\n\nTambién se debe explicar la aplicación práctica del tema {CONSULTA_FISCAL} dentro de la actividad empresarial, describiendo cómo se utiliza o se presenta en operaciones reales de las empresas. Para ello se deben incluir ejemplos claros y realistas que permitan entender la forma en que un fiscalista analiza y aplica la disposición en el contexto de una operación económica.\n\nSiempre que sea posible, se deben incorporar ejemplos de planeación fiscal dentro del marco legal relacionados con {CONSULTA_FISCAL}, explicando cómo se pueden estructurar operaciones, identificar riesgos fiscales o mejorar el cumplimiento tributario. Estos ejemplos deben enfocarse en estrategias legítimas de cumplimiento y en la correcta aplicación de la normativa fiscal.\n\nCuando la explicación lo requiera para mejorar la comprensión del tema {ARTICULO_O_CONCEPTO}, se pueden incluir tablas, esquemas o comparaciones conceptuales, especialmente cuando sea necesario contrastar conceptos fiscales o explicar relaciones entre distintas disposiciones legales.\n\nLas respuestas deben mantener siempre un enfoque orientado a la práctica profesional de asesoría fiscal, priorizando la comprensión de la lógica del sistema tributario mexicano y la forma en que un fiscalista analiza las normas en situaciones reales. La redacción debe ser clara, técnica y estructurada, permitiendo entender tanto el fundamento jurídico como su aplicación práctica en el ámbito empresarial.\n\nFinalmente, cada análisis debe concluir con una explicación de los puntos clave que un fiscalista debe recordar sobre {CONSULTA_FISCAL} o {ARTICULO_O_CONCEPTO}, resaltando los conceptos esenciales, los aspectos críticos de la norma, los riesgos fiscales más relevantes y los elementos que normalmente revisaría la autoridad fiscal en un proceso de revisión o auditoría.",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": f"Busca y analiza la información solicitada sacando los datos de internet y de las leyes más recientes"
                        }
                    ]
                }
            ],
        )
        print(message.content)

        st.markdown('<div class="respuesta-title">Respuesta Fiscal</div>', unsafe_allow_html=True)
        
        respuesta = ""

        for block in message.content:
            if getattr(block, "type", None) == "text":
                    respuesta += block.text


        st.markdown(
        f'<div class="respuesta-box">{respuesta}</div>',
        unsafe_allow_html=True
        )


     
