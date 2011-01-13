using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace Dojo
{
    public static class Matchers
    {
        public static void AoAplicarSolucaoDeveSer(this string expressao, string numero)
        {
            var teclado = new Teclado();
            var numero_calculado = teclado.resolver(expressao);
            Assert.AreEqual(numero, numero_calculado);
        }

    }

    [TestClass]
    public class UnitTest1
    {

        [TestMethod]
        public void retorna_6_ao_receber_M()
        {
            "M".AoAplicarSolucaoDeveSer("6");
        }

        [TestMethod]
        public void retorna_2_ao_receber_A()
        {
            var teclado = new Teclado();
            var numero = teclado.resolver(expressao: "A");
            Assert.AreEqual("2", numero);
        }

        [TestMethod]
        public void retorna_2_ao_receber_B()
        {
            var teclado = new Teclado();
            var numero = teclado.resolver(expressao: "B");
            Assert.AreEqual("2", numero);
        }

        [TestMethod]
        public void retorna_2_ao_receber_C()
        {
            var teclado = new Teclado();
            var numero = teclado.resolver(expressao: "C");
            Assert.AreEqual("2", numero);
        }
        [TestMethod]
        public void retorna_6_ao_receber_O()
        {
            var teclado = new Teclado();
            var numero = teclado.resolver(expressao: "O");
            Assert.AreEqual("6", numero);
        }
        [TestMethod]
        public void retorna_Hifen_ao_receber_Hifen()
        {
            var teclado = new Teclado();
            var numero = teclado.resolver(expressao: "-");
            Assert.AreEqual("-", numero);
        }
        [TestMethod]
        public void retorna_99_ao_receber_XY()
        {
            var teclado = new Teclado();
            var numero = teclado.resolver(expressao: "XY");
            Assert.AreEqual("99", numero);
        }
    }
}
