-- ==========================================
-- BANCO DE DADOS - SOUL HUNTER
-- PostgreSQL / Neon (schema de referência)
-- O schema final é gerado pelos models em models/models.py
-- ==========================================

-- ==========================================
-- USUARIO
-- ==========================================
CREATE TABLE usuario (
    id_usuario    BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nome          VARCHAR(100)  NOT NULL,
    email         VARCHAR(150)  NOT NULL UNIQUE,
    senha_hash    VARCHAR(255)  NOT NULL,
    pontos        INTEGER       NOT NULL DEFAULT 0 CHECK (pontos >= 0),
    nivel         INTEGER       NOT NULL DEFAULT 1 CHECK (nivel >= 1),
    data_cadastro TIMESTAMP     NOT NULL DEFAULT CURRENT_TIMESTAMP,
    ativo         BOOLEAN       NOT NULL DEFAULT TRUE
);

-- ==========================================
-- EVENTO
-- ==========================================
CREATE TABLE evento (
    id_evento   BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nome        VARCHAR(150) NOT NULL,
    descricao   VARCHAR(500),
    parceiro    VARCHAR(150),
    imagem_url  VARCHAR(500),
    data_inicio TIMESTAMP    NOT NULL,
    data_fim    TIMESTAMP    NOT NULL,
    ativo       BOOLEAN      NOT NULL DEFAULT TRUE,
    CONSTRAINT chk_datas_evento CHECK (data_fim > data_inicio)
);

-- ==========================================
-- LOTE_GERACAO
-- ==========================================
CREATE TABLE lote_geracao (
    id_lote           BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    id_evento         BIGINT,
    nome              VARCHAR(150) NOT NULL,
    quantidade_maxima INTEGER      NOT NULL CHECK (quantidade_maxima > 0),
    quantidade_gerada INTEGER      NOT NULL DEFAULT 0 CHECK (quantidade_gerada >= 0),
    raridade          VARCHAR(20),
    ativo             BOOLEAN      NOT NULL DEFAULT TRUE,
    data_criacao      TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_lote_evento
        FOREIGN KEY (id_evento) REFERENCES evento (id_evento),
    CONSTRAINT chk_lote_quantidade
        CHECK (quantidade_gerada <= quantidade_maxima)
);

-- ==========================================
-- FANTASMA
-- ==========================================
CREATE TABLE fantasma (
    id_fantasma   BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    id_lote       BIGINT,
    seed          BIGINT      NOT NULL,
    raridade      VARCHAR(20) NOT NULL,
    corpo         VARCHAR(50) NOT NULL,
    olho          VARCHAR(50) NOT NULL,
    boca          VARCHAR(50) NOT NULL,
    acessorios    JSONB,
    aura          VARCHAR(50),
    efeito        VARCHAR(50),
    imagem_url    VARCHAR(500),
    data_geracao  TIMESTAMP   NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_fantasma_lote
        FOREIGN KEY (id_lote) REFERENCES lote_geracao (id_lote)
);

-- ==========================================
-- PONTO_SPAWN
-- ==========================================
CREATE TABLE ponto_spawn (
    id_spawn       BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    id_lote        BIGINT       NOT NULL,
    latitude       DECIMAL(10,7) NOT NULL,
    longitude      DECIMAL(10,7) NOT NULL,
    raio_captura   DECIMAL(6,2)  NOT NULL CHECK (raio_captura > 0),
    ativo          BOOLEAN       NOT NULL DEFAULT TRUE,
    data_criacao   TIMESTAMP     NOT NULL DEFAULT CURRENT_TIMESTAMP,
    data_expiracao TIMESTAMP,
    CONSTRAINT fk_spawn_lote
        FOREIGN KEY (id_lote) REFERENCES lote_geracao (id_lote)
);

-- ==========================================
-- CAPTURA
-- ==========================================
CREATE TABLE captura (
    id_captura        BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    id_usuario        BIGINT       NOT NULL,
    id_fantasma       BIGINT       NOT NULL,
    id_spawn          BIGINT       NOT NULL,
    latitude_usuario  DECIMAL(10,7) NOT NULL,
    longitude_usuario DECIMAL(10,7) NOT NULL,
    distancia_metros  DECIMAL(10,2) NOT NULL CHECK (distancia_metros >= 0),
    data_captura      TIMESTAMP     NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_captura_usuario FOREIGN KEY (id_usuario) REFERENCES usuario (id_usuario),
    CONSTRAINT fk_captura_fantasma FOREIGN KEY (id_fantasma) REFERENCES fantasma (id_fantasma),
    CONSTRAINT fk_captura_spawn FOREIGN KEY (id_spawn) REFERENCES ponto_spawn (id_spawn)
);

-- ==========================================
-- COLECAO
-- ==========================================
CREATE TABLE colecao (
    id_usuario           BIGINT    NOT NULL,
    id_fantasma          BIGINT    NOT NULL,
    quantidade           INTEGER   NOT NULL DEFAULT 1 CHECK (quantidade > 0),
    data_primeira_captura TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    data_ultima_captura   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id_usuario, id_fantasma),
    CONSTRAINT fk_colecao_usuario FOREIGN KEY (id_usuario) REFERENCES usuario (id_usuario),
    CONSTRAINT fk_colecao_fantasma FOREIGN KEY (id_fantasma) REFERENCES fantasma (id_fantasma)
);