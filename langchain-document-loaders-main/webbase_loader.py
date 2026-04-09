from dotenv import load_dotenv
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

#model = ChatOpenAI()

prompt = PromptTemplate(
    template='Answer the following question \n {question} from the following text - \n {text}',
    input_variables=['question','text']
)

url = 'https://www.flipkart.com/apple-macbook-air-m4-16-gb-256-gb-ssd-macos-sequoia-mw123hn-a/p/itm08069ed2395aa?pid=COMH9ZWQDGMTF3HA&lid=LSTCOMH9ZWQDGMTF3HAIAWW11&marketplace=FLIPKART&q=macbook+air+m4&store=6bo%2Fb5g&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_2_8_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_8_na_na_na&fm=Search&iid=ba10645c-7030-455c-8aae-c360162a2b72.COMH9ZWQDGMTF3HA.SEARCH&ppt=sp&ppn=sp&ssid=in4brgim1s0000001756727069426&qH=a3dc101ea3bce06d'
loader = WebBaseLoader(url)

docs = loader.load()

print("content: ", docs[0].page_content)

