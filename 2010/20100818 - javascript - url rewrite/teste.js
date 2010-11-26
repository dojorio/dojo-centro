$(document).ready(function(){

    describe('URL Rewrite',{

        '/article/52 deve retornar /article?id=52': function() {
            var url = rewrite('/article/52')
            value_of(url).should_be('/article?id=52')
        },

        '/article/54 deve retornar /article?id=54': function() {
            var url = rewrite('/article/54')
            value_of(url).should_be('/article?id=54')
        },

        '/article/5 deve retornar /article?id=5': function() {
            var url = rewrite('/article/5')
            value_of(url).should_be('/article?id=5')
        },

        '/article/1234567 deve retornar /article?id=1234567': function()        {
            var url = rewrite('/article/1234567')
            value_of(url).should_be('/article?id=1234567')
        },

        '/guide/1/2008/2 deve retornar /guide/1/2009/2': function() {
            var url = rewrite('/guide/1/2008/2')
            value_of(url).should_be('/guide/1/2009/2')
        },
        '/guide/512/2008/ deve retornar /guide/512/2009/': function() {
            var url = rewrite('/guide/512/2008/')
            value_of(url).should_be('/guide/512/2009/')
        },
        '/company/brasil/rio deve retornar /company?country=brasil&city=rio': function() {
            var url = rewrite('/company/brasil/rio')
            value_of(url).should_be('/company?country=brasil&city=rio')
        },


    })


});

