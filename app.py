import streamlit as st

# Configuración de la página con ancho de 1080px
st.set_page_config(
    page_title="Identidad de Marca - Yamileth Ospino",
    page_icon="",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Estilos CSS avanzados: Tipografía estilizada, jerarquía refinada y sin la regla de pestañas solicitada
st.markdown("""
    <style>
    /* Importar fuente editorial sofisticada de Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap');

    /* Ocultar elementos predeterminados de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Contenedor principal a 1080px */
    .block-container {
        max-width: 1080px !important;
        padding-top: 2.5rem !important;
        padding-bottom: 3.5rem !important;
        padding-left: 3rem !important;
        padding-right: 3rem !important;
        background-color: #FFFFFF;
        border-radius: 12px;
        box-shadow: 0 4px 25px rgba(0, 0, 0, 0.04);
        margin-top: 25px;
        margin-bottom: 25px;
    }
    
    /* Fondo general */
    .stApp {
        background-color: #F4F7F4;
    }
    
    /* Tipografía base más estilizada */
    body, p, span, li {
        color: #26332E !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        font-size: 15px;   /* 1.05rem */
        font-weight: 400;
        line-height: 1.7;
    }
    
    /* Subtítulos pequeños y captions con contraste y estilo */
    small, [data-testid="stCaptionContainer"] p {
        color: #4A5D53 !important;
        font-weight: 600 !important;
        font-size: 0.9rem !important;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    /* Encabezado principal */
    .hero-container {
        padding: 10px 0px 20px 0px;
        border-bottom: 2px solid #2D3A34;
        margin-bottom: 30px;
        text-align: center;
    }
    .main-title {
        color: #1A2420 !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        font-size: 2.3rem !important;
        font-weight: 700 !important;
        letter-spacing: -0.5px;
        margin-bottom: 6px;
        text-transform: uppercase;
    }
    .sub-title {
        color: #4A5D53 !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        font-size: 1.1rem !important;
        font-weight: 500;
        letter-spacing: 0.3px;
    }
    
    /* Pestañas horizontales limpias (sin la regla de selección anterior) */
    .stTabs [data-baseweb="tab-list"] {
        gap: 6px;
        background-color: #EEF2EE;
        padding: 8px;
        border-radius: 8px;
        margin-bottom: 30px;
        flex-wrap: wrap;
    }
    .stTabs [data-baseweb="tab"] {
        height: 42px;
        background-color: #FFFFFF;
        border-radius: 6px;
        color: #2D3A34 !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        font-weight: bold;
        font-size: 0.9rem;
        border: 1px solid #D1DCD5;
        padding: 0px 16px;
    }
    
    /* Cajas y contenedores */
    .highlight-box {
        background-color: #F8FAF8;
        padding: 24px 28px;
        border-radius: 8px;
        border-left: 4px solid #2D3A34;
        margin: 20px 0px;
        color: #1A2420 !important;
        border-top: 1px solid #E2E8E4;
        border-right: 1px solid #E2E8E4;
        border-bottom: 1px solid #E2E8E4;
    }
    
    .manifesto-box {
        background-color: #F8FAF8;
        padding: 35px;
        border-radius: 8px;
        font-style: italic;
        color: #1A2420 !important;
        line-height: 1.9;
        border: 1px solid #E2E8E4;
    }
    
    /* Jerarquía estricta de Títulos */
    h2 {
        color: #1A2420 !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        font-size: 1.6rem !important;
        font-weight: 700 !important;
        margin-top: 20px !important;
        margin-bottom: 15px !important;
        letter-spacing: -0.3px;
    }
    h3 {
        color: #2D3A34 !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        font-size: 1.25rem !important;
        font-weight: 600 !important;
        margin-top: 25px !important;
        margin-bottom: 10px !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- ENCABEZADO PRINCIPAL ---
st.markdown("""
    <div class="hero-container">
        <h1 class="main-title">Identidad de Marca</h1>
        <p class="sub-title">Yamileth Ospino &nbsp;|&nbsp; Psicología</p>
    </div>
""", unsafe_allow_html=True)

# --- MENÚ HORIZONTAL EN PESTAÑAS ---
tabs = st.tabs([
    "Inicio",
    "Hallazgo",
    "Visión y Misión",
    "Valores",
    "Personalidad",
    "Concepto",
    "Manifiesto",
    "Posicionamiento",
    "Tono",
    "Síntesis"
])

# --- 0. VISTA GENERAL ---
with tabs[0]:
    st.markdown("""
    <div class="highlight-box">
        <b>Idea estratégica central:</b><br>
        <i>El bienestar se construye a lo largo de la vida.</i>
    </div>
    """, unsafe_allow_html=True)
    
    st.write(
        "Documento de trabajo que sintetiza la **propuesta de identidad estratégica**. "
        "Su propósito es servir como base para validar la esencia, el posicionamiento "
        "y la futura expresión visual y verbal de la marca."
    )
    

# --- 01. HALLAZGO ESTRATÉGICO ---
with tabs[1]:
    st.header("01. Hallazgo estratégico")
    st.write(
        "La marca entiende la psicología no únicamente como una intervención cuando aparece un problema, "
        "sino como un **acompañamiento** que puede aportar en distintas etapas y circunstancias de la vida. "
        "La propuesta combina **escucha sin juicio**, preparación profesional, orientación y herramientas para que "
        "cada persona pueda comprender mejor lo que vive y tomar sus propias decisiones."
    )
    
    st.subheader("Los cuatro pilares")
    st.markdown("""
    * **Escucha sin juicio:** Crear un espacio en el que la persona pueda expresarse con confianza y respeto.
    * **Conocimiento profesional:** Sostener el acompañamiento en preparación, actualización y responsabilidad ética.
    * **Autonomía y orientación:** Facilitar comprensión y herramientas, sin imponer respuestas ni decidir por la persona.
    * **Prevención y continuidad:** Reconocer que el cuidado de la salud mental puede ser relevante antes de una crisis y a lo largo de la vida.
    """)

# --- 02. VISIÓN Y MISIÓN ---
with tabs[2]:
    st.header("02. Visión y misión")
    
    st.subheader("Visión propuesta")
    st.caption("Hacia dónde quiere contribuir la marca")
    st.markdown("""
    <div class="highlight-box">
        Contribuir a una sociedad que reconozca la salud mental como <b>parte esencial del bienestar durante toda la vida</b>, donde las personas puedan acceder a acompañamiento psicológico oportuno y desarrollar herramientas para afrontar sus desafíos y vivir con mayor bienestar.
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("Misión propuesta")
    st.caption("Qué ofrece y cómo lo hace")
    st.markdown("""
    <div class="highlight-box">
        Brindar <b>acompañamiento psicológico profesional, empático y basado en evidencia</b>, que permita a las personas comprender sus pensamientos, emociones y conductas, afrontar los desafíos de las distintas etapas de la vida y desarrollar herramientas para tomar sus propias decisiones y mejorar su bienestar.
    </div>
    """, unsafe_allow_html=True)

# --- 03. VALORES DE MARCA ---
with tabs[3]:
    st.header("03. Valores de marca")
    st.markdown("""
    * **Empatía y respeto:** Escuchar con atención, reconocer la historia de cada persona y *evitar juicios o etiquetas*.
    * **Ética y autonomía:** Cuidar la confidencialidad y los límites profesionales, *respetando la capacidad de cada persona para decidir*.
    * **Rigor y aprendizaje continuo:** Mantener una práctica responsable, *fundamentada en el conocimiento* y abierta a la actualización.
    * **Independencia y empoderamiento:** Ofrecer orientación y herramientas para que las personas *comprendan su situación* y tomen decisiones propias.
    * **Prevención y continuidad:** Promover una mirada del bienestar psicológico que *no se limite a responder a una crisis puntual*.
    """)

# --- 04. PERSONALIDAD DE MARCA ---
with tabs[4]:
    st.header("04. Personalidad de marca")
    st.write(
        "La marca se expresa como una **profesional cercana y confiable**, con calidez humana y una base científica clara. "
        "La cercanía transmite seguridad sin borrar los límites del vínculo profesional."
    )
    st.markdown("""
    * **Cercana:** Humana y accesible, *sin confundirse con una relación de amistad*.
    * **Científica:** Demuestra preparación y criterio, *explicando con claridad y sensibilidad*.
    * **Reflexiva:** Invita a comprender y explorar, *sin decirle a la persona cómo debe vivir*.
    * **Profesional:** Transmite confianza y estructura *sin recurrir a un lenguaje institucional distante*.
    * **Metódica y contemporánea:** Proyecta orden, actualización y *apertura a distintas realidades*.
    """)

# --- 05. CONCEPTO ---
with tabs[5]:
    st.header("05. Concepto")
    
    st.subheader("Principal")
    st.markdown("""
    <div class="highlight-box">
        <b>El bienestar se construye a lo largo de la vida</b><br>
        <i>Este concepto permite hablar de desarrollo, cambios, prevención, aprendizaje y continuidad. Amplía la percepción de la psicología más allá de la crisis y da coherencia a una práctica que acompaña distintas etapas.</i>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("Complementarios")
    st.markdown("""
    * **Un espacio para comprender y avanzar:** Expresa la experiencia que la persona puede encontrar: *escucha, confianza, claridad, herramientas y autonomía*.
    * **Ciencia que acompaña:** Comunica la unión entre *conocimiento profesional, humanidad y confianza*.
    """)
    
    st.subheader("Arquitectura conceptual sugerida")
    tabla_arq = [
        {"Nivel": "Centro", "Función": "Define la visión amplia", "Idea": "El bienestar se construye a lo largo de la vida"},
        {"Nivel": "Experiencia", "Función": "Describe cómo se siente el acompañamiento", "Idea": "Un espacio para comprender y avanzar"},
        {"Nivel": "Fundamento", "Función": "Explica por qué confiar", "Idea": "Ciencia que acompaña"}
    ]
    st.table(tabla_arq)

# --- 06. MANIFIESTO ---
with tabs[6]:
    st.header("06. Manifiesto de marca")
    st.markdown("""
    <div class="manifesto-box">
        “La salud mental importa en cada etapa de la vida.<br><br>
        Creemos que cuidar la salud mental no debería ser el último recurso cuando sentimos que ya no podemos más. Todas las personas atraviesan cambios, decisiones y momentos que pueden transformar su manera de pensar, sentir y vivir. No tenemos que recorrerlos sin apoyo.<br><br>
        Acompañar no significa decirle a alguien cómo vivir. Significa escuchar sin juzgar, comprender su historia, ofrecer herramientas y ayudarle a encontrar claridad para tomar sus propias decisiones.<br><br>
        Creemos en una psicología profesional, fundamentada en el conocimiento y ejercida con empatía, respeto y responsabilidad. Una psicología que reconoce a la persona más allá de sus dificultades y que comprende que su bienestar también está relacionado con su historia, su entorno y sus vínculos.<br><br>
        Queremos contribuir a que pedir ayuda sea una posibilidad y no un motivo de vergüenza; a que el cuidado de la salud mental pueda comenzar antes de una crisis y continuar a lo largo de la vida.<br><br>
        Porque cada persona merece ser escuchada, comprendida y acompañada con respeto.<br><br>
        <b>El bienestar también se construye. Y no tenemos que hacerlo a solas.</b>”
    </div>
    """, unsafe_allow_html=True)

# --- 07. POSICIONAMIENTO ---
with tabs[7]:
    st.header("07. Posicionamiento")
    st.subheader("Declaración de posicionamiento propuesta")
    st.markdown("""
    <div class="highlight-box">
        Para las personas que buscan comprender lo que están viviendo y desarrollar herramientas para afrontar los desafíos de la vida, <b>La marca ofrece acompañamiento psicológico cercano, profesional y fundamentado en el conocimiento</b>, que combina escucha sin juicio, orientación y una visión integral de la persona.
    </div>
    """, unsafe_allow_html=True)
    
    st.write(
        "La promesa no es resolver la vida de la persona ni garantizar resultados rápidos; "
        "es ofrecer un **espacio profesional para comprender**, explorar opciones y desarrollar recursos propios."
    )

# --- 08. TONO Y LENGUAJE ---
with tabs[8]:
    st.header("08. Tono y lenguaje")
    
    tabla_tono = [
        {"Dimensión": "Cercanía", "Cómo se expresa": "Cálida, respetuosa y accesible", "Evitar": "Exceso de confianza o familiaridad"},
        {"Dimensión": "Claridad", "Cómo se expresa": "Palabras sencillas, ideas concretas", "Evitar": "Tecnicismos innecesarios o frases ambiguas"},
        {"Dimensión": "Profesionalismo", "Cómo se expresa": "Conocimiento explicado con claridad", "Evitar": "Tono frío, rígido o excesivamente institucional"},
        {"Dimensión": "Reflexión", "Cómo se expresa": "Preguntas que invitan a comprender", "Evitar": "Imponer conclusiones o dar lecciones"},
        {"Dimensión": "Esperanza realista", "Cómo se expresa": "Hablar de posibilidades, herramientas y procesos", "Evitar": "Promesas de cambio inmediato o frases motivacionales vacías"}
    ]
    st.table(tabla_tono)
    
    st.subheader("Ejemplos de lenguaje")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Preferible:**\n- *“Podemos explorar lo que estás viviendo y las herramientas que podrían ayudarte”*.\n- *“Pedir apoyo también puede ser una forma de cuidarte”*.")
    with col2:
        st.markdown("**Evitar:**\n- *“Te voy a decir qué tienes que hacer”*.\n- *“Vas a cambiar tu vida en pocas sesiones”*.")

# --- 09. SÍNTESIS ---
with tabs[9]:
    st.header("09. Síntesis")
    st.subheader("Propuesta de síntesis")
    tabla_sintesis = [
        {"Elemento": "Visión", "Propuesta": "Una sociedad que reconozca la salud mental en todas las etapas de la vida."},
        {"Elemento": "Misión", "Propuesta": "Acompañamiento profesional, empático y fundamentado en conocimiento."},
        {"Elemento": "Valores", "Propuesta": "Empatía, ética, rigor, autonomía, prevención y continuidad."},
        {"Elemento": "Personalidad", "Propuesta": "Cercana, reflexiva, científica, metódica y confiable."},
        {"Elemento": "Concepto", "Propuesta": "El bienestar se construye a lo largo de la vida."},
        {"Elemento": "Manifiesto", "Propuesta": "La salud mental importa en cada etapa de la vida."},
        {"Elemento": "Posicionamiento", "Propuesta": "Acompañamiento cercano y profesional, con escucha, orientación y herramientas."},
        {"Elemento": "Tono", "Propuesta": "Cercano sin exceso de informalidad; científico sin frialdad; claro sin simplificar en exceso."}
    ]
    st.table(tabla_sintesis)
