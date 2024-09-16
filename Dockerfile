FROM registry1.dso.mil/ironbank/redhat/python/python39:3.9
USER root

RUN yum update -y && yum install -y libxml2-devel xmlsec1 xmlsec1-openssl openssl libtool-ltdl pkg-config 
# Copy/extract openlxp-ecc-xis source code
RUN mkdir -p /tmp/openlxp-xis

WORKDIR /tmp/openlxp-xis/

COPY openlxp-xis-1.0.3.tar.gz .

RUN tar -xvf ./openlxp-xis-1.0.3.tar.gz --strip-components=1
RUN    cp ./requirements.txt ./start-app.sh ./start-server.sh /tmp/
RUN    rm openlxp-xis-1.0.3.tar.gz 
# Requirements for xis   
RUN  if [ ! -f /tmp/debug.log ]; then touch /tmp/debug.log ; fi && \
    chmod a=rwx /tmp/debug.log && \
    chmod +x /tmp/start-server.sh && \
    chmod +x /tmp/start-app.sh && \
    pip install --upgrade pip && \
    pip install -r requirements.txt && \
    chmod -s /usr/bin/write && \
    chmod -s /var/lib/tpm2-tss/system/keystore

RUN chown -R 1001:1001 /tmp//tmp/openlxp-xis/
WORKDIR /tmp/openlxp-xis/
RUN yum clean all

# remove unnecessary test files
RUN rm -rf /opt/app-root/lib/python3.9/site-packages/social_core/tests/backends/test_apple.py && \
    rm -rf /opt/app-root/lib/python3.9/site-packages/tornado/test/test.key && \
    rm -rf /opt/app-root/lib/python3.9/site-packages/social_core/tests/backends/__pycache__/test_keycloak.cpython-39.pyc && \
    rm -rf /opt/app-root/lib/python3.9/site-packages/social_core/tests/backends/__pycache__/test_apple.cpython-39.pyc && \
    rm -rf /opt/app-root/lib/python3.9/site-packages/social_core/tests/testkey.pem && \
    rm -rf /opt/app-root/lib/python3.9/site-packages/social_core/tests/backends/test_keycloak.py


USER 1001

# start server
EXPOSE 8020
STOPSIGNAL SIGTERM


