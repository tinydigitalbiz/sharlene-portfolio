f=open('index.html','r')
c=f.read()
f.close()
hero_start = c.find('<section id="hero">')
about_start = c.find('<section id="about">')
new_hero = '<section id="hero">\n  <div class="hero-grid-bg"></div>\n  <div class="hero-glow"></div>\n  <div class="hero-glow2"></div>\n  <div id="hero-left">\n    <h1 class="hero-name">Sharlene<br><em>Javier.</em></h1>\n    <p class="hero-eyebrow">Digital Transformation · Program Management · AI Automation · Process Design</p>\n    <div class="stats-strip">\n      <div class="stat-item"><span class="stat-number">10+</span><span class="stat-label">Years of Enterprise Experience</span></div>\n      <div class="stat-item"><span class="stat-number">15+</span><span class="stat-label">Complex Programs Delivered</span></div>\n      <div class="stat-item"><span class="stat-number">$10M+</span><span class="stat-label">Revenue Growth Generated</span></div>\n      <div class="stat-item"><span class="stat-number">98%</span><span class="stat-label">Onme Deployment Rate</span></div>\n      <div class="stat-item"><span class="stat-number">8</span><span class="stat-label">Industries Transformed</span></div>\n    </div>\n    <div class="hero-ctas">\n      <a href="#projects" class="btn-primary">View My Work</a>\n      <a href="#contact" class="btn-ghost">Lets Talk</a>\n    </div>\n  </div>\n  <div id="hero-photo-wrap">\n    <img class="hero-photo" src="assets/images/profile.png" alt="Sharlene Javier"/>\n  </div>\n</section>\n\n'
c = c[:hero_start] + new_hero + c[about_start:]
f=open('index.html','w')
f.write(c)
f.close()
print('Done!')
