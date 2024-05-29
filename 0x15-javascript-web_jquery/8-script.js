const api = "https://swapi-api.alx-tools.com/api/films/?format=json";

$.ajax({
    url: api,
    method: 'GET',
    dataType: 'json',
    success: function (data)
    {
        console.log(data.results)
        data.results.forEach(mov =>
        {
            $('UL#list_movies').append(`<li>${mov.title}</li>`);
        });
    },
    error: function (error)
    {
        console.log(error);
    }
});
