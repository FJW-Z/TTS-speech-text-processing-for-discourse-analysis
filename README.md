# TTS-speech-text-processing-for-discourse-analysis
a program to process linguistic data in a TTS project for a moblile phone voice assistant (as an intern linguistic engineer)

# TTS-Speech-Text Processing Tools for Discourse Analysis  
语音-文本处理工具集（用于多模态话语分析与计算语言学研究）


## 项目定位  
本仓库整合了实习期间开发的语音相关文本处理工具，专注于解决**多模态话语分析、计算语言学研究**中的数据预处理问题。工具链覆盖从原始语音文本（如ASR输出、TTS输入）到标准化语料库的全流程处理，可直接用于公共话语、媒体传播等场景的语料构建与分析。  


## 核心功能模块  
按“数据处理流水线”逻辑分为4大模块，支持从格式转换到工程化批量处理的完整需求：  

### 1. 多模态数据格式转换  
`01_format_conversion/`  
- `excel_to_txt_clean.ipynb`：将含标注的Excel表格（如语音文本对齐数据）转换为纯文本（TXT），支持清洗空值、过滤无效行，保留关键语料信息。  
- `excel_to_txt_basic.ipynb`：基础版Excel转TXT工具，适合快速提取表格中的文本列（如TTS训练文本）。  
- `txt_to_excel.ipynb`：将零散TXT文本按行/列结构化写入Excel，便于语料的二次标注（如添加情感标签、话语主体信息）。  

### 2. 文本数据清洗与标准化  
`02_text_cleaning/`  
- `text_case_normalization.ipynb`：文本大小写规范处理（如将全大写语音转写文本转为首字母大写），适配语言学分析中的格式一致性要求。  
- `text_deduplication_truncation.ipynb`：去除重复文本（避免训练/分析偏差）、截断超长文本（适配模型输入限制），提升语料质量。  

### 3. 文本拆分与编码  
`03_text_splitting_encoding/`  
- `txt_splitter.ipynb`：按规则拆分长文本（如按标点、固定长度），生成子文件，适合大规模语料的批量标注或模型分批输入。  
- `text_encoding_with_freq.ipynb`：为文本添加编号、统计字频并编码，辅助话语特征量化分析（如公共话语中的高频词分布）。  

### 4. 工程化工具链  
`04_engineering_tools/`  
- `file_batcher.ipynb`：按数量自动拆分文件夹中的文件（如将1000条语音文本分成10个批次），支持并行处理与团队协作标注。  
- `asr_text_generation.ipynb`：ASR输出文本的后处理工具（如修正识别错误、补全省略语），衔接语音识别与文本分析环节。  


## 技术栈  
- 编程语言：Python 3.8+  
- 核心库：pandas（数据处理）、numpy（数值计算）、re（正则清洗）  
- 运行环境：Jupyter Notebook（支持交互式调试与结果可视化）  


## 研究应用场景  
1. **多模态语料库构建**：通过格式转换与清洗工具，将语音（ASR）、文本、标注数据整合为标准化语料库，用于“语音-文本”模态对比研究（如公共演讲中语音语调与文本情感的关联）。  
2. **舆情分析预处理**：批量处理社交媒体语音转写文本，去重、标准化后可直接输入情感分析模型，提升舆情量化精度。  
3. **计算语言学实验**：文本拆分与编码工具支持大规模语料的特征提取，可用于话语风格分类、语言政策影响评估等研究。  


