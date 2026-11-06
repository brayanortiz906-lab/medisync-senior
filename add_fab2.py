PAGES = ['index.html','landing_medisync_senior.html','tutorial_medisync.html','prototipo_simple.html','ensayo_medisync_senior.html']

def fab(sections=False):
    sec = ''
    if sections:
        sec = '''
    <div style="border-top:1px solid rgba(255,255,255,0.1);margin-top:8px;padding-top:8px;">
      <p style="color:#94a3b8;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:0.1em;margin:0 0 6px 4px;">Secciones</p>
      <a href="#problema" style="display:block;padding:6px 12px;color:#cbd5e1;text-decoration:none;border-radius:8px;font-size:13px;" onmouseover="this.style.background='rgba(255,255,255,0.1)'" onmouseout="this.style.background='transparent'">⚠️ Problema</a>
      <a href="#solucion" style="display:block;padding:6px 12px;color:#cbd5e1;text-decoration:none;border-radius:8px;font-size:13px;" onmouseover="this.style.background='rgba(255,255,255,0.1)'" onmouseout="this.style.background='transparent'">💡 Solución</a>
      <a href="#demostracion" style="display:block;padding:6px 12px;color:#cbd5e1;text-decoration:none;border-radius:8px;font-size:13px;" onmouseover="this.style.background='rgba(255,255,255,0.1)'" onmouseout="this.style.background='transparent'">📱 Demo</a>
      <a href="#pitch" style="display:block;padding:6px 12px;color:#cbd5e1;text-decoration:none;border-radius:8px;font-size:13px;" onmouseover="this.style.background='rgba(255,255,255,0.1)'" onmouseout="this.style.background='transparent'">🎥 Pitch</a>
      <a href="#ensayo" style="display:block;padding:6px 12px;color:#cbd5e1;text-decoration:none;border-radius:8px;font-size:13px;" onmouseover="this.style.background='rgba(255,255,255,0.1)'" onmouseout="this.style.background='transparent'">📝 Ensayo</a>
      <a href="#equipo" style="display:block;padding:6px 12px;color:#cbd5e1;text-decoration:none;border-radius:8px;font-size:13px;" onmouseover="this.style.background='rgba(255,255,255,0.1)'" onmouseout="this.style.background='transparent'">👥 Equipo</a>
    </div>'''
    return '''<!-- QUICK NAV FAB -->
<div id="qnFab" style="position:fixed;bottom:24px;right:24px;z-index:9999;font-family:system-ui,sans-serif;">
  <button onclick="document.getElementById('qnPanel').classList.toggle('hidden')" style="width:52px;height:52px;border-radius:50%;background:linear-gradient(135deg,#2563eb,#10b981);color:#fff;border:none;box-shadow:0 8px 24px rgba(0,0,0,0.4);cursor:pointer;font-size:20px;display:flex;align-items:center;justify-content:center;">
    <i class="fa-solid fa-compass"></i>
  </button>
  <div id="qnPanel" class="hidden" style="position:absolute;bottom:64px;right:0;background:rgba(15,23,42,0.97);backdrop-filter:blur(12px);border:1px solid rgba(255,255,255,0.15);border-radius:16px;padding:12px;min-width:220px;box-shadow:0 12px 32px rgba(0,0,0,0.5);">
    <p style="color:#94a3b8;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:0.1em;margin:0 0 8px 4px;">Navegación rápida</p>
    <a href="index.html" style="display:block;padding:8px 12px;color:#e2e8f0;text-decoration:none;border-radius:8px;font-size:14px;" onmouseover="this.style.background='rgba(255,255,255,0.1)'" onmouseout="this.style.background='transparent'">🏠 Inicio</a>
    <a href="landing_medisync_senior.html" style="display:block;padding:8px 12px;color:#e2e8f0;text-decoration:none;border-radius:8px;font-size:14px;" onmouseover="this.style.background='rgba(255,255,255,0.1)'" onmouseout="this.style.background='transparent'">📄 Landing</a>
    <a href="tutorial_medisync.html" style="display:block;padding:8px 12px;color:#e2e8f0;text-decoration:none;border-radius:8px;font-size:14px;" onmouseover="this.style.background='rgba(255,255,255,0.1)'" onmouseout="this.style.background='transparent'">📖 Tutorial</a>
    <a href="prototipo_simple.html" style="display:block;padding:8px 12px;color:#e2e8f0;text-decoration:none;border-radius:8px;font-size:14px;" onmouseover="this.style.background='rgba(255,255,255,0.1)'" onmouseout="this.style.background='transparent'">📱 Prototipo</a>
    <a href="ensayo_medisync_senior.html" style="display:block;padding:8px 12px;color:#e2e8f0;text-decoration:none;border-radius:8px;font-size:14px;" onmouseover="this.style.background='rgba(255,255,255,0.1)'" onmouseout="this.style.background='transparent'">📝 Ensayo</a>
    ''' + sec + '''
  </div>
</div>
'''

for f in PAGES:
    s = open(f, encoding='utf-8').read()
    if 'qnFab' in s:
        print(f, 'already has FAB, skip')
        continue
    if '</body>' not in s:
        print(f, 'no body close')
        continue
    fab_html = fab(sections=(f=='landing_medisync_senior.html'))
    s = s.replace('</body>', fab_html + '\n</body>', 1)
    open(f, 'w', encoding='utf-8').write(s)
    print(f, 'updated')
print('done')
'''

# Add padding-top to body CSS block
for f in PAGES:
    s = open(f, encoding='utf-8').read()
    if 'padding-top:60px' not in s:
        s = s.replace('body{padding-bottom:90px;}', 'body{padding-top:60px;padding-bottom:90px;}', 1)
        # also handle ensayo inline style case
        open(f, 'w', encoding='utf-8').write(s)
    print(f, 'padding updated')
print('done')
