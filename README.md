# MediSync Senior

> **Adherencia médica para adultos mayores** — App accesible con doble vista (Mamá y Cuidador) que muestra la foto real de la caja, habla en voz alta y sincroniza las tomas en tiempo real.

**Proyecto universitario** — Institución Universitaria Pascual Bravo · TICs y Competencias Digitales 2026

---

## 🌐 Demo en vivo (GitHub Pages)

| Página | Enlace |
|---|---|
| **Landing Page** | [Abrir](https://brayanortiz906-lab.github.io/medisync-senior/landing_medisync_senior.html) |
| **Prototipo completo** | [Abrir](https://brayanortiz906-lab.github.io/medisync-senior/interfaz_medisync_senior.html) |
| **Prototipo demo (ambas vistas)** | [Abrir](https://brayanortiz906-lab.github.io/medisync-senior/prototipo_demo.html) |
| **Prototipo de prueba** | [Abrir](https://brayanortiz906-lab.github.io/medisync-senior/prototipo_prueba.html) |
| **Ensayo APA 7** | [Abrir](https://brayanortiz906-lab.github.io/medisync-senior/ensayo_medisync_senior.html) |

---

## 📋 El Problema

> *"María y los adultos mayores tienen problemas para tomar la medicina correcta porque las cajas son idénticas y sufren olvidos, y eso le cuesta complicaciones de salud y 5+ horas a su cuidador."*

### Costo real
- **5 horas perdidas a la semana** por el cuidador.
- **Riesgo de urgencias** por dosis dobles o descompensación.
- **Cajas e instrucciones enanas e ilegibles** para el adulto mayor.

---

## 💡 La Solución

MediSync Senior es una app web accesible con **doble vista** (Mamá y Cuidador) que:

1. **Muestra la foto real de la caja** en tamaño gigante.
2. **Habla en voz alta** las instrucciones.
3. **Sincroniza las tomas en tiempo real** entre ambos dispositivos.

### Cómo funciona (3 pasos)
1. **Santiago escanea** la caja y la pastilla con IA.
2. **La app proyecta** en la pantalla de Mamá la foto gigante y le habla en voz alta.
3. **Mamá oprime un solo botón verde** y Santiago recibe la confirmación en tiempo real.

---

## 🏗️ Estructura del Proyecto

```
medisync-senior/
├── index.html                          # Portal de entrada (redirige a landing)
├── landing_medisync_senior.html        # Landing page completa
├── interfaz_medisync_senior.html       # Prototipo funcional (Firebase + modo local)
├── prototipo_demo.html                 # Demo: ambas vistas lado a lado (sin código)
├── prototipo_prueba.html               # Prototipo de prueba (con código de vinculación)
├── ensayo_medisync_senior.html         # Ensayo académico APA 7
├── MediSync_Senior_Ensayo_APA7.docx    # Ensayo en Word (APA 7)
├── FIREBASE_SETUP.md                   # Guía de configuración de Firebase
├── README.md                           # Este archivo
├── capacitor.config.json                # Configuración Capacitor (Android)
├── package.json                        # Dependencias Node
└── android/                            # Proyecto Android (Capacitor)
```

---

## 🚀 Cómo ejecutar (100% estático — sin Docker, sin build)

### Opción 1: GitHub Pages (recomendado)
Ya está desplegado en: https://brayanortiz906-lab.github.io/medisync-senior/

### Opción 2: Abrir directamente
1. Descarga o clona el repositorio.
2. Abre `index.html` o `landing_medisync_senior.html` en tu navegador.
3. ¡Listo! No requiere instalación ni servidor.

### Opción 3: Servidor local (opcional)
```bash
# Python
python -m http.server 8000

# Node.js
npx serve .
```

---

## 🔥 Sincronización en la nube (Firebase)

El prototipo funciona en **modo local** por defecto (BroadcastChannel + localStorage, solo mismo navegador).

Para sincronizar entre dispositivos distantes (celular de María y celular de Santiago):

1. Crea un proyecto en [Firebase Console](https://console.firebase.google.com).
2. Activa **Realtime Database** (modo de prueba).
3. Copia el `firebaseConfig` de tu proyecto.
4. En `interfaz_medisync_senior.html`, busca `FIREBASE_CONFIG` y reemplaza los valores `REEMPLAZA...`.
5. Guarda y recarga. El badge superior cambiará de "local" (gris) a "nube" (verde).

Guía completa: [FIREBASE_SETUP.md](FIREBASE_SETUP.md)

---

## 👥 Equipo de Trabajo

| Integrante | Rol Principal | Avatar |
|---|---|---|
| **Santiago** | Líder de Pitch y Video | SL |
| **Gustavo** | Parte del equipo | GA |
| **Brayan** | Líder de Prototipo y Desarrollo Web | BA |

---

## 🎤 Video Pitch (Shark Tank)

- **Pedido:** $15.000.000 COP por el 12% de participación.
- **Duración:** 4 minutos.
- Para incrustar el video, reemplaza `VIDEO_ID_AQUI` en `landing_medisync_senior.html` (línea ~447) con el ID real de YouTube.

---

## 📄 Ensayo Académico

- Formato: APA 7.
- Disponible en: `ensayo_medisync_senior.html` (visualización web) y `MediSync_Senior_Ensayo.docx` (descarga).
- Incluye: planteamiento del problema, marco teórico, metodología, resultados y conclusiones.

---

## 🛠️ Tecnologías

- **HTML5** + **Tailwind CSS** (CDN) + **FontAwesome** (CDN)
- **JavaScript** vanilla (sin frameworks)
- **Firebase Realtime Database** (opcional, para sincronización en la nube)
- **Capacitor** (para generar APK Android)
- **GitHub Pages** (hosting estático)

---

## 📱 APK Android

Se generó un APK universal (`MediSync_Senior.apk`) a partir del prototipo usando Capacitor. Para regenerarlo:

```bash
npm install
npx cap sync android
cd android && ./gradlew assembleDebug
```

---

## 📝 Licencia

Proyecto académico — Institución Universitaria Pascual Bravo, 2026.