## 使用说明  
1. 安装依赖：  
   ```bash
   pip install pandas numpy jupyter
2. 选择对应模块的 .ipynb 文件，按注释修改输入路径（支持本地文件或语料库路径）。
3. 运行代码块，输出结果将保存在指定目录（默认与输入同路径）。
   
版本更新
2024.10：优化文本去重算法，支持自定义重复阈值；新增 ASR 文本补全功能。
2024.09：初始版本，完成格式转换与基础清洗模块。

若用于学术研究，欢迎引用或联系进一步交流跨学科应用场景！

# Speech-Text Processing Tools for Discourse Analysis  
Tools for Multimodal Discourse Analysis and Computational Linguistics  


## Project Overview  
This repository integrates speech-related text processing tools developed during my internship, focusing on **data preprocessing for multimodal discourse analysis and computational linguistics research**. The toolchain covers the entire workflow from raw speech text (e.g., ASR output, TTS input) to standardized corpus construction, enabling direct application in scenarios such as public discourse analysis and media communication.  


## Core Modules (Data Processing Pipeline)  
The tools are organized into 4 modules to support end-to-end processing from format conversion to engineering-level batch operations:  

### 1. Multimodal Data Format Conversion  
`01_format_conversion/`  
- `excel_to_txt_clean.ipynb`: Converts annotated Excel spreadsheets (e.g., speech-text alignment data) to plain text (TXT), with support for null value cleaning and invalid row filtering to retain key corpus information.  
- `excel_to_txt_basic.ipynb`: Basic Excel-to-TXT converter, ideal for quickly extracting text columns (e.g., TTS training text) from spreadsheets.  
- `txt_to_excel.ipynb`: Structurally writes scattered TXT text into Excel row-by-row/column-by-column, facilitating secondary annotation (e.g., adding sentiment labels, discourse subject information).  

### 2. Text Cleaning and Standardization  
`02_text_cleaning/`  
- `text_case_normalization.ipynb`: Normalizes text case (e.g., converting all-uppercase speech transcription to title case), meeting format consistency requirements in linguistic analysis.  
- `text_deduplication_truncation.ipynb`: Removes duplicate text (to avoid training/analysis bias) and truncates overly long text (to fit model input constraints), improving corpus quality.  

### 3. Text Splitting and Encoding  
`03_text_splitting_encoding/`  
- `txt_splitter.ipynb`: Splits long text into sub-files by rules (e.g., punctuation, fixed length), suitable for batch annotation or model分批 input of large-scale corpora.  
- `text_encoding_with_freq.ipynb`: Adds numbering to text, counts word frequency, and encodes text to support quantitative analysis of discourse features (e.g., distribution of high-frequency words in public discourse).  

### 4. Engineering Toolchain  
`04_engineering_tools/`  
- `file_batcher.ipynb`: Automatically splits files in a folder by quantity (e.g., dividing 1000 speech texts into 10 batches), supporting parallel processing and team collaborative annotation.  
- `asr_text_generation.ipynb`: Post-processing tool for ASR output text (e.g., correcting recognition errors,补全省略语), bridging the gap between speech recognition and text analysis.  


## Tech Stack  
- Programming Language: Python 3.8+  
- Core Libraries: pandas (data processing), numpy (numerical computation), re (regex cleaning)  
- Runtime Environment: Jupyter Notebook (supports interactive debugging and result visualization)  


## Research Application Scenarios  
1. **Multimodal Corpus Construction**: Integrates speech (ASR), text, and annotation data into a standardized corpus via format conversion and cleaning tools, enabling “speech-text” modal comparison studies (e.g., the correlation between speech intonation and text sentiment in public speeches).  
2. **Sentiment Analysis Preprocessing**: Batch-processes speech transcription text from social media, and the deduplicated/standardized text can be directly fed into sentiment analysis models to improve quantification accuracy.  
3. **Computational Linguistics Experiments**: Text splitting and encoding tools support feature extraction from large-scale corpora, enabling research on discourse style classification, language policy impact assessment, etc.  


## Usage Instructions  
1. Install Dependencies:  
   ```bash
   pip install pandas numpy jupyter
2. Select the corresponding .ipynb file in each module, modify the input path as per comments (local files or corpus paths are supported).
3. Run the code blocks; output results will be saved in the specified directory (default is the same path as input).
   
Version Updates
Oct 2024: Optimized text deduplication algorithm (supports custom duplication thresholds); added ASR text completion functionality.
Sep 2024: Initial version, completed format conversion and basic cleaning modules.

For academic research, feel free to cite or contact me for further discussion on interdisciplinary applications!
