# TableauでKPIダッシュボードを改善する

## アイデア
Tableauを活用した業績予測において、予測モデルのパラメータ調整とデータソース連携を効率化。外部要因の取り込みを自動化し、予測精度を向上させる。

### 具体例
小売チェーンの経営企画部で、店舗別の売上予測モデルのパラメータを調整する場面。新規出店の影響や外部要因を加味しながら、Tableauダッシュボードの予測精度を向上させる。

## アーキテクチャ
| Type | Name | Role |
|--|--|--|
| Client | Claude Desktop App | 予測モデル改善の対話型支援 |
| Server | Tableau MCP Server [要自作] | TableauのREST APIを利用した設定値の取得・更新 |
| Server | PostgreSQL | モデル調整履歴とその効果の記録 |
| Server | Fetch | 外部要因データの構造化収集 |

```mermaid
sequenceDiagram
    actor User as アナリスト
    participant CAP as Claude Desktop App
    participant TBL as Tableau MCP Server
    participant DB as PostgreSQL
    participant FTC as Fetch
    
    User->>CAP: 予測モデルの改善を依頼
    CAP->>TBL: 現在の設定を取得
    TBL-->>CAP: 設定情報を返却
    CAP->>DB: 過去の調整履歴を確認
    DB-->>CAP: 類似条件での履歴を返却
    CAP->>FTC: 関連する外部要因を収集
    FTC-->>CAP: 構造化された市場データを返却
    CAP-->>User: モデル調整案を提示
    User->>CAP: 調整案の承認
    CAP->>TBL: モデルパラメータを更新
    TBL-->>User: Tableau上で更新を確認
    User->>CAP: 予測精度の検証を依頼
    CAP->>TBL: 予測と実績の差異を分析
    TBL-->>CAP: 分析結果を返却
    CAP->>DB: 調整結果を記録
    DB-->>CAP: 記録完了を通知
    CAP-->>User: 改善提案を提示
```

## 思考プロセス

### 対象の活動の価値は何か
- 予測モデルの継続的な精度向上と工数削減
    - モデル調整の試行錯誤を効率化
    - 新規出店影響の定量化が容易に
    - レポート作成の自動化

### 価値を妨げる課題は何か
- Tableau操作の専門性が必要
- モデル調整の判断基準が属人化
- 外部要因の取り込みが手作業

### なぜ課題が発生するのか、仮説推論
- Tableauの機能が多岐にわたり習熟に時間が必要
- 予測精度向上のノウハウが体系化されていない
- 各種データソースとの連携に個別の設定が必要