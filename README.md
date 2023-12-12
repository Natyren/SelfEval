# [SelfEval: Automated Evaluation for Text-to-Image Generative Models](https://arxiv.org/abs/2311.10708)

## Overview

This repository contains the open-source implementation of the SelfEval method, a novel approach to assessing the text-to-image understanding capabilities of generative models. SelfEval leverages the generative model to compute the likelihood of real images given text prompts, enabling automated and fine-grained evaluation on various tasks, including attribute binding, color recognition, counting, shape recognition, and spatial understanding.


## Key Features

- **Fine-Grained Evaluation:** SelfEval facilitates the assessment of generative models on tasks such as attribute binding, color recognition, counting, shape recognition, and spatial understanding, providing detailed insights into their capabilities.

- **Compatibility with Standard Datasets:** Leveraging existing multimodal text-image discriminative model evaluation datasets, SelfEval ensures a standardized and comparable evaluation methodology.

- **High Agreement with Human Evaluations:** SelfEval is the first automated metric to demonstrate a high degree of agreement with gold-standard human evaluations across multiple models and benchmarks, particularly in measuring text-faithfulness.

- **Challenging Task Evaluation:** SelfEval allows the evaluation of generative models on challenging tasks, such as the Winoground image-score, where they exhibit competitive performance compared to discriminative models.

- **Mitigation of Drawbacks in Standard Metrics:** The repository highlights severe drawbacks of standard automated metrics, such as CLIP-score, for measuring text faithfulness on benchmarks like DrawBench, and demonstrates how SelfEval addresses and sidesteps these issues.

## Usage

To use SelfEval for automated evaluation of your text-to-image generative models, follow the instructions in the provided documentation. The repository includes code, examples, and pre-trained models to streamline the evaluation process.


## Contributions and Issues

Contributions and issue reports are welcome! Feel free to fork the repository, make improvements, and submit pull requests. If you encounter any issues or have suggestions for enhancements, please open an issue on the repository.
