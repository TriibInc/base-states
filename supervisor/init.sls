include:
  - python

supervisor:
  pip.installed:
    - name: supervisor
    - require:
      - pkg: python-pkgs
      - file: /etc/supervisord.conf


/etc/supervisord.conf:
  file.managed:
    - source: salt://supervisor/supervisord.conf
    - user: root
    - group: root
    - mode: 644

/etc/init.d/supervisord:
  file.managed:
    - source: salt://supervisor/supervisord.sh
    - makedirs: True
    - mode: 755
  cmd.run:
    - name: sudo service supervisord restart
    - require:
      - pip.installed: supervisor
      - file: /etc/init.d/supervisord

