PAGES = ['index.html','landing_medisync_senior.html','tutorial_medisync.html','prototipo_simple.html','ensayo_medisync_senior.html']

for f in PAGES:
    s = open(f, encoding='utf-8').read()
    # remove FAB block
    import re
    s = re.sub(r'<!-- QUICK NAV FAB -->.*?</div>\s*\n</div>\s*\n', '', s, count=1, flags=re.DOTALL)
    # Also try simpler removal
    if 'qnFab' in s:
        # remove from <!-- QUICK NAV FAB --> to the matching closing before </body>
        idx = s.find('<!-- QUICK NAV FAB -->')
        if idx != -1:
            end = s.find('</body>', idx)
            if end != -1:
                s = s[:idx] + s[end:]
    open(f, 'w', encoding='utf-8').write(s)
    print(f, 'FAB removed' if 'qnFab' not in s else 'FAB STILL PRESENT')
print('done')
