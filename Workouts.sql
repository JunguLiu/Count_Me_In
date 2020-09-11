BEGIN;

SET client_encoding = 'LATIN1';

COPY Workouts (id, name, calories, category, location, image) FROM stdin;
1 boxing  200 with-equipment  indoor-possible https://github.com/sanasdh/Count_Me_In/blob/master/main_app/static/img/workout-boxing.jpg?raw=true
2	biking  150 with-equipment   outdoor-possible https://github.com/sanasdh/Count_Me_In/blob/master/main_app/static/img/workout-biking.jpg?raw=true
3	Rope-Skipping	100	with-equipment   indoor-possible    https://github.com/sanasdh/Count_Me_In/blob/master/main_app/static/img/workout-ropeSkipping.jpg?raw=true 
4	Running	100	without-equipment   outdoor-possible    https://github.com/sanasdh/Count_Me_In/blob/master/main_app/static/img/workout-running.jpg?raw=true 
5	Sit-Up	30	without-equipment   indoor-possible https://github.com/sanasdh/Count_Me_In/blob/master/main_app/static/img/workout-situp.jpg?raw=true
6	Squat	30	without-equipment   indoor-possible https://github.com/sanasdh/Count_Me_In/blob/master/main_app/static/img/workout-squat.jpg?raw=true
7	Swimming    200 with-equipment   indoor-possible    https://github.com/sanasdh/Count_Me_In/blob/master/main_app/static/img/workout-swimming.jpg?raw=true
8	Yoga	70	without-equipment   indoor-possible https://github.com/sanasdh/Count_Me_In/blob/master/main_app/static/img/workout-yoga.jpg?raw=true
9	Push-Up	40	without-equipment   indoor-possible https://github.com/sanasdh/Count_Me_In/blob/master/main_app/static/img/workout-pushUps.jpg?raw=true


COMMIT;

ANALYZE Workouts;
