"use strict";(self.webpackChunkheng_docs=self.webpackChunkheng_docs||[]).push([[1974],{5254:(e,t,n)=>{n.r(t),n.d(t,{assets:()=>i,contentTitle:()=>o,default:()=>p,frontMatter:()=>a,metadata:()=>c,toc:()=>d});var s=n(4848),r=n(8453);const a={sidebar_position:1},o="\u81f4\u5f00\u53d1\u8005\u7684\u4e00\u5c01\u4fe1",c={id:"tutorial-basics/create-a-page",title:"\u81f4\u5f00\u53d1\u8005\u7684\u4e00\u5c01\u4fe1",description:"\u4eb2\u7231\u7684\u5f00\u53d1\u8005\uff1a",source:"@site/docs/tutorial-basics/create-a-page.md",sourceDirName:"tutorial-basics",slug:"/tutorial-basics/create-a-page",permalink:"/heng-docs/docs/tutorial-basics/create-a-page",draft:!1,unlisted:!1,editUrl:"https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/docs/tutorial-basics/create-a-page.md",tags:[],version:"current",sidebarPosition:1,frontMatter:{sidebar_position:1},sidebar:"tutorialSidebar",previous:{title:"Meet Sparky",permalink:"/heng-docs/docs/category/meet-sparky"},next:{title:"Sparky \u54ee\u5929\u4f7f\u7528\u8bf4\u660e\u4e66",permalink:"/heng-docs/docs/tutorial-basics/create-a-document"}},i={},d=[];function u(e){const t={h1:"h1",p:"p",...(0,r.R)(),...e.components};return(0,s.jsxs)(s.Fragment,{children:[(0,s.jsx)(t.h1,{id:"\u81f4\u5f00\u53d1\u8005\u7684\u4e00\u5c01\u4fe1",children:"\u81f4\u5f00\u53d1\u8005\u7684\u4e00\u5c01\u4fe1"}),"\n",(0,s.jsx)(t.p,{children:"\u4eb2\u7231\u7684\u5f00\u53d1\u8005\uff1a"}),"\n",(0,s.jsx)(t.p,{children:"\u9996\u5148\uff0c\u611f\u8c22\u60a8\u9009\u62e9\u5e76\u4fe1\u4efb\u6211\u4eec\u7684\u4ea7\u54c1\u2014\u2014 SPARKY \u54ee\u5929\uff0c\u9996\u4e2a\u624b\u529e\u7ea7\u9ad8\u52a8\u6001\u673a\u5668\u4eba\u5f00\u53d1\u5e73\u53f0\u3002\u6211\u4eec\u6df1\u77e5\uff0c\u4ece\u5c0f\u767d\u5230\u5927\u5e08\u7684\u5f00\u53d1\u8def\u4e0a\u4ece\u6765\u90fd\u4e0d\u662f\u4e00\u5e06\u98ce\u987a\u3002\u800c\u5728\u8fd9\u5d0e\u5c96\u7684\u7ec3\u7ea7\u4e4b\u8def\u4e0a\uff0c\u5f00\u53d1\u8005\u4eec\u901a\u5e38\u4f1a\u9762\u4e34\u4e00\u4e9b\u76f8\u4f3c\u7684\u56f0\u5883\u548c\u96be\u9898\uff1a\u73a9\u6cd5\u5355\u4e00\u3001\u4e0a\u624b\u5f00\u53d1\u56f0\u96be\u3001\u6587\u6863\u8d44\u6e90\u8d2b\u7620\u7b49\u3002"}),"\n",(0,s.jsx)(t.p,{children:"\u56e0\u6b64\uff0c\u540c\u6837\u4f5c\u4e3a\u5f00\u53d1\u8005\u7684\u6211\u4eec\u5728\u8e29\u8fc7\u65e0\u6570\u5751\u540e\u603b\u7ed3\u7ecf\u9a8c\u6559\u8bad\uff0c\u6f5c\u5fc3\u591a\u5e74\u7814\u53d1\uff0c\u5e76\u6700\u7ec8\u4e3a\u5927\u5bb6\u5e26\u6765\u4e86SPARKY \u54ee\u5929\uff0c\u5e0c\u671b\u80fd\u591f\u5728\u964d\u4f4e\u5f00\u53d1\u96be\u5ea6\u7684\u540c\u65f6\u4f7f\u5f00\u53d1\u66f4\u52a0\u4fbf\u6377\uff1a SPARKY \u54ee\u5929\u652f\u6301 Python \u3001C/C++ \u4f5c\u4e3a\u5f00\u53d1\u8bed\u8a00\uff1b\u642d\u8f7d\u81ea\u4e3b\u7814\u53d1\u7684 AIA \u4e00\u4f53\u5316\u6267\u884c\u5668\uff08 ALL-IN-ACTUATOR )\uff0c\u5c06\u817f\u90e8\u4e09\u4e2a\u81ea\u7531\u5ea6\u96c6\u6210\u5728\u4e00\u4e2a\u6267\u884c\u5668\u5185\uff0c\u9ad8\u96c6\u6210\u5ea6\u8bbe\u8ba1\u8d4b\u4e88\u673a\u5668\u4eba\u6781\u5927\u7684\u5de5\u4f5c\u7a7a\u95f4\u548c\u52a8\u4f5c\u7075\u5de7\u5ea6\uff1b\u80fd\u591f\u4e24\u9897\u87ba\u4e1d\u5b9e\u73b0\u817f\u90e8\u6746\u7ec4\u7684\u88c5\u914d\u4e0e\u5347\u7ea7\uff0c\u652f\u6301\u81ea\u884c\u8bbe\u8ba1\u6253\u5370\u4e2a\u6027\u5316\u5916\u58f3\uff1b\u914d\u5907\u5feb\u62c6\u5f0f\u78c1\u5438\u80cc\u90e8\u76d6\u677f\uff0c\u8f7b\u677e\u4f7f\u7528\u5916\u8bbe\u63a5\u53e3\u8fde\u63a5\u60a8\u81ea\u5df1\u7684\u786c\u4ef6\u5916\u8bbe......"}),"\n",(0,s.jsx)(t.p,{children:"\u4e8b\u5b9e\u4e0a\uff0c SPARKY \u4e0d\u4ec5\u662f\u4e00\u53f0\u673a\u5668\u4eba\uff0c\u5b83\u66f4\u662f\u6211\u4eec\u673a\u5668\u4eba\u7f8e\u5b66\u89c2\u7684\u96c6\u4e2d\u4f53\u73b0\u3002\u6211\u4eec\u575a\u6301\u673a\u5668\u4eba\u8bbe\u8ba1\u201c\u5c11\u5373\u662f\u591a\uff0c\u8d8a\u7b80\u5355\u8d8a\u53ef\u9760\u201d\u7684\u7406\u5ff5\uff0c\u575a\u6301\u751f\u547d\u79d1\u5b66\u548c\u79d1\u6280\u5143\u7d20\u7684\u6709\u673a\u878d\u5408\uff0c\u575a\u6301\u5728\u529f\u80fd\u548c\u5916\u89c2\u7684\u4e0d\u65ad\u53d6\u820d\u4e2d\u5bfb\u6c42\u5e73\u8861\uff1a\u91c7\u7528\u6a21\u4eff\u771f\u5b9e\u56db\u8db3\u54fa\u4e73\u52a8\u7269\u817f\u90e8\u6570\u5b66\u6a21\u578b\u3001\u91c7\u7528\u50a8\u80fd\u5143\u4ef6\u6a21\u4eff\u771f\u5b9e\u8ddf\u8171\u3001\u5c06\u6240\u6709\u7684\u4f20\u611f\u4e0e\u8ba1\u7b97\u96c6\u6210\u4e8e\u54ee\u5929\u5934\u90e8\u6a21\u4eff\u5927\u8111\u76ae\u5c42\u3001\u6240\u6709\u6267\u884c\u5668\u50cf\u795e\u7ecf\u4e2d\u67a2\u4e00\u6837\u8fde\u63a5\u5230\u5934\u90e8\u3001\u91c7\u7528\u4ece\u4e00\u800c\u7ec8\u7684\u5408\u91d1\u63d0\u5347\u4ea7\u54c1\u8d28\u611f\u3002\u5728\u6b64\uff0c\u6211\u4eec\u4e5f\u975e\u5e38\u9ad8\u5174\u80fd\u591f\u4e0e\u60a8\u4e00\u540c\u5206\u4eab\u6211\u4eec\u7684\u76ee\u6807\uff1a\u6052\u4e4b\u672a\u6765\u81f4\u529b\u4e8e\u4ee5\u673a\u5668\u4eba\u4e0e\u4eba\u5de5\u667a\u80fd\u6280\u672f\u4e3a\u6838\u5fc3\uff0c\u52a9\u529b\u4eba\u7c7b\u63a2\u7d22\u5e76\u89e3\u51b3\u751f\u547d\u79d1\u5b66\u95ee\u9898\u3002\u6211\u4eec\u5e0c\u671b\uff0c SPARKY \u53ef\u4ee5\u6210\u4e3a\u60a8\u5f97\u529b\u7684\u5f00\u53d1\u5e73\u53f0\uff0c\u8d4b\u4e88\u673a\u5668\u4eba\u50cf\u662f\u771f\u5b9e\u72d7\u72d7\u4e00\u6837\u7684\u8fd0\u52a8\u80fd\u529b\u3002"}),"\n",(0,s.jsx)(t.p,{children:"\u968f\u7740\u6280\u672f\u7684\u4e0d\u65ad\u53d1\u5c55\uff0c\u751f\u547d\u4f53\u4e0e\u673a\u5668\u7684\u878d\u5408\u53d8\u5f97\u4e0d\u518d\u9065\u8fdc\u3002\u6211\u4eec\u9700\u8981\u66f4\u591a\u4eba\u53c2\u4e0e\u8fdb\u6765\uff0c\u4f60\u4eec\u63d0\u51fa\u7684\u6bcf\u4e00\u4e2a\u521b\u610f\u548c\u60f3\u6cd5\u90fd\u662f\u63a8\u52a8\u6211\u4eec\u5411\u524d\u8fc8\u8fdb\u7684\u52a8\u529b\u3002\u4f5c\u4e3a\u6211\u4eec\u6700\u5b9d\u8d35\u7684\u65e9\u671f\u5408\u4f5c\u4f19\u4f34\uff0c\u968f\u7bb1\u9644\u9001HENGBOT\u4e3a\u60a8\u51c6\u5907\u7684\u5177\u6709\u552f\u4e00\u7f16\u53f7\u7684VIP \u5361\u4e00\u5f20\uff0c\u6b64\u5361\u5c06\u4f5c\u4e3a HENGBOT \u540e\u7eed\u4ea7\u54c1\u5185\u6d4b\u3001\u4ea7\u54c1\u6df1\u5ea6\u5b9a\u5236\u3001\u4ea7\u54c1\u53d1\u5e03\u4f1a\u7b49\u5168\u90e8\u6d3b\u52a8\u7684\u5165\u573a\u5238\uff0c\u8fd8\u8bf7\u59a5\u5584\u4fdd\u7ba1\u3002\u540c\u65f6\uff0c\u4e3a\u66f4\u597d\u7684\u6c9f\u901a\u4e0e\u4ea4\u6d41\uff0c\u671f\u5f85\u60a8\u901a\u8fc7\u4e0b\u65b9\u4e8c\u7ef4\u7801\u6dfb\u52a0\u5c0f\u52a9\u624b\u5fae\u4fe1\u5e76\u52a0\u5165\u5b98\u65b9\u793e\u7fa4\u4e0e\u6211\u4eec\u76f8\u4f1a\u3002"}),"\n",(0,s.jsx)(t.p,{children:"\u518d\u6b21\u8877\u5fc3\u611f\u8c22\u4f60\u4eec\u5bf9 SPARKY \u4ee5\u53ca HENGBOT \u7684\u652f\u6301\u548c\u4fe1\u4efb\uff01"}),"\n",(0,s.jsx)(t.p,{children:"\u6700\u8bda\u631a\u7684\u95ee\u5019\uff0c\nHENGBOT TEAM"})]})}function p(e={}){const{wrapper:t}={...(0,r.R)(),...e.components};return t?(0,s.jsx)(t,{...e,children:(0,s.jsx)(u,{...e})}):u(e)}},8453:(e,t,n)=>{n.d(t,{R:()=>o,x:()=>c});var s=n(6540);const r={},a=s.createContext(r);function o(e){const t=s.useContext(a);return s.useMemo((function(){return"function"==typeof e?e(t):{...t,...e}}),[t,e])}function c(e){let t;return t=e.disableParentContext?"function"==typeof e.components?e.components(r):e.components||r:o(e.components),s.createElement(a.Provider,{value:t},e.children)}}}]);