import streamlit as st
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import requests

# =========================
# NATION DATA
# =========================

nation_data = pd.read_excel("網路APP檔案.xlsx")

countries = sorted(
    nation_data["Country"]
    .dropna()
    .astype(str)
    .str.strip()
    .tolist()
)

# =========================
# PAGE SETUP
# =========================
st.set_page_config(
    page_title="MY NET ZERO | GNPA",

    layout="wide"
)


# =========================
# HERO VIDEO
# =========================
if st.session_state.get("hero_visible", True):
    st.video(
        "hero.mp4",
        autoplay=True,
        muted=True,
        loop=False
    )

# =========================
# COLORS / STYLE
# =========================
st.markdown("""
<style>

.stApp {
    background-color: #FAFAF7;
}

.block-container {
    max-width: 1150px;
    padding-top: 45px;
    padding-bottom: 80px;
}

.gnpa {
    color: #2F765D;
    font-size: 14px;
    font-weight: 700;
    letter-spacing: 3px;
}

.agency {
    color: #68757D;
    font-size: 15px;
    margin-top: 5px;
}

.main-title {
    color: #123047;
    font-size: 70px;
    font-weight: 750;
    letter-spacing: -3px;
    margin-top: 55px;
    margin-bottom: 5px;
}

.world-title {
    color: #2F765D;
    font-size: 18px;
    font-weight: 700;
    letter-spacing: 4px;
    margin-bottom: 70px;
}

.small-title {
    color: #68757D;
    font-size: 14px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.formula {
    color: #123047;
    font-size: 42px;
    font-weight: 650;
    margin-top: 10px;
    margin-bottom: 35px;
}

.divider {
    height: 1px;
    background-color: #D9DEDB;
    margin-top: 25px;
    margin-bottom: 50px;
}

.diet-title {
    color: #123047;
    font-size: 32px;
    font-weight: 750;
    letter-spacing: 3px;
}

.number-title {
    color: #68757D;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 2px;
}

.big-number {
    color: #123047;
    font-size: 43px;
    font-weight: 700;
}

.small-number {
    color: #68757D;
    font-size: 14px;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)

# =========================
# GNPA
# =========================

st.markdown(
    '<div style="font-size:24px; font-weight:800; color:#2F765D; '
    'letter-spacing:6px; margin-top:28px; margin-bottom:6px;">'
    'GNPA'
    '</div>'
    '<div style="font-size:14px; font-weight:600; color:#123047; '
    'letter-spacing:1.6px; text-transform:uppercase; margin-bottom:5px;">'
    'Global Nature & Plant-based Diet Shift Agency'
    '</div>'
    '<div style="font-size:13px; font-weight:500; color:#68757D; '
    'letter-spacing:0.5px; margin-bottom:34px;">'
    'Agence mondiale pour la nature et la transition vers une alimentation végétale'
    '</div>',
    unsafe_allow_html=True
)




# =========================
# À PROPOS DE GNPA
# =========================

with st.expander("À PROPOS DE GNPA"):
    st.markdown(
        """
**Global Nature & Plant-based Transition alimentaire Agency (GNPA)**

GNPA est une initiative axée sur la recherche qui explore les relations entre
les systèmes alimentaires, la restauration de la nature, le changement climatique et la trajectoire vers le Net Zero.

**MY NET ZERO** traduit cette recherche en une plateforme interactive,
permettant aux individus, aux nations et au public mondial d’explorer comment les changements
alimentaires et la restauration de la nature peuvent influencer les résultats climatiques.

La plateforme est conçue pour relier la recherche scientifique à la compréhension
du public et au débat sur les politiques publiques.
        """
    )

# =========================
# CONTACT / POSER UNE QUESTION
# =========================

with st.expander("CONTACT / POSER UNE QUESTION"):

    with st.form("contact_form"):

        contact_name = st.text_input("Nom")
        contact_organization = st.text_input("Organisation")
        contact_country = st.text_input("Pays")
        contact_email = st.text_input("Email")
        contact_message = st.text_area("Question / Message")

        contact_submit = st.form_submit_button("ENVOYER")

    if contact_submit:

        if not contact_name or not contact_email or not contact_message:
            st.warning(
                "Veuillez indiquer votre nom, votre e-mail et votre question/message."
            )

        else:
            form_data = {
                "name": contact_name,
                "organization": contact_organization,
                "country": contact_country,
                "email": contact_email,
                "message": contact_message
            }

            try:
                response = requests.post(
                    "https://formspree.io/f/xeaobwry",
                    data=form_data,
                    timeout=10
                )

                if response.ok:
                    st.success(
                        "Merci. Votre message a été envoyé avec succès."
                    )
                else:
                    st.error(
                        "Votre message n’a pas pu être envoyé. Veuillez réessayer."
                    )

            except requests.RequestException:
                st.error(
                    "Votre message n’a pas pu être envoyé. Veuillez réessayer."
                )

    st.caption(
        "Vos informations seront utilisées uniquement pour répondre à votre demande."
    )

# =========================
# MY NET ZERO
# =========================
st.markdown(
    '<div class="main-title">MY NET ZERO</div>',
    unsafe_allow_html=True
)

# =========================
# MAIN NAVIGATION
# =========================

nav1, nav2, nav3, nav4 = st.columns(4)

with nav1:
    for_me = st.button(
        "POUR MOI",
        use_container_width=True
    )

with nav2:
    my_nation = st.button(
        "MON PAYS",
        use_container_width=True
    )

with nav3:
    our_world = st.button(
        "NOTRE MONDE",
        use_container_width=True
    )

with nav4:
    beyond_net_zero = st.button(
        "AU-DELÀ DU NET ZERO",
        use_container_width=True
    )


# =========================
# MON PAYS SELECTOR
# =========================

# =========================
# PAGE SELECTION
# =========================

if "show_nation" not in st.session_state:
    st.session_state.show_nation = False

if "show_for_me" not in st.session_state:
    st.session_state.show_for_me = False

if "show_beyond" not in st.session_state:
    st.session_state.show_beyond = False

if "hero_visible" not in st.session_state:
    st.session_state.hero_visible = True

if for_me:
    st.session_state.show_for_me = True
    st.session_state.show_nation = False
    st.session_state.show_beyond = False
    st.session_state.hero_visible = False

if my_nation:
    st.session_state.show_for_me = False
    st.session_state.show_nation = True
    st.session_state.show_beyond = False
    st.session_state.hero_visible = False

if our_world:
    st.session_state.show_for_me = False
    st.session_state.show_nation = False
    st.session_state.show_beyond = False
    st.session_state.hero_visible = False

if beyond_net_zero:
    st.session_state.show_for_me = False
    st.session_state.show_nation = False
    st.session_state.show_beyond = True
    st.session_state.hero_visible = False

# =========================
# PAGE BACKGROUND
# =========================

if st.session_state.show_for_me:
    page_bg = "#FCECEF"

elif st.session_state.show_nation:
    page_bg = "#F6F0DF"

elif st.session_state.show_beyond:
    page_bg = "#EAF5ED"

else:
    page_bg = "#EAF4F8"

st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {page_bg};
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# AU-DELÀ DU NET ZERO
# =========================

if st.session_state.show_beyond:

    st.markdown(
        '<div style="font-size:48px; font-weight:750; color:#123047; '
        'margin-top:55px; letter-spacing:-1px;">'
        'AU-DELÀ DU NET ZERO'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="font-size:30px; font-weight:700; color:#2F765D; '
        'margin-top:8px; margin-bottom:35px;">'
        'UN AVENIR PROSPÈRE'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="font-size:21px; line-height:1.8; color:#123047; '
        'max-width:850px; margin-bottom:50px;">'
        'Changer un système non durable ne signifie pas renoncer à l’avenir.<br>'
        'Il s’agit d’ouvrir la voie à un avenir plus abondant, plus avancé, '
        'et plus enthousiasmant que nous ne l’avions imaginé.'
        '</div>',
        unsafe_allow_html=True
    )

    future1, future2, future3, future4 = st.columns(4)

    with future1:
        st.markdown("### SÉCURITÉ ALIMENTAIRE")

    with future2:
        st.markdown("### UNE PLANÈTE RESTAURÉE")

    with future3:
        st.markdown("### STABILITÉ CLIMATIQUE")

    with future4:
        st.markdown("### PROGRÈS HUMAIN")
     
# =========================
# POUR MOI
# =========================

if st.session_state.show_for_me:

    st.markdown(
        '<div style="font-size:32px; font-weight:700; color:#123047; '
        'margin-top:30px;">POUR MOI</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="color:#2F765D; font-size:15px; font-weight:700; '
        'letter-spacing:2px; margin-top:25px;">INDICE MY NET ZERO</div>',
        unsafe_allow_html=True
    )

    if "diet_choice" not in st.session_state:
        st.session_state.diet_choice = "D’ORIGINE ANIMALE"

    if st.session_state.diet_choice == "VÉGÉTAL":
        my_net_zero_index = -6
    else:
        my_net_zero_index = 10

    st.markdown(
        f'<div style="font-size:64px; font-weight:750; color:#123047; '
        f'margin-top:5px; margin-bottom:30px;">{my_net_zero_index}</div>',
        unsafe_allow_html=True
    )
    

    personal1, personal2 = st.columns(2)

    with personal1:
        st.markdown(
            '<div class="number-title">VIE QUOTIDIENNE</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            '<div style="font-size:46px; font-weight:700; color:#123047; '
            'margin-top:10px;">2</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            '<div class="small-number">'
            'Énergie · Transport · Cuisine · Appareils'
            '</div>',
            unsafe_allow_html=True
        )

    with personal2:

        st.markdown(
            '<div class="number-title">ALIMENTATION</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            '<div style="font-size:46px; font-weight:700; color:#123047; '
            'margin-top:10px;">8</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            '<div class="small-number">'
            'Système alimentaire d’origine animale'
            '</div>',
            unsafe_allow_html=True
        )

    st.markdown(
        '<div style="height:35px;"></div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="color:#2F765D; font-size:15px; font-weight:700; '
        'letter-spacing:2px;">VOTRE ALIMENTATION</div>',
        unsafe_allow_html=True
    )

    diet1, diet2 = st.columns(2)

    if "diet_choice" not in st.session_state:
        st.session_state.diet_choice = "D’ORIGINE ANIMALE"

    with diet1:
        plant_based = st.button(
            "VÉGÉTAL",
            use_container_width=True
        )

        if plant_based:
            st.session_state.diet_choice = "VÉGÉTAL"
            st.rerun()

    with diet2:
        animal_based = st.button(
            "D’ORIGINE ANIMALE",
            use_container_width=True
        )

        if animal_based:
            st.session_state.diet_choice = "D’ORIGINE ANIMALE"
            st.rerun()

  
    if st.session_state.diet_choice == "VÉGÉTAL":

        st.markdown(
            '<div style="height:35px;"></div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div style="color:#2F765D; font-size:15px; font-weight:700; '
            'letter-spacing:2px; margin-bottom:20px;">QU’EST-CE QUI CHANGE ?</div>',
            unsafe_allow_html=True
        )

        # FIRST ROW
        change1, change2, change3 = st.columns(3)

        with change1:
            st.markdown(
                '<div class="number-title">RÉDUCTION DU MÉTHANE</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                '<div style="font-size:27px; font-weight:700; color:#123047; '
                'margin-top:10px;">RÉDUIT</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                '<div class="small-number">émissions de méthane liées à l’élevage</div>',
                unsafe_allow_html=True
            )

        with change2:
            st.markdown(
                '<div class="number-title">TERRES LIBÉRÉES</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                '<div style="font-size:32px; font-weight:700; color:#123047; '
                'margin-top:10px;">78%</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                '<div class="small-number">des terres agricoles mondiales</div>',
                unsafe_allow_html=True
            )

        with change3:
            st.markdown(
                '<div class="number-title">RESTAURATION DES FORÊTS</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                '<div style="font-size:32px; font-weight:700; color:#123047; '
                'margin-top:10px;">41%</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                '<div class="small-number">de la déforestation tropicale liée à la production de bœuf</div>',
                unsafe_allow_html=True
            )

        # SPACE BETWEEN TWO ROWS
        st.markdown(
            '<div style="height:30px;"></div>',
            unsafe_allow_html=True
        )

        # SECOND ROW
        change4, change5, change6 = st.columns(3)

        with change4:
            st.markdown(
                '<div class="number-title">ABSORPTION NATURELLE DU CO₂</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                '<div style="font-size:27px; font-weight:700; color:#123047; '
                'margin-top:10px;">RESTAURÉE</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                '<div class="small-number">grâce à la restauration des écosystèmes</div>',
                unsafe_allow_html=True
            )

        with change5:
            st.markdown(
                '<div class="number-title">RESTAURATION DES ZONES MORTES OCÉANIQUES</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                '<div style="font-size:32px; font-weight:700; color:#123047; '
                'margin-top:10px;">80%</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                '<div class="small-number">les zones mortes se rétablissent et les forêts marines côtières reprennent l’absorption du CO₂</div>',
                unsafe_allow_html=True
            )

        with change6:
            st.markdown(
                '<div class="number-title">RÉDUCTION DE L’ÉNERGIE FOSSILE</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                '<div style="font-size:32px; font-weight:700; color:#123047; '
                'margin-top:10px;">41%</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                '<div class="small-number">attribuée à la consommation d’énergie du système d’élevage</div>',
                unsafe_allow_html=True
            )

if st.session_state.show_nation:
    selected_country = st.selectbox(
        "SÉLECTIONNEZ VOTRE PAYS",
        countries
    )

    selected_row = nation_data[
        nation_data["Country"].astype(str).str.strip() == selected_country
    ].iloc[0]

    selected_region = selected_row["Groups"]

    st.markdown(
        f'<div style="font-size:32px; font-weight:700; color:#123047; '
        f'margin-top:25px;">{selected_country.upper()}</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div style="font-size:16px; color:#68757D; '
        f'margin-top:5px;">{selected_region}</div>',
        unsafe_allow_html=True
    )
    
     
    co2_impact = selected_row["Cow's CO2  impact "]
    gdp_impact = selected_row["COW's GDP impacts"]

  
    # =========================
    # SCORE NET ZERO
    # =========================

    ghg_net_zero = selected_row["Net Zero Score --GHG-IPCC"]
    my_net_zero = selected_row["MY NZ Research Model Outome"]

    st.markdown(
        '<div style="font-size:20px; font-weight:800; color:#2F765D; '
        'letter-spacing:2px; margin-top:40px; margin-bottom:18px;">'
        'SCORE NET ZERO'
        '</div>',
        unsafe_allow_html=True
    )

    with st.container(border=True):

        score1, score2 = st.columns(2)

        with score1:
            st.markdown(
                '<div style="font-size:14px; font-weight:700; color:#2F765D; '
                'letter-spacing:2px;">GES — MODÈLE DU GIEC</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                f'<div style="font-size:30px; font-weight:700; color:#123047; '
                f'margin-top:18px; margin-bottom:18px;">{ghg_net_zero}</div>',
                unsafe_allow_html=True
            )

        with score2:
            st.markdown(
                '<div style="font-size:14px; font-weight:700; color:#2F765D; '
                'letter-spacing:2px;">MODÈLE DE RECHERCHE MY NET ZERO</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                f'<div style="font-size:30px; font-weight:700; color:#123047; '
                f'margin-top:18px; margin-bottom:18px;">{my_net_zero}</div>',
                unsafe_allow_html=True
            )

    st.markdown(
        '<div style="height:35px;"></div>',
        unsafe_allow_html=True
    )






    result1, result2 = st.columns(2)

    with result1:
        st.markdown(
            '<div class="number-title">IMPACT CO₂ DE L’ÉLEVAGE</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            f'<div style="font-size:38px; font-weight:700; '
            f'color:#123047; margin-top:10px;">{co2_impact*100:,.0f}%</div>',
            unsafe_allow_html=True
        )

    with result2:
        st.markdown(
            '<div class="number-title">IMPACT DE L’ÉLEVAGE SUR LE PIB</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            f'<div style="font-size:38px; font-weight:700; '
            f'color:#123047; margin-top:10px;">{gdp_impact*100:,.0f}%</div>',
            unsafe_allow_html=True
        )

    regional_co2 = selected_row["Livestock CO2 Region"]
    regional_gdp = selected_row["Livestock GDP Region"]

    st.markdown(
        f'<div style="font-size:15px; font-weight:700; color:#2F765D; '
        f'letter-spacing:2px; margin-top:35px;">'
        f'{selected_region.upper()} — COMPARAISON RÉGIONALE</div>',
        unsafe_allow_html=True
    )

    region1, region2 = st.columns(2)

    with region1:
        st.markdown(
            '<div class="number-title">IMPACT CO₂ RÉGIONAL</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            f'<div style="font-size:30px; font-weight:700; color:#123047; '
            f'margin-top:8px;">{regional_co2 * 100:,.0f}%</div>',
            unsafe_allow_html=True
        )

    with region2:
        st.markdown(
            '<div class="number-title">IMPACT RÉGIONAL SUR LE PIB</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            f'<div style="font-size:30px; font-weight:700; color:#123047; '
            f'margin-top:8px;">{regional_gdp * 100:,.0f}%</div>',
            unsafe_allow_html=True
        )


    # =========================
    # BASE DE CALCUL
    # =========================

    st.markdown(
        '<div style="height:25px;"></div>',
        unsafe_allow_html=True
    )

    basis1, basis2 = st.columns(2)

    with basis1:
        st.markdown(
            '<div style="border:1px solid #D9DEDB; border-radius:8px; padding:20px 24px; min-height:250px;">'
            '<div style="color:#123047; font-size:15px; font-weight:700; letter-spacing:1.5px; margin-bottom:18px;">IMPACT CO₂ — BASE DE CALCUL</div>'
            '<div style="color:#68757D; font-size:15px; line-height:2;">Émissions de méthane<br>Terres de pâturage<br>Déforestation<br>Consommation d’énergie<br>Combustibles fossiles</div>'
            '</div>',
            unsafe_allow_html=True
        )

    with basis2:
        st.markdown(
            '<div style="border:1px solid #D9DEDB; border-radius:8px; padding:20px 24px; min-height:250px;">'
            '<div style="color:#123047; font-size:15px; font-weight:700; letter-spacing:1.5px; margin-bottom:18px;">IMPACT SUR LE PIB — BASE DE CALCUL</div>'
            '<div style="color:#68757D; font-size:15px; line-height:2;">Émissions de méthane<br>Eau<br>Érosion des sols<br>Déforestation<br>Cultures fourragères</div>'
            '</div>',
            unsafe_allow_html=True
        )

    st.markdown(
        '<div style="color:#68757D; font-size:13px; margin-top:12px;">'
        'Les résultats sont calculés à l’aide du modèle de recherche MY NET ZERO.'
        '</div>',
        unsafe_allow_html=True
    )
    
    # =========================
    # MESSAGE NATIONAL CLÉ
    # =========================

    national_message = selected_row["Key national message"]

    st.markdown(
        '<div style="height:30px;"></div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="color:#2F765D; font-size:14px; font-weight:700; '
        'letter-spacing:2px;">MESSAGE NATIONAL CLÉ</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div style="color:#123047; font-size:20px; line-height:1.7; '
        f'margin-top:12px; margin-bottom:20px;">{national_message}</div>',
        unsafe_allow_html=True
    )



st.markdown(
    '<div class="world-title">NET ZERO MONDIAL</div>',
    unsafe_allow_html=True
)


# =========================
# NET ZERO FORMULAS
# =========================
col1, col2 = st.columns(2)

with col1:

    st.markdown(
        '<div class="small-title">'
        'Net Zero conventionnel'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="formula">'
        '1 − 1 = 0'
        '</div>',
        unsafe_allow_html=True
    )

with col2:

    st.markdown(
        '<div class="small-title">'
        'Écart réel vers le Net Zero'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '''
        <div style="
            color:#123047;
            font-size:34px;
            font-weight:600;
            margin-top:10px;
            line-height:1.25;
            white-space:nowrap;
        ">
            Net Zero = 1 − (0.25 − 11.87)
        </div>

        <div style="
            color:#123047;
            font-size:58px;
            font-weight:750;
            letter-spacing:-2px;
            margin-top:12px;
            margin-bottom:25px;
        ">
            = 12.62
        </div>
        ''',
        unsafe_allow_html=True
    )

  


# =========================
# WHY
# =========================
with st.expander("POURQUOI ?"):

    st.image(
        "net_zero_gap.png.png",
        caption="Figure 1.1. Mesure de la distance entre la situation actuelle et la réussite climatique.",
        use_container_width=True
    )

    st.markdown("""
### L’ÉCART VERS LE NET ZERO

**Écart de CO₂ atmosphérique**

426 ppm − 350 ppm ≈ **76 ppm**

**Équivalent CO₂**

76 ppm × 7.81 GtCO₂/ppm ≈ **593 GtCO₂**

**Équivalent en années d’émissions mondiales**

593 GtCO₂ ÷ 50 GtCO₂/year ≈ **11.87 years**

**Modèle MY NET ZERO**

1 − (0.25 − 11.87) ≈ **12.62**

*Base de conversion : Poljak (2023), où chaque ppm de CO₂ atmosphérique ≈ 7,81 GtCO₂.*
""")

st.markdown(
    '<div class="divider"></div>',
    unsafe_allow_html=True
)


# =========================
# TRANSITION ALIMENTAIRE
# =========================
st.markdown(
    '<div class="diet-title">TRANSITION ALIMENTAIRE</div>',
    unsafe_allow_html=True
)


diet_shift = st.slider(
    "Transition alimentaire",
    0,
    100,
    0,
    1,
    label_visibility="collapsed"
)


# =========================
# CALCULATION
# =========================

MAX_CO2 = 643.0

START_PPM = 426.0
TARGET_PPM = 350.0

co2_reduced = MAX_CO2 * diet_shift / 100

co2_remaining = MAX_CO2 - co2_reduced

current_ppm = (
    START_PPM
    - (START_PPM - TARGET_PPM)
    * diet_shift / 100
)

ppm_reduced = START_PPM - current_ppm


# =========================
# RESULTS
# =========================
col3, col4 = st.columns(2)

with col3:

    st.markdown(
        '<div class="number-title">'
        'CO₂ RÉDUIT'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="big-number">'
        f'{co2_reduced:.1f} GtCO₂'
        f'</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="small-number">'
        f'{co2_remaining:.1f} GtCO₂ restantes'
        f'</div>',
        unsafe_allow_html=True
    )


with col4:

    st.markdown(
        '<div class="number-title">'
        'CO₂ ATMOSPHÉRIQUE'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="big-number">'
        f'{current_ppm:.1f} ppm'
        f'</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="small-number">'
        f'426 → {current_ppm:.1f} ppm'
        f'</div>',
        unsafe_allow_html=True
    )


# =========================
# CHART DATA
# =========================

x = np.arange(0, 101)

carbon_curve = MAX_CO2 * (1 - x / 100)

ppm_curve = (
    START_PPM
    - (START_PPM - TARGET_PPM)
    * x / 100
)


# =========================
# CHART 1
# =========================

chart1, chart2 = st.columns(2)


with chart1:

    fig1 = go.Figure()

    fig1.add_trace(
        go.Scatter(
            x=x,
            y=carbon_curve,
            mode="lines",
            line=dict(
                color="#123047",
                width=4
            )
        )
    )

    fig1.add_trace(
        go.Scatter(
            x=[diet_shift],
            y=[co2_remaining],
            mode="markers",
            marker=dict(
                size=13,
                color="#2F765D"
            )
        )
    )

    fig1.update_layout(
        title="ÉCART DE CO₂",
        height=330,
        showlegend=False,
        paper_bgcolor="#FAFAF7",
        plot_bgcolor="#FAFAF7",
        xaxis_title="Transition alimentaire (%)",
        yaxis_title="GtCO₂ restantes",
        margin=dict(
            l=20,
            r=20,
            t=55,
            b=30
        )
    )

    st.plotly_chart(
        fig1,
        use_container_width=True,
        config={
            "displayModeBar": False
        }
    )


# =========================
# CHART 2
# =========================

with chart2:

    fig2 = go.Figure()

    fig2.add_trace(
        go.Scatter(
            x=x,
            y=ppm_curve,
            mode="lines",
            line=dict(
                color="#2F765D",
                width=4
            )
        )
    )

    fig2.add_trace(
        go.Scatter(
            x=[diet_shift],
            y=[current_ppm],
            mode="markers",
            marker=dict(
                size=13,
                color="#123047"
            )
        )
    )

    fig2.update_layout(
        title="CO₂ ATMOSPHÉRIQUE",
        height=330,
        showlegend=False,
        paper_bgcolor="#FAFAF7",
        plot_bgcolor="#FAFAF7",
        xaxis_title="Transition alimentaire (%)",
        yaxis_title="ppm",
        margin=dict(
            l=20,
            r=20,
            t=55,
            b=30
        )
    )

    st.plotly_chart(
        fig2,
        use_container_width=True,
        config={
            "displayModeBar": False
        }
    )

# =========================
# KEY IMPACTS
# =========================

st.markdown(
    '<div class="divider"></div>',
    unsafe_allow_html=True
)

impact1, impact2, impact3 = st.columns(3)

with impact1:
    st.markdown(
        '<div class="number-title">TERRES LIBÉRÉES</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div style="font-size:32px; font-weight:700; color:#123047; '
        'margin-top:12px; white-space:nowrap;">37 millions de km²</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="small-number">78 % des terres agricoles mondiales</div>',
        unsafe_allow_html=True
    )

with impact2:
    st.markdown(
        '<div class="number-title">RÉDUCTION DES GES</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div style="font-size:32px; font-weight:700; color:#123047; '
        'margin-top:12px;">166%</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="small-number">des GES mondiaux de 2020</div>',
        unsafe_allow_html=True
    )

with impact3:
    st.markdown(
        '<div class="number-title">RÉDUCTION DES COÛTS ÉCONOMIQUES</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div style="font-size:32px; font-weight:700; color:#123047; '
        'margin-top:12px;">163%</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="small-number">du PIB mondial de 2020</div>',
        unsafe_allow_html=True
    )

# =========================
# SECOND WHY
# =========================

with st.expander(
    "POURQUOI LA TRANSITION ALIMENTAIRE MODIFIE-T-ELLE LE CO₂ ?"
):

    st.markdown(
        '<div style="font-size:22px; font-weight:700; color:#123047; '
        'margin-bottom:15px;">MODÈLE DE DONNÉES</div>',
        unsafe_allow_html=True
    )

    st.image(
        "data model.png",
        caption="Modèle de données de recherche MY NET ZERO",
        use_container_width=True
    )


    st.markdown(
        '<div style="font-size:22px; font-weight:700; color:#123047; '
        'margin-top:35px; margin-bottom:15px;">'
        'STRUCTURE DE LA RECHERCHE'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
**CHAPITRE 3 — DONNÉES ET MÉTHODOLOGIE**  
Cadre de recherche · Données · Variables · Équations · Modèle de restauration de la nature

**CHAPITRE 4 — ÉMISSIONS ET ABSORPTION NATURELLE DU CO₂**  
Validité du modèle · Prévisions · Analyse de sensibilité · Scénarios climatiques

**CHAPITRE 5 — COÛTS EXTERNES DES COMBUSTIBLES FOSSILES ET DE L’ÉLEVAGE**  
Externalités de l’élevage · Énergie · Coûts économiques

**CHAPITRE 6 — RESPONSABILITÉ CO₂ DES COMBUSTIBLES FOSSILES ET DE L’ÉLEVAGE**  
Émissions · Perte d’élimination du CO₂ · Consommation d’énergie · Analyse de sensibilité des terres et des forêts · Responsabilité ajustée

**CHAPITRE 7 — APPLICATION ET MODÈLE DE RESTAURATION DE LA NATURE**  
États-Unis · Chine · Politique climatique mondiale · Restauration de la nature
        """
    )

    st.caption(
        "Detailed methodology, calculations, sensitivity analyses and "
        "underlying data are documented in the full research."
    )



    st.markdown(
        '<div style="font-size:22px; font-weight:700; color:#123047; '
        'margin-top:40px; margin-bottom:15px;">'
        'BASE DE CALCUL'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
**ÉNERGIE — 41 %**

**DONNÉES SOURCES**  
Consommation mondiale de viande par type · Besoins énergétiques par type de viande · Population mondiale · Consommation mondiale d’électricité

**CALCUL MY NET ZERO**  
Consommation de viande × besoin énergétique par type de viande × population mondiale  
→ estimation de la consommation mondiale d’électricité de l’industrie de la viande  
→ comparaison avec la consommation mondiale totale d’électricité

**RÉSULTAT**  
Consommation d’électricité estimée de l’industrie de la viande = **41 % de la consommation mondiale d’électricité**
        """
    )

    st.caption(
        "Derived indicator calculated by the MY NET ZERO research model "
        "from underlying source data."
    )

    st.markdown(
        """
**MÉTHANE — 31 %**

**DONNÉES SOURCES**  
Population bovine · Émissions annuelles de méthane par bovin

**HYPOTHÈSE DU MODÈLE MY NET ZERO**  
Méthane = **100× équivalent CO₂** afin de représenter son fort effet de réchauffement à court terme

**CALCUL MY NET ZERO**  
Population bovine × émissions de méthane par bovin × 100 équivalent CO₂  
→ environ **15,2 GtCO₂-éq.**

**RÉSULTAT**  
15,2 GtCO₂-éq. ÷ 50 GtCO₂-éq. d’émissions mondiales annuelles  
→ **≈ 31 %**
        """
    )

    st.caption(
        "The 100× methane factor is a MY NET ZERO model assumption. "
        "It is not the conventional 100-year GWP factor."
    )
 
    st.markdown(
        """
**TERRES — 11 %**

**DONNÉES SOURCES**  
Utilisation des terres par l’élevage = **37 millions de km²**

**CALCUL MY NET ZERO**  
37 millions de km² × capacité estimée d’absorption du CO₂ des terres libérées  
→ environ **5,17 GtCO₂ par an**

**RÉSULTAT**  
5,17 GtCO₂ ÷ 50 GtCO₂ d’émissions mondiales annuelles  
→ **≈ 11 %**
        """
    )

    st.caption(
        "The 37 millions de km² livestock land-use estimate is source data. "
        "The 11% indicator is derived by the MY NET ZERO research model."
    )

    st.markdown(
        """
**FORÊT — 91 %**

**PÉRIMÈTRE DU MODÈLE**  
Estimation prudente utilisant les bovins des **pays amazoniens et d’un pays du bassin du Congo**, plutôt que la population bovine mondiale

**CALCUL MY NET ZERO**  
Population bovine dans les régions de forêt tropicale sélectionnées × impact sur la superficie forestière × capacité estimée d’absorption du CO₂ des forêts tropicales  
→ environ **45,34 GtCO₂ par an**

**RÉSULTAT**  
45,34 GtCO₂ ÷ 50 GtCO₂ d’émissions mondiales annuelles  
→ **≈ 91 %**
        """
    )

    st.caption(
        "The forest estimate uses a deliberately restricted tropical-forest "
        "boundary to avoid applying one CO₂ absorption rate to forests "
        "across different climatic regions."
    )

    st.markdown(
        """
**RESPONSABILITÉ CO₂ TOTALE DE L’ÉLEVAGE — 166 %**

**RÉALLOCATION DE L’ÉNERGIE**  
Consommation énergétique de l’industrie de la viande = **41 %** de l’électricité mondiale  
Appliquée à la **base de référence de 78 % pour les combustibles fossiles**  
→ 78 % × 41 % ≈ **32 %**

**CALCUL INTÉGRÉ MY NET ZERO**  
Méthane **31 %** + Terres **11 %** + Forêt **91 %** + Énergie **32 %**

**RÉSULTAT**  
31 % + 11 % + 91 % + 32 % ≈ **166 %**
        """
    )

    st.caption(
        "The 166% result is an integrated MY NET ZERO research-model "
        "estimate relative to the 50 GtCO₂-eq. annual global emissions baseline."
    )


    st.markdown(
        '<div style="font-size:22px; font-weight:700; color:#123047; '
        'margin-top:40px; margin-bottom:15px;">'
        'SOURCES'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
**PRINCIPALES SOURCES DE DONNÉES**

**FAO / UNFAO**  
Données sur l’élevage, la consommation alimentaire et l’utilisation des terres agricoles

**Energypedia**  
Besoins énergétiques dans les chaînes de valeur alimentaires et agricoles

**U.S. Energy Information Administration (EIA)**  
Données mondiales sur l’énergie et l’électricité

**IPCC**  
Cadre conventionnel de comptabilisation des gaz à effet de serre et d’évaluation du climat
        """
    )

    st.caption(
        "Source data are used as inputs. Calculations, integration and "
        "derived indicators are produced by the MY NET ZERO research model."
    )
    st.markdown(
        """
**CONSULTER LES SOURCES ORIGINALES**

[FAO / FAOSTAT — Données mondiales sur l’alimentation et l’agriculture](https://www.fao.org/faostat/)

[Energypedia — Énergie dans les chaînes de valeur alimentaires et agricoles](https://energypedia.info/wiki/Energy_within_Food_and_Agricultural_Value_Chains)

[U.S. Energy Information Administration (EIA) — Données sur l’électricité](https://www.eia.gov/electricity/data.php)

[Gatti et al. (2021), Nature — L’Amazonie comme source de carbone liée à la déforestation et au changement climatique](https://www.nature.com/articles/s41586-021-03629-6)
        """
    )
