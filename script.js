var client_id = '07c70ef841674ff4aebc0dbcbcfe42fe';
var client_secret = 'c599ef8cb7e144dea3192a600a8b90a9'

var authOptions = {
    url: 'https://accounts.spotify.com/api/token',
    headers: {
        'Authorization' : 'Basic ' + (new Buffer.from(client_id + ':' + client_secret).toString('base64'))
    },
    form: {
        grant_type: 'client_crediental'
    },
    json: true
};

request.post(authOptions, function(error, response, body){
    if (!error && response.statusCode === 200) {
        var token = body.access_token;
       // console.log(token);
    }
});


