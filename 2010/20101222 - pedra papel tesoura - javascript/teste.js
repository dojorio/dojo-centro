$(document).ready(function(){
				describe('quando valor é papel', {
						'deve empatar com papel': function() {
								var resultado = jokenpo('papel', 'papel');
								value_of(resultado).should_be('empate');
								},

						'deve vencer pedra': function() {
								var resultado = jokenpo('papel', 'pedra');
								value_of(resultado).should_be('papel');
								},

						'deve perder para tesoura': function() {
								var resultado = jokenpo('papel', 'tesoura');
								value_of(resultado).should_be('tesoura');
								},
						});


				describe('quando valor é pedra', {
								'deve empatar com pedra': function() {
										var resultado = jokenpo('pedra', 'pedra');
										value_of(resultado).should_be('empate');
										},

								'deve vencer tesoura': function() {
										var resultado = jokenpo('pedra', 'tesoura');
										value_of(resultado).should_be('pedra');
										},

								'deve perder para papel': function() {
										var resultado = jokenpo('pedra', 'papel');
										value_of(resultado).should_be('papel');
										},
								});


				describe('quando valor é tesoura', {
								'deve empatar com tesoura': function() {
										var resultado = jokenpo('tesoura', 'tesoura');
										value_of(resultado).should_be('empate');
										},

								'deve vencer papel': function() {
										var resultado = jokenpo('tesoura', 'papel');
										value_of(resultado).should_be('tesoura');
										},

								'deve perder para pedra': function() {
										var resultado = jokenpo('tesoura', 'pedra');
										value_of(resultado).should_be('pedra');
										},
								});

});

