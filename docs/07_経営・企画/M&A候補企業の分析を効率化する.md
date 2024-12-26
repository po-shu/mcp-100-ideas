# M&A候補企業の分析を効率化する

## アイデア
M&A専門データベースの分析結果を起点に、ニュースやソーシャルメディアなどの最新情報を組み合わせて、より包括的な企業評価を支援します。専門家の深い分析と、オープンデータでのトレンド把握を組み合わせることで、シナジー効果の予測とリスク評価の質を向上させます。<br>

### 具体例
製造業の経営企画部門が新規事業領域への参入を検討する際、Capital IQやSPEEDAでの定量分析を基に、最新の市場動向や企業評判をオープンデータから収集。財務・事業性評価に加えて、組織カルチャーや市場での評価も含めた、より立体的な企業理解を実現します。<br>

## アーキテクチャ
| Type | Name | Role |
|--|--|--|
| Client | Claude Desktop App | データ統合と分析支援のインターフェース |
| Server | Brave Search | ニュース、SNS、業界トレンドの収集 |
| Server | PostgreSQL | 分析データの集約と履歴管理 |
| Server | Fetch | 専門DBからのデータ取得 |
| Server | Confluence | 分析テンプレートと評価ノウハウの管理 |

```mermaid
sequenceDiagram
    actor User as 経営企画担当者
    participant MCP as Claude Desktop App
    participant Fetch as Fetch Server
    participant Brave as Brave Search Server
    participant DB as PostgreSQL Server
    participant Wiki as Confluence Server

    note over User,Wiki: Capital IQ, SPEEDA等の<br>専門DBには別途アクセス

    User->>MCP: 候補企業を指定
    MCP->>Wiki: 分析テンプレート取得
    Wiki-->>MCP: テンプレート
    MCP->>Fetch: 専門DB APIの実行
    Fetch-->>MCP: 財務・事業データ
    MCP->>Brave: 最新動向の検索
    Brave-->>MCP: オープンデータ
    MCP->>DB: データの統合保存
    DB-->>MCP: 保存完了
    MCP-->>User: 初期評価レポート提示

    User->>MCP: シナジー分析を依頼
    MCP->>DB: 過去の分析データ取得
    DB-->>MCP: 類似事例データ
    MCP->>Wiki: 評価ノウハウの参照
    Wiki-->>MCP: 分析ガイドライン
    MCP-->>User: シナジー予測<br>リスク評価<br>優先度提案

    User->>MCP: 分析結果の保存を依頼
    MCP->>DB: 評価データを保存
    DB-->>MCP: 保存完了
    MCP->>Wiki: ノウハウを追記
    Wiki-->>MCP: 更新完了
    MCP-->>User: 完了報告
```

## 思考プロセス

### 対象の活動の価値は何か
- 専門家による定量分析と最新のオープンデータの組み合わせ
- 財務・事業面だけでなく、組織や市場評価も含めた多角的な分析
- 過去の分析事例とノウハウの組織的な蓄積と活用
- より質の高い意思決定のための情報提供

### 価値を妨げる課題は何か
- 専門DBとオープンデータの統合的な分析の難しさ
- データソースごとの更新タイミングのばらつき
- 定性的な評価要素の数値化や比較の困難さ
- 分析ノウハウの属人化

### なぜ課題が発生するのか、仮説推論
- 各種専門DBが独立して存在し、横断的な分析が困難
- オープンデータの信頼性や重要度の判断が必要
- 業界特性や企業規模による評価基準の違い
- 分析経験の共有と再利用の仕組みが不足