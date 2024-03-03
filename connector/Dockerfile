FROM mageai/mageai:0.9.65

ARG PROJECT_DIR=.
ARG MAGE_CODE_PATH=/home/src
ARG USER_CODE_PATH=${MAGE_CODE_PATH}/${PROJECT_DIR}

ENV USER_CODE_PATH=${USER_CODE_PATH} \
    PYTHONPATH="${PYTHONPATH}:${MAGE_CODE_PATH}"

WORKDIR ${MAGE_CODE_PATH}

COPY ${PROJECT_DIR} ${USER_CODE_PATH}

RUN pip install --upgrade pip && \
    pip install -r ${USER_CODE_PATH}/requirements.txt && \
    python3 /app/install_other_dependencies.py --path ${USER_CODE_PATH} && \
    rm -rf /root/.cache

RUN addgroup --system nonroot && \
    adduser --system --ingroup nonroot nonroot && \
    chown -R nonroot:nonroot ${MAGE_CODE_PATH} && \
    chmod -R 775 ${MAGE_CODE_PATH}

USER nonroot
ENV PYTHONPATH="${PYTHONPATH}:/home/src"

CMD ["/bin/sh", "-c", "/app/run_app.sh"]
