# 罗店.cn — 上海宝山罗店本地信息门户

纯静态 HTML 站点，托管于 GitHub Pages，面向中国大陆用户的本地生活门户 MVP。

## 页面结构

| 文件 | 内容 |
|---|---|
| `index.html` | 首页：栏目入口、资讯推荐、商家速览、入驻 CTA |
| `news.html` | 罗店资讯：罗店镇历史沿革（时间轴）与区域资源 |
| `scenic.html` | 景点游玩总览 |
| `town.html` | 罗店古镇游玩攻略 |
| `meilanhu.html` | 美兰湖游玩攻略 |
| `shops.html` | 本地商家黄页（5 条示例占位数据） |
| `house.html` | 厂房商铺租赁信息展示 |
| `service.html` | 便民服务电话与办事指引 |
| `contact.html` | 商家入驻（第三方表单 iframe 占位） |
| `about.html` | 关于本站与免责声明 |
| `CNAME` | 自定义域名 `xn--4kq07d.cn`（罗店.cn 的 punycode） |

## 部署步骤（GitHub Pages）

1. 将本目录推送至 GitHub 仓库 `mfujun2025/luodian` 的 `main` 分支；
2. 仓库 Settings → Pages → Source 选择 `Deploy from a branch`，分支 `main`，目录 `/ (root)`；
3. 在 Custom domain 填入 `罗店.cn`（或 `xn--4kq07d.cn`），勾选 Enforce HTTPS；
4. 域名注册商处把 罗店.cn 的 DNS 解析（CNAME 到 `mfujun2025.github.io`，或接入 Cloudflare CDN 后由 Cloudflare 托管 DNS）。

## 上线前待办

- [ ] 将 `shops.html` 中的 5 条示例商家替换为真实商家信息；
- [ ] 将 `contact.html` 中 `https://example.com/your-form` 替换为飞书表单 / 腾讯问卷 iframe 地址；
- [ ] 核实 `service.html` 中的电话并替换【示例】条目；
- [ ] 替换 `about.html` 中的示例邮箱；
- [ ] 页脚 ICP 备案号在备案完成后更新；
- [ ] 访问速度优化：接入 Cloudflare CDN（国内直连 GitHub Pages 不稳定）。

## 合规提示

未完成 ICP 备案前，本站仅提供免费信息展示与免费收录，不开展付费经营性业务；付费置顶、广告联盟等变现服务在备案完成后开放。
