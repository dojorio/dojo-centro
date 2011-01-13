using System;
using System.Collections.Generic;
using System.Text.RegularExpressions;

namespace Dojo
{
    public class Teclado
    {
        internal object resolver(string expressao)
        {
            
            var expressoesMapeadas = criarExpressoesMapeadas();

            foreach(var mapeamento in expressoesMapeadas)
            {
                expressao = Regex.Replace(expressao, 
                    mapeamento.Key, mapeamento.Value);   
            }
            
            return expressao;
        }

        private static Dictionary<string, string> criarExpressoesMapeadas()
        {
            var mapeamentos = new Dictionary<string, string>()
                                  {
                                      {"[OM]", "6"},
                                      {"[A-C]", "2"},
                                      {"[W-Z]", "9"}

                                  };
            return mapeamentos;
        }
    }





}
