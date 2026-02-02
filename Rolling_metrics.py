def rolling_es(return1, window=250, conf=0.975):
    ES=[]
    for i in len(return1):
        if i<250:
            ES.append(np.nan)
        else:
            window_pnl=return1.iloc[i-window:i]
            var=np.percentile(window_pnl,(1-conf)*100)
            es=-window_pnl[window_pnl<var].mean()
            ES.append(es)
    return ES
