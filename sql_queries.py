# DROP TABLES

songplay_table_drop = "drop table if exists songplays;"
user_table_drop = "drop table if exists users;"
song_table_drop = "drop table if exists songs;"
artist_table_drop = "drop table if exists artists;"
time_table_drop = "drop table if exists time;"

# CREATE TABLES

# song_id and artist_id are exempt of the not null constraint as mentioned in the FAQs page.

songplay_table_create = ("""
    create table if not exists songplays (
        songplay_id serial,
        start_time timestamp not null,
        user_id int not null,
        level varchar,
        song_id varchar,
        artist_id varchar,
        session_id int,
        location varchar,
        user_agent varchar,
        primary key (songplay_id)
    );
""")

user_table_create = ("""
    create table if not exists users (
        user_id int,
        first_name varchar,
        last_name varchar,
        gender char(1),
        level varchar,
        primary key (user_id)
    );
""")

song_table_create = ("""
    create table if not exists songs (
        song_id varchar,
        title varchar not null,
        artist_id varchar,
        year int,
        duration float not null,
        primary key (song_id)
    );
""")

artist_table_create = ("""
    create table if not exists artists (
        artist_id varchar,
        name varchar not null,
        location varchar,
        latitude float,
        longitude float,
        primary key (artist_id)
    );
""")

time_table_create = ("""
    create table if not exists time (
        start_time timestamp,
        hour int,
        day int,
        week int,
        month int,
        year int,
        weekday int,
        primary key (start_time)
    );
""")

# INSERT RECORDS

songplay_table_insert = ("""
    insert into songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) 
    values (to_timestamp(%s /1000), %s, %s, %s, %s, %s, %s, %s)
    on conflict do nothing;
""")

user_table_insert = ("""
    insert into users (user_id, first_name, last_name, gender, level) 
    values (%s, %s, %s, %s, %s)
    on conflict do nothing;
""")

song_table_insert = ("""
    insert into songs (song_id, title, artist_id, year, duration) 
    values (%s, %s, %s, %s, %s)
    on conflict do nothing;
""")

artist_table_insert = ("""
    insert into artists (artist_id, name, location, latitude, longitude) 
    values (%s, %s, %s, %s, %s)
    on conflict do nothing;
""")


time_table_insert = ("""
    insert into time (start_time, hour, day, week, month, year, weekday) 
    values (to_timestamp(%s /1000), %s, %s, %s, %s, %s, %s)
    on conflict do nothing;
""")

# FIND SONGS
song_select = ("""
    select so.song_id, ar.artist_id from
    songs so inner join
    artists ar on so.artist_id = ar.artist_id
    where title = %s
        and name = %s
        and duration = %s
""")




# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]