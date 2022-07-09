import streamlit as st
import pandas as pd


st.header('ApeRealm Link&Data')


expander = st.expander("Ethscan_Link")

egst_link = '[eGST](https://etherscan.io/token/0x473037de59cf9484632f4A27B509CFE8d4a31404?a=0x9c97a34b3f6d2c6cc9e5cbb77f5214fee6d2b70f#readContract)'
expander.markdown(egst_link, unsafe_allow_html=True)

egmt_link = '[eGMT](https://etherscan.io/token/0xe3c408BD53c31C085a1746AF401A4042954ff740?a=0x9c97a34b3f6d2c6cc9e5cbb77f5214fee6d2b70f)'
expander.markdown(egmt_link, unsafe_allow_html=True)

unei_link = '[運営アドレス](https://etherscan.io/address/0x776019eC6b3dEe2B8fd4232cC70395A75E0Eb0d2)'
expander.markdown(unei_link, unsafe_allow_html=True)

dooar_link = '[DooarSwapv2Router02](https://etherscan.io/address/0x53e0e51b5Ed9202110D7Ecd637A4581db8b9879F)'
expander.markdown(dooar_link, unsafe_allow_html=True)

egstweth_link = '[Dooar eGST-WETHプール](https://etherscan.io/address/0x09d614845450c1002d04213b68c386a747d0a65a)'
expander.markdown(egstweth_link, unsafe_allow_html=True)

egstusdc_link = '[Dooar eGST-USDCプール](https://etherscan.io/address/0x770cbfff3c47134a878d513921ac59a1fd24e514)'
expander.markdown(egstusdc_link, unsafe_allow_html=True)

usdcweth_link = '[Dooar USDC-WETHプール](https://etherscan.io/address/0x9c2DC3D5ffcEcF61312C5F4C00660695B32fB3D1)'
expander.markdown(usdcweth_link, unsafe_allow_html=True)

usdcegmt_link = '[Dooar USDC-eGMTプール](https://etherscan.io/address/0xAeAca8C32039A466FB32Bde6F566130A1f49D21e)'
expander.markdown(usdcegmt_link, unsafe_allow_html=True)


expander = st.expander("神ツール_Link")

tokenbuyer_link = '[Tokenbuyer](https://tokenbuyer.notdao.io/?v=1)'
expander.markdown(tokenbuyer_link, unsafe_allow_html=True)

dooarswap_link = '[DooarSwap](https://dooarswap.notdao.io/#/swap)'
expander.markdown(dooarswap_link, unsafe_allow_html=True)

manual_link = '[神ツール使用手順](https://magareba.com/egst-early-buy-sell/)'
expander.markdown(manual_link, unsafe_allow_html=True)

expander.caption('神へのお礼')
code = '0x7EEfDc91f5F972eC855f34055f4945B3B419925C'
expander.code(code, language='python')

expander = st.expander("Chart_Link")
dooar_gst_link = '[(Dooarswap) eGST-USDCチャート](https://dexscreener.com/ethereum/0x770cbfff3c47134a878d513921ac59a1fd24e514)'
expander.markdown(dooar_gst_link, unsafe_allow_html=True)

uni_gst_link = '[(Uniswap) eGST-USDCチャート](https://dexscreener.com/ethereum/0xf6b6d608e8aad7a40597f280aa5206fceb0b9364)'
expander.markdown(uni_gst_link, unsafe_allow_html=True)


expander = st.expander("Contract_Data")

d = {'コントラクトアドレス':['0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48',
    '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2',
    '0x473037de59cf9484632f4A27B509CFE8d4a31404',
    '0xe3c408BD53c31C085a1746AF401A4042954ff740'],
     'Decimals':[6,18,8,8]}
     
df = pd.DataFrame(data=d,index=['USDC','WETH','eGST','eGMT'])
expander.write(df)

if st.checkbox('STEPNで損した人はCheck'):
     uni_gst_link = '[『歩くな』](https://mirror.xyz/0x2F17901116041821b52b48e07d08a8071B7e0E89/uUZZmjg3VJHUkxeJOa0uDLdH0eO0SLhuDNFDLvts01Y)'
     st.markdown(uni_gst_link, unsafe_allow_html=True)