# Detector Resilience Lab

<p align="center"><img src="./docs/media/social-preview.svg" alt="Detector Resilience Lab" width="100%"></p>
<p align="center"><img src="./docs/media/demo.gif" alt="Detector Resilience Lab reproducible demo" width="100%"></p>
<p align="center"><strong>Measure how detection fails.</strong></p>
<p align="center">Safe feature-space drift experiments for defensive model research.</p>
<p align="center"><img alt="Test" src="https://github.com/LLR6/LR-Detector-Resilience-Lab/actions/workflows/test.yml/badge.svg"> <img alt="Python 3.10+" src="https://img.shields.io/badge/python-3.10%2B-blue"> <img alt="MIT" src="https://img.shields.io/badge/license-MIT-green"> <img alt="Version" src="https://img.shields.io/badge/version-0.1.0-8b5cf6"></p>

## 30 秒看懂

在不可执行的数值特征上训练透明逻辑回归检测器，再对恶意标签样本施加固定种子的特征漂移，比较漂移前后的 TP / FP / TN / FN，并保留翻转样本的特征差值。

```text
Labeled features → Train → Baseline → Safe drift → Degradation report
```

## 5 分钟 Demo

```bash
python -m pip install -e .
detector-resilience examples/features.csv --seed 7 --output report.json
```

仓库样例的固定结果：

| 阶段 | TP | FN | Recall |
|---|---:|---:|---:|
| Baseline | 10 | 0 | 1.00 |
| Feature drift | 8 | 2 | 0.80 |

## 为什么值得研究

高测试集准确率不能说明模型面对分布漂移仍然可靠。报告同时输出模型退化、翻转样本和逐特征变化，便于讨论鲁棒性、反例与再训练策略。

## 边界

实验只修改 CSV 中的数值特征，不读取、生成或修改可执行文件，也不提供杀软绕过载荷。样例很小，只用于验证实验管线；结论不能外推到真实恶意软件数据集。

## 研究路线

加入交叉验证、校准曲线、多个分类器、特征归因、漂移检测与公开安全数据集适配器。

作者：LLR6 · MIT License
