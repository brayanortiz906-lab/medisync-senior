# MediSync Senior - Sincronización en la nube (Firebase)

La app funciona en modo **local** por defecto (BroadcastChannel + localStorage, solo mismo dispositivo/navegador).
Para sincronizar entre dispositivos distantes (Madre en su celular y Santiago en el suyo), configura Firebase Realtime Database.

## Pasos (5 minutos)

1. Ve a https://console.firebase.google.com y crea un proyecto (ej: `medisync-senior`).
2. En el menú izquierdo: **Build → Realtime Database → Create Database**. Elige la región más cercana. Modo de prueba (test mode) por 30 días está bien para el prototipo.
3. En **Reglas (Rules)**, asegúrate de que permitan lectura/escritura:
   ```json
   {
     "rules": {
       ".read": true,
       ".write": true
     }
   }
   ```
   (Solo para prototipo académico. En producción restringe por autenticación.)
4. En **Configuración del proyecto (ícono de engranaje) → Tus apps → Web (</>)**, registra una app web. Copia el objeto `firebaseConfig`.
5. Abre `interfaz_medisync_senior.html` y busca el bloque `FIREBASE_CONFIG`. Reemplaza los valores `REEMPLAZA...` con los de tu proyecto:
   ```js
   const FIREBASE_CONFIG = {
       apiKey: "AIza...",
       authDomain: "medisync-senior.firebaseapp.com",
       databaseURL: "https://medisync-senior-default-rtdb.firebaseio.com",
       projectId: "medisync-senior",
       storageBucket: "medisync-senior.appspot.com",
       messagingSenderId: "123456789",
       appId: "1:123456789:web:abc..."
   };
   ```
6. Guarda y recarga. El badge superior cambiará de "local" a "nube" (verde).

## Cómo se sincroniza

- **Cuidador (Santiago)** selecciona su rol → se genera un código de 6 dígitos y se guarda en `/links/{codigo}` en Firebase.
- **Madre (María)** selecciona su rol → ingresa el código → la app verifica en Firebase y vincula.
- Cuando María toma una dosis → se publica en `/links/{codigo}/lastDose` → Santiago recibe la confirmación en tiempo real (incluso en otro dispositivo/país).

## Fallback

Si Firebase no está configurado o falla, la app sigue funcionando con BroadcastChannel + localStorage (solo mismo navegador/dispositivo). No se rompe nada.