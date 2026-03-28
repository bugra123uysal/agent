import finnhub
import requests
from google import genai
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st

# finnhub api key
api_key="*************"

# gemini  api key
g_api_key="***********"


hisse=["AMD","NVDA","MU","TSM"]
for hf in hisse:
    # şuanki fiyat
    url=f"https://finnhub.io/api/v1/quote?symbol={hf}&token={api_key}"
    response=requests.get(url)
    data=response.json()
    hisse=data.get('c')

    # 52 haftalık fiyat
    metrics=requests.get(f"https://finnhub.io/api/v1/stock/metric?symbol={hf}&metric=all&token={api_key}").json()
    # Fiyat / 52 Hafta
    high_52w        = metrics['metric'].get('52WeekHigh')
    low_52w         = metrics['metric'].get('52WeekLow')
    rtn_52w         = metrics['metric'].get('52WeekPriceReturnDaily')
    rtn_ytd         = metrics['metric'].get('ytdPriceReturn')
    beta            = metrics['metric'].get('beta')
    
    # Değerleme
    pe_ttm          = metrics['metric'].get('peBasicExclExtraTTM')
    pe_norm         = metrics['metric'].get('peNormalizedAnnual')
    pb              = metrics['metric'].get('pbAnnual')
    ps_ttm          = metrics['metric'].get('psTTM')
    ev_ebitda       = metrics['metric'].get('evToEbitdaTTM')
    ev_satis        = metrics['metric'].get('evToSalesTTM')
    p_fcf           = metrics['metric'].get('pfcfShareTTM')
    defter_hisse    = metrics['metric'].get('bookValueShareAnnual')
    
    # Karlılık & Büyüme
    roe             = metrics['metric'].get('roeTTM')
    roa             = metrics['metric'].get('roaAnnual')
    roi             = metrics['metric'].get('roiTTM')
    brut_marj       = metrics['metric'].get('grossMarginTTM')
    net_marj        = metrics['metric'].get('netProfitMarginTTM')
    faaliyet_marj   = metrics['metric'].get('operatingMarginTTM')
    eps_ttm         = metrics['metric'].get('epsBasicExclExtraTTM')
    eps_buyume_3y   = metrics['metric'].get('epsGrowth3Y')
    eps_buyume_5y   = metrics['metric'].get('epsGrowth5Y')
    gelir_buyume_3y = metrics['metric'].get('revenueGrowth3Y')
    gelir_buyume_yoy= metrics['metric'].get('revenueGrowthTTMYoy')
    
    # Borç & Likidite
    d_e_oran        = metrics['metric'].get('totalDebt/totalEquityAnnual')
    uzun_vade_d_e   = metrics['metric'].get('longTermDebt/equityAnnual')
    net_borc        = metrics['metric'].get('netDebtAnnual')
    cari_oran       = metrics['metric'].get('currentRatioAnnual')
    asit_test       = metrics['metric'].get('quickRatioAnnual')
    
    # Nakit Akışı
    fcf             = metrics['metric'].get('freeCashFlowTTM')
    fcf_hisse       = metrics['metric'].get('freeCashFlowPerShareTTM')
    
    # Temettü
    temttu_verimi   = metrics['metric'].get('dividendYieldIndicatedAnnual')
    temttu_hisse    = metrics['metric'].get('dividendsPerShareAnnual')
    odeme_orani     = metrics['metric'].get('payoutRatioTTM')

    print(f"{hf}:{hisse}\n 52 haftalık en yüksek fiyat: {high_52w} \n 52 haftalık en düşük fiyat: {low_52w} \n  \n\n\n\n\n\n ")

    cıktı = f"""
    52 Hafta Yüksek         : {high_52w        }
    52 Hafta Düşük          : {low_52w         }
    52 Hafta Getiri %       : {rtn_52w         }
    YTD Getiri %            : {rtn_ytd         }
    Beta                    : {beta            }
    
    F/K (TTM)               : {pe_ttm          }
    F/K Normalize           : {pe_norm         }
    F/Defter                : {pb              }
    F/Satış (TTM)           : {ps_ttm          }
    EV/EBITDA (TTM)         : {ev_ebitda       }
    EV/Satış (TTM)          : {ev_satis        }
    Fiyat/FCF (TTM)         : {p_fcf           }
    Defter Değeri/Hisse     : {defter_hisse    }
    
    ROE (TTM)               : {roe             }
    ROA (Yıllık)            : {roa             }
    ROI (TTM)               : {roi             }
    Brüt Marj (TTM)         : {brut_marj       }
    Net Marj (TTM)          : {net_marj        }
    Faaliyet Marjı (TTM)    : {faaliyet_marj   }
    
    EPS (TTM)               : {eps_ttm         }
    EPS Büyüme 3Y           : {eps_buyume_3y   }
    EPS Büyüme 5Y           : {eps_buyume_5y   }
    Gelir Büyüme 3Y         : {gelir_buyume_3y }
    Gelir Büyüme YoY        : {gelir_buyume_yoy}
    
    Borç/Özkaynak           : {d_e_oran        }
    Uzun Vade Borç/Özkaynak : {uzun_vade_d_e   }
    Net Borç                : {net_borc        }
    Cari Oran               : {cari_oran       }
    Asit-Test Oranı         : {asit_test       }
    
    Serbest Nakit Akışı     : {fcf             }
    FCF/Hisse               : {fcf_hisse       }
    
    Temettü Verimi          : {temttu_verimi   }
    Temettü/Hisse           : {temttu_hisse    }
    Ödeme Oranı             : {odeme_orani     }
    """
    
    print(cıktı)
# gemini
llm=ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    # gemini  api key
    g_api_key="AIzaSyBn2XISk5PC_lCR_BOGm3DHqb_kjvJ9wNU",
    temperature=0.7, # yaratıcılık oranı
)
sor=llm.invoke("MU hissesi ile ilgili son haberler ve hisse hakkındaki biligler RSI 100 50 200 günlük ortalama fiyatları nedir teşekkürler?")
print(sor.content)

"""  
score=0

if rsı < 50:
    score +=1
elif ma50 

"""


  