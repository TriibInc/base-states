mod_wsgi:
  pkg:
    - installed
    - name: libapache2-mod-wsgi

remove_existing_conf:
  file.absent:
      - name: /etc/apache2/sites-enabled/000-default

/etc/apache2/mods-enabled/ssl.load:
  file.symlink:
    - target: /etc/apache2/mods-available/ssl.load
    - require:
      - pkg: httpd

/etc/apache2/mods-enabled/rewrite.load:
  file.symlink:
    - target: /etc/apache2/mods-available/rewrite.load
    - require:
      - pkg: httpd

httpd:
  pkg:
    - installed
    - name: apache2
  service:
    - running
    - name: apache2
    - enable: True
    - require:
      - pkg: mod_wsgi
