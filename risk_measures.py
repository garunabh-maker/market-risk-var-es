def historical_pnl(return2, conf=0.975):
    var_975=-np.percentile(return2,(1-conf)*100)
    return var_975

def expected_shortfall(return2, conf=0.975):
    var_975=np.percentile(return2,(1-conf)*100)
    es=-return2[return2<var_975].mean()
    return es