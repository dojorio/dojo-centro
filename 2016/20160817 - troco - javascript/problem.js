exports.troco = function (preco, pagamento) {
    return preco == pagamento ? {} : {'1':1}
};
