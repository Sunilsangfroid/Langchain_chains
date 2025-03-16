from langchain_core.prompts import PromptTemplate
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel

load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")
if not google_api_key:
    raise ValueError("GOOGLE_API_KEY is not set in the environment variables")

model1 = ChatGoogleGenerativeAI(model='gemini-1.5-pro', api_key=google_api_key)
model2 = ChatGoogleGenerativeAI(model='gemini-1.5-pro', api_key=google_api_key)

prompt1 = PromptTemplate(
    template='Generate short and simple notes from the following text \n {text}',
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template='Generate 5 short question answers on the following text \n {text}',
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template='Merge the provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz}',
    input_variables=['notes', 'quiz']
)
parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})

merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain

text ="""
Successes of DMs Since the pioneering works by Sohl-Dickstein et al. (2015), Ho et al.
(2020b), and Song et al. (2020c), diffusion models (DMs) have emerged as the leading
approach for generative modeling, finding widespread use in various domains, including
neural image synthesis and editing (Nichol and Dhariwal, 2021; Dhariwal and Nichol, 2021;
Ramesh et al., 2022b; Saharia et al., 2022a; Rombach et al., 2022), audio and molecule
synthesis (Hoogeboom et al., 2022; Chen et al., 2020), image segmentation (Baranchuk et al.,
2021), and video or 3D object generation (Ho et al., 2022; Molad et al., 2023; Poole et al.,
2022b). DMs have shown remarkable performance improvements over time, as seen in the
steady trend of unconditional Frechet Inception Score (Heusel et al., 2017) (FID) reductions
on datasets such as CIFAR10, from 25.32 (Song and Ermon, 2019) to 1.97 (Karras et al.).
Diffusion Distillation The concept of knowledge distillation (Hinton et al., 2015; Oord
et al., 2018), which aims to create smaller and more efficient models while maintaining
accuracy, has shown great success in various research domains. In particular, distilling
knowledge from pre-trained classifiers has resulted in models with comparable accuracy,
reduced model size, and improved inference efficiency (Touvron et al., 2021). Given the
success of diffusion models (DMs) in numerous applications, there is a growing interest in
distilling knowledge from these models to create smaller and more efficient versions. One of
the key motivations for diffusion distillation is to significantly accelerate the sampling speed,
which is currently hindered by the large number of neural function evaluations required. To
improve the inference efficiency of DMs, researchers are exploring ways to distill the learned
knowledge from DMs to efficient sampling mechanisms, such as a direct implicit generator or
a fewer-steps vector field. By doing so, they have been able to create student models that
have further improved inference efficiency with minimal performance loss. Some distilled
student models require less than 10 neural function evaluations but still offer comparable
generative performance to their larger counterparts.
Diffusion distillation also serves as a means to establish connections between DMs
and other generative models, such as implicit generative models and normalizing flows.
Through knowledge transfer between DMs and other models, researchers can study the
micro-connections between them and explore their potential for future generative modeling
research.
This paper provides a comprehensive review of existing research on diffusion distillation
strategies. Our review is organized into three main categories: diffusion-to-field (D2F)
distillation (Section 2), diffusion-to-generator (D2G) distillation (Section 3), and training-free
(TF) distillation (Section 4). Each category contains studies that share similar settings and
methodologies. In addition to our categorization, we also discuss broader topics in diffusion
distillation throughout the rest of this survey."""

result = chain.invoke({'text':text})

print(result)

chain.get_graph().print_ascii()