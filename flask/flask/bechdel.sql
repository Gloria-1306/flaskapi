select * from movies
where originalTitle like "%Wall%";

select originalTitle, rating 
from movies
inner join bechdel
using (movieId)
where movieId like "910970"; 

-- les acteurs qui ont joués ds le + de genre

select personId,movieId, genre, (count distinct genre  from people
inner join moviespeople
on (personId.moviespeople)
inner join moviesgenres
on (movieId)