CREATE SCHEMA IF NOT EXISTS predictions
    AUTHORIZATION postgres;

COMMENT ON SCHEMA predictions
    IS 'Stores information about requests';
    
CREATE TABLE IF NOT EXISTS predictions.history
(
    order_id bigint NOT NULL DEFAULT 0,
    store_id bigint NOT NULL DEFAULT 0,
    to_user_distance double precision NOT NULL DEFAULT 0,
    to_user_elevation double precision NOT NULL DEFAULT 0,
    total_earning double precision NOT NULL DEFAULT 0,
    created_at timestamp with time zone,
    taken integer,
    CONSTRAINT history_pkey PRIMARY KEY (order_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS predictions.history
    OWNER to postgres;
