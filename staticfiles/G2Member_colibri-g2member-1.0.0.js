(function(J){typeof define=="function"&&define.amd?define(J):J()})(function(){"use strict";/*! colibri-g2member - v1.0.0 *//**
 * @license
 * Copyright 2019 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */var mi;const J=globalThis,Ve=J.ShadowRoot&&(J.ShadyCSS===void 0||J.ShadyCSS.nativeShadow)&&"adoptedStyleSheets"in Document.prototype&&"replace"in CSSStyleSheet.prototype,Be=Symbol(),dt=new WeakMap;let ut=class{constructor(e,i,o){if(this._$cssResult$=!0,o!==Be)throw Error("CSSResult is not constructable. Use `unsafeCSS` or `css` instead.");this.cssText=e,this.t=i}get styleSheet(){let e=this.o;const i=this.t;if(Ve&&e===void 0){const o=i!==void 0&&i.length===1;o&&(e=dt.get(i)),e===void 0&&((this.o=e=new CSSStyleSheet).replaceSync(this.cssText),o&&dt.set(i,e))}return e}toString(){return this.cssText}};const gi=t=>new ut(typeof t=="string"?t:t+"",void 0,Be),ne=(t,...e)=>{const i=t.length===1?t[0]:e.reduce((o,n,s)=>o+(r=>{if(r._$cssResult$===!0)return r.cssText;if(typeof r=="number")return r;throw Error("Value passed to 'css' function must be a 'css' function result: "+r+". Use 'unsafeCSS' to pass non-literal values, but take care to ensure page security.")})(n)+t[s+1],t[0]);return new ut(i,t,Be)},bi=(t,e)=>{if(Ve)t.adoptedStyleSheets=e.map(i=>i instanceof CSSStyleSheet?i:i.styleSheet);else for(const i of e){const o=document.createElement("style"),n=J.litNonce;n!==void 0&&o.setAttribute("nonce",n),o.textContent=i.cssText,t.appendChild(o)}},ht=Ve?t=>t:t=>t instanceof CSSStyleSheet?(e=>{let i="";for(const o of e.cssRules)i+=o.cssText;return gi(i)})(t):t;/**
 * @license
 * Copyright 2017 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */const{is:yi,defineProperty:vi,getOwnPropertyDescriptor:xi,getOwnPropertyNames:$i,getOwnPropertySymbols:wi,getPrototypeOf:Ci}=Object,H=globalThis,pt=H.trustedTypes,Di=pt?pt.emptyScript:"",He=H.reactiveElementPolyfillSupport,ce=(t,e)=>t,$e={toAttribute(t,e){switch(e){case Boolean:t=t?Di:null;break;case Object:case Array:t=t==null?t:JSON.stringify(t)}return t},fromAttribute(t,e){let i=t;switch(e){case Boolean:i=t!==null;break;case Number:i=t===null?null:Number(t);break;case Object:case Array:try{i=JSON.parse(t)}catch{i=null}}return i}},Ge=(t,e)=>!yi(t,e),mt={attribute:!0,type:String,converter:$e,reflect:!1,hasChanged:Ge};Symbol.metadata??(Symbol.metadata=Symbol("metadata")),H.litPropertyMetadata??(H.litPropertyMetadata=new WeakMap);class se extends HTMLElement{static addInitializer(e){this._$Ei(),(this.l??(this.l=[])).push(e)}static get observedAttributes(){return this.finalize(),this._$Eh&&[...this._$Eh.keys()]}static createProperty(e,i=mt){if(i.state&&(i.attribute=!1),this._$Ei(),this.elementProperties.set(e,i),!i.noAccessor){const o=Symbol(),n=this.getPropertyDescriptor(e,o,i);n!==void 0&&vi(this.prototype,e,n)}}static getPropertyDescriptor(e,i,o){const{get:n,set:s}=xi(this.prototype,e)??{get(){return this[i]},set(r){this[i]=r}};return{get(){return n==null?void 0:n.call(this)},set(r){const a=n==null?void 0:n.call(this);s.call(this,r),this.requestUpdate(e,a,o)},configurable:!0,enumerable:!0}}static getPropertyOptions(e){return this.elementProperties.get(e)??mt}static _$Ei(){if(this.hasOwnProperty(ce("elementProperties")))return;const e=Ci(this);e.finalize(),e.l!==void 0&&(this.l=[...e.l]),this.elementProperties=new Map(e.elementProperties)}static finalize(){if(this.hasOwnProperty(ce("finalized")))return;if(this.finalized=!0,this._$Ei(),this.hasOwnProperty(ce("properties"))){const i=this.properties,o=[...$i(i),...wi(i)];for(const n of o)this.createProperty(n,i[n])}const e=this[Symbol.metadata];if(e!==null){const i=litPropertyMetadata.get(e);if(i!==void 0)for(const[o,n]of i)this.elementProperties.set(o,n)}this._$Eh=new Map;for(const[i,o]of this.elementProperties){const n=this._$Eu(i,o);n!==void 0&&this._$Eh.set(n,i)}this.elementStyles=this.finalizeStyles(this.styles)}static finalizeStyles(e){const i=[];if(Array.isArray(e)){const o=new Set(e.flat(1/0).reverse());for(const n of o)i.unshift(ht(n))}else e!==void 0&&i.push(ht(e));return i}static _$Eu(e,i){const o=i.attribute;return o===!1?void 0:typeof o=="string"?o:typeof e=="string"?e.toLowerCase():void 0}constructor(){super(),this._$Ep=void 0,this.isUpdatePending=!1,this.hasUpdated=!1,this._$Em=null,this._$Ev()}_$Ev(){var e;this._$ES=new Promise(i=>this.enableUpdating=i),this._$AL=new Map,this._$E_(),this.requestUpdate(),(e=this.constructor.l)==null||e.forEach(i=>i(this))}addController(e){var i;(this._$EO??(this._$EO=new Set)).add(e),this.renderRoot!==void 0&&this.isConnected&&((i=e.hostConnected)==null||i.call(e))}removeController(e){var i;(i=this._$EO)==null||i.delete(e)}_$E_(){const e=new Map,i=this.constructor.elementProperties;for(const o of i.keys())this.hasOwnProperty(o)&&(e.set(o,this[o]),delete this[o]);e.size>0&&(this._$Ep=e)}createRenderRoot(){const e=this.shadowRoot??this.attachShadow(this.constructor.shadowRootOptions);return bi(e,this.constructor.elementStyles),e}connectedCallback(){var e;this.renderRoot??(this.renderRoot=this.createRenderRoot()),this.enableUpdating(!0),(e=this._$EO)==null||e.forEach(i=>{var o;return(o=i.hostConnected)==null?void 0:o.call(i)})}enableUpdating(e){}disconnectedCallback(){var e;(e=this._$EO)==null||e.forEach(i=>{var o;return(o=i.hostDisconnected)==null?void 0:o.call(i)})}attributeChangedCallback(e,i,o){this._$AK(e,o)}_$EC(e,i){var s;const o=this.constructor.elementProperties.get(e),n=this.constructor._$Eu(e,o);if(n!==void 0&&o.reflect===!0){const r=(((s=o.converter)==null?void 0:s.toAttribute)!==void 0?o.converter:$e).toAttribute(i,o.type);this._$Em=e,r==null?this.removeAttribute(n):this.setAttribute(n,r),this._$Em=null}}_$AK(e,i){var s;const o=this.constructor,n=o._$Eh.get(e);if(n!==void 0&&this._$Em!==n){const r=o.getPropertyOptions(n),a=typeof r.converter=="function"?{fromAttribute:r.converter}:((s=r.converter)==null?void 0:s.fromAttribute)!==void 0?r.converter:$e;this._$Em=n,this[n]=a.fromAttribute(i,r.type),this._$Em=null}}requestUpdate(e,i,o){if(e!==void 0){if(o??(o=this.constructor.getPropertyOptions(e)),!(o.hasChanged??Ge)(this[e],i))return;this.P(e,i,o)}this.isUpdatePending===!1&&(this._$ES=this._$ET())}P(e,i,o){this._$AL.has(e)||this._$AL.set(e,i),o.reflect===!0&&this._$Em!==e&&(this._$Ej??(this._$Ej=new Set)).add(e)}async _$ET(){this.isUpdatePending=!0;try{await this._$ES}catch(i){Promise.reject(i)}const e=this.scheduleUpdate();return e!=null&&await e,!this.isUpdatePending}scheduleUpdate(){return this.performUpdate()}performUpdate(){var o;if(!this.isUpdatePending)return;if(!this.hasUpdated){if(this.renderRoot??(this.renderRoot=this.createRenderRoot()),this._$Ep){for(const[s,r]of this._$Ep)this[s]=r;this._$Ep=void 0}const n=this.constructor.elementProperties;if(n.size>0)for(const[s,r]of n)r.wrapped!==!0||this._$AL.has(s)||this[s]===void 0||this.P(s,this[s],r)}let e=!1;const i=this._$AL;try{e=this.shouldUpdate(i),e?(this.willUpdate(i),(o=this._$EO)==null||o.forEach(n=>{var s;return(s=n.hostUpdate)==null?void 0:s.call(n)}),this.update(i)):this._$EU()}catch(n){throw e=!1,this._$EU(),n}e&&this._$AE(i)}willUpdate(e){}_$AE(e){var i;(i=this._$EO)==null||i.forEach(o=>{var n;return(n=o.hostUpdated)==null?void 0:n.call(o)}),this.hasUpdated||(this.hasUpdated=!0,this.firstUpdated(e)),this.updated(e)}_$EU(){this._$AL=new Map,this.isUpdatePending=!1}get updateComplete(){return this.getUpdateComplete()}getUpdateComplete(){return this._$ES}shouldUpdate(e){return!0}update(e){this._$Ej&&(this._$Ej=this._$Ej.forEach(i=>this._$EC(i,this[i]))),this._$EU()}updated(e){}firstUpdated(e){}}se.elementStyles=[],se.shadowRootOptions={mode:"open"},se[ce("elementProperties")]=new Map,se[ce("finalized")]=new Map,He==null||He({ReactiveElement:se}),(H.reactiveElementVersions??(H.reactiveElementVersions=[])).push("2.0.4");/**
 * @license
 * Copyright 2017 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */const de=globalThis,we=de.trustedTypes,ft=we?we.createPolicy("lit-html",{createHTML:t=>t}):void 0,gt="$lit$",G=`lit$${Math.random().toFixed(9).slice(2)}$`,bt="?"+G,Ei=`<${bt}>`,Q=document,ue=()=>Q.createComment(""),he=t=>t===null||typeof t!="object"&&typeof t!="function",je=Array.isArray,Pi=t=>je(t)||typeof(t==null?void 0:t[Symbol.iterator])=="function",qe=`[ 	
\f\r]`,pe=/<(?:(!--|\/[^a-zA-Z])|(\/?[a-zA-Z][^>\s]*)|(\/?$))/g,yt=/-->/g,vt=/>/g,K=RegExp(`>|${qe}(?:([^\\s"'>=/]+)(${qe}*=${qe}*(?:[^ 	
\f\r"'\`<>=]|("|')|))|$)`,"g"),xt=/'/g,$t=/"/g,wt=/^(?:script|style|textarea|title)$/i,Si=t=>(e,...i)=>({_$litType$:t,strings:e,values:i}),p=Si(1),Z=Symbol.for("lit-noChange"),D=Symbol.for("lit-nothing"),Ct=new WeakMap,X=Q.createTreeWalker(Q,129);function Dt(t,e){if(!je(t)||!t.hasOwnProperty("raw"))throw Error("invalid template strings array");return ft!==void 0?ft.createHTML(e):e}const Li=(t,e)=>{const i=t.length-1,o=[];let n,s=e===2?"<svg>":e===3?"<math>":"",r=pe;for(let a=0;a<i;a++){const c=t[a];let d,u,h=-1,v=0;for(;v<c.length&&(r.lastIndex=v,u=r.exec(c),u!==null);)v=r.lastIndex,r===pe?u[1]==="!--"?r=yt:u[1]!==void 0?r=vt:u[2]!==void 0?(wt.test(u[2])&&(n=RegExp("</"+u[2],"g")),r=K):u[3]!==void 0&&(r=K):r===K?u[0]===">"?(r=n??pe,h=-1):u[1]===void 0?h=-2:(h=r.lastIndex-u[2].length,d=u[1],r=u[3]===void 0?K:u[3]==='"'?$t:xt):r===$t||r===xt?r=K:r===yt||r===vt?r=pe:(r=K,n=void 0);const x=r===K&&t[a+1].startsWith("/>")?" ":"";s+=r===pe?c+Ei:h>=0?(o.push(d),c.slice(0,h)+gt+c.slice(h)+G+x):c+G+(h===-2?a:x)}return[Dt(t,s+(t[i]||"<?>")+(e===2?"</svg>":e===3?"</math>":"")),o]};class me{constructor({strings:e,_$litType$:i},o){let n;this.parts=[];let s=0,r=0;const a=e.length-1,c=this.parts,[d,u]=Li(e,i);if(this.el=me.createElement(d,o),X.currentNode=this.el.content,i===2||i===3){const h=this.el.content.firstChild;h.replaceWith(...h.childNodes)}for(;(n=X.nextNode())!==null&&c.length<a;){if(n.nodeType===1){if(n.hasAttributes())for(const h of n.getAttributeNames())if(h.endsWith(gt)){const v=u[r++],x=n.getAttribute(h).split(G),m=/([.?@])?(.*)/.exec(v);c.push({type:1,index:s,name:m[2],strings:x,ctor:m[1]==="."?Ti:m[1]==="?"?Ai:m[1]==="@"?Oi:Ce}),n.removeAttribute(h)}else h.startsWith(G)&&(c.push({type:6,index:s}),n.removeAttribute(h));if(wt.test(n.tagName)){const h=n.textContent.split(G),v=h.length-1;if(v>0){n.textContent=we?we.emptyScript:"";for(let x=0;x<v;x++)n.append(h[x],ue()),X.nextNode(),c.push({type:2,index:++s});n.append(h[v],ue())}}}else if(n.nodeType===8)if(n.data===bt)c.push({type:2,index:s});else{let h=-1;for(;(h=n.data.indexOf(G,h+1))!==-1;)c.push({type:7,index:s}),h+=G.length-1}s++}}static createElement(e,i){const o=Q.createElement("template");return o.innerHTML=e,o}}function re(t,e,i=t,o){var r,a;if(e===Z)return e;let n=o!==void 0?(r=i._$Co)==null?void 0:r[o]:i._$Cl;const s=he(e)?void 0:e._$litDirective$;return(n==null?void 0:n.constructor)!==s&&((a=n==null?void 0:n._$AO)==null||a.call(n,!1),s===void 0?n=void 0:(n=new s(t),n._$AT(t,i,o)),o!==void 0?(i._$Co??(i._$Co=[]))[o]=n:i._$Cl=n),n!==void 0&&(e=re(t,n._$AS(t,e.values),n,o)),e}class Ri{constructor(e,i){this._$AV=[],this._$AN=void 0,this._$AD=e,this._$AM=i}get parentNode(){return this._$AM.parentNode}get _$AU(){return this._$AM._$AU}u(e){const{el:{content:i},parts:o}=this._$AD,n=((e==null?void 0:e.creationScope)??Q).importNode(i,!0);X.currentNode=n;let s=X.nextNode(),r=0,a=0,c=o[0];for(;c!==void 0;){if(r===c.index){let d;c.type===2?d=new fe(s,s.nextSibling,this,e):c.type===1?d=new c.ctor(s,c.name,c.strings,this,e):c.type===6&&(d=new Ni(s,this,e)),this._$AV.push(d),c=o[++a]}r!==(c==null?void 0:c.index)&&(s=X.nextNode(),r++)}return X.currentNode=Q,n}p(e){let i=0;for(const o of this._$AV)o!==void 0&&(o.strings!==void 0?(o._$AI(e,o,i),i+=o.strings.length-2):o._$AI(e[i])),i++}}class fe{get _$AU(){var e;return((e=this._$AM)==null?void 0:e._$AU)??this._$Cv}constructor(e,i,o,n){this.type=2,this._$AH=D,this._$AN=void 0,this._$AA=e,this._$AB=i,this._$AM=o,this.options=n,this._$Cv=(n==null?void 0:n.isConnected)??!0}get parentNode(){let e=this._$AA.parentNode;const i=this._$AM;return i!==void 0&&(e==null?void 0:e.nodeType)===11&&(e=i.parentNode),e}get startNode(){return this._$AA}get endNode(){return this._$AB}_$AI(e,i=this){e=re(this,e,i),he(e)?e===D||e==null||e===""?(this._$AH!==D&&this._$AR(),this._$AH=D):e!==this._$AH&&e!==Z&&this._(e):e._$litType$!==void 0?this.$(e):e.nodeType!==void 0?this.T(e):Pi(e)?this.k(e):this._(e)}O(e){return this._$AA.parentNode.insertBefore(e,this._$AB)}T(e){this._$AH!==e&&(this._$AR(),this._$AH=this.O(e))}_(e){this._$AH!==D&&he(this._$AH)?this._$AA.nextSibling.data=e:this.T(Q.createTextNode(e)),this._$AH=e}$(e){var s;const{values:i,_$litType$:o}=e,n=typeof o=="number"?this._$AC(e):(o.el===void 0&&(o.el=me.createElement(Dt(o.h,o.h[0]),this.options)),o);if(((s=this._$AH)==null?void 0:s._$AD)===n)this._$AH.p(i);else{const r=new Ri(n,this),a=r.u(this.options);r.p(i),this.T(a),this._$AH=r}}_$AC(e){let i=Ct.get(e.strings);return i===void 0&&Ct.set(e.strings,i=new me(e)),i}k(e){je(this._$AH)||(this._$AH=[],this._$AR());const i=this._$AH;let o,n=0;for(const s of e)n===i.length?i.push(o=new fe(this.O(ue()),this.O(ue()),this,this.options)):o=i[n],o._$AI(s),n++;n<i.length&&(this._$AR(o&&o._$AB.nextSibling,n),i.length=n)}_$AR(e=this._$AA.nextSibling,i){var o;for((o=this._$AP)==null?void 0:o.call(this,!1,!0,i);e&&e!==this._$AB;){const n=e.nextSibling;e.remove(),e=n}}setConnected(e){var i;this._$AM===void 0&&(this._$Cv=e,(i=this._$AP)==null||i.call(this,e))}}class Ce{get tagName(){return this.element.tagName}get _$AU(){return this._$AM._$AU}constructor(e,i,o,n,s){this.type=1,this._$AH=D,this._$AN=void 0,this.element=e,this.name=i,this._$AM=n,this.options=s,o.length>2||o[0]!==""||o[1]!==""?(this._$AH=Array(o.length-1).fill(new String),this.strings=o):this._$AH=D}_$AI(e,i=this,o,n){const s=this.strings;let r=!1;if(s===void 0)e=re(this,e,i,0),r=!he(e)||e!==this._$AH&&e!==Z,r&&(this._$AH=e);else{const a=e;let c,d;for(e=s[0],c=0;c<s.length-1;c++)d=re(this,a[o+c],i,c),d===Z&&(d=this._$AH[c]),r||(r=!he(d)||d!==this._$AH[c]),d===D?e=D:e!==D&&(e+=(d??"")+s[c+1]),this._$AH[c]=d}r&&!n&&this.j(e)}j(e){e===D?this.element.removeAttribute(this.name):this.element.setAttribute(this.name,e??"")}}class Ti extends Ce{constructor(){super(...arguments),this.type=3}j(e){this.element[this.name]=e===D?void 0:e}}class Ai extends Ce{constructor(){super(...arguments),this.type=4}j(e){this.element.toggleAttribute(this.name,!!e&&e!==D)}}class Oi extends Ce{constructor(e,i,o,n,s){super(e,i,o,n,s),this.type=5}_$AI(e,i=this){if((e=re(this,e,i,0)??D)===Z)return;const o=this._$AH,n=e===D&&o!==D||e.capture!==o.capture||e.once!==o.once||e.passive!==o.passive,s=e!==D&&(o===D||n);n&&this.element.removeEventListener(this.name,this,o),s&&this.element.addEventListener(this.name,this,e),this._$AH=e}handleEvent(e){var i;typeof this._$AH=="function"?this._$AH.call(((i=this.options)==null?void 0:i.host)??this.element,e):this._$AH.handleEvent(e)}}class Ni{constructor(e,i,o){this.element=e,this.type=6,this._$AN=void 0,this._$AM=i,this.options=o}get _$AU(){return this._$AM._$AU}_$AI(e){re(this,e)}}const We=de.litHtmlPolyfillSupport;We==null||We(me,fe),(de.litHtmlVersions??(de.litHtmlVersions=[])).push("3.2.1");const Et=(t,e,i)=>{const o=(i==null?void 0:i.renderBefore)??e;let n=o._$litPart$;if(n===void 0){const s=(i==null?void 0:i.renderBefore)??null;o._$litPart$=n=new fe(e.insertBefore(ue(),s),s,void 0,i??{})}return n._$AI(t),n};/**
 * @license
 * Copyright 2017 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */let j=class extends se{constructor(){super(...arguments),this.renderOptions={host:this},this._$Do=void 0}createRenderRoot(){var i;const e=super.createRenderRoot();return(i=this.renderOptions).renderBefore??(i.renderBefore=e.firstChild),e}update(e){const i=this.render();this.hasUpdated||(this.renderOptions.isConnected=this.isConnected),super.update(e),this._$Do=Et(i,this.renderRoot,this.renderOptions)}connectedCallback(){var e;super.connectedCallback(),(e=this._$Do)==null||e.setConnected(!0)}disconnectedCallback(){var e;super.disconnectedCallback(),(e=this._$Do)==null||e.setConnected(!1)}render(){return Z}};j._$litElement$=!0,j.finalized=!0,(mi=globalThis.litElementHydrateSupport)==null||mi.call(globalThis,{LitElement:j});const Je=globalThis.litElementPolyfillSupport;Je==null||Je({LitElement:j}),(globalThis.litElementVersions??(globalThis.litElementVersions=[])).push("4.1.1");/**
 * @license
 * Copyright 2017 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */const De=t=>(e,i)=>{i!==void 0?i.addInitializer(()=>{customElements.define(t,e)}):customElements.define(t,e)};/**
 * @license
 * Copyright 2017 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */const _i={attribute:!0,type:String,converter:$e,reflect:!1,hasChanged:Ge},ki=(t=_i,e,i)=>{const{kind:o,metadata:n}=i;let s=globalThis.litPropertyMetadata.get(n);if(s===void 0&&globalThis.litPropertyMetadata.set(n,s=new Map),s.set(i.name,t),o==="accessor"){const{name:r}=i;return{set(a){const c=e.get.call(this);e.set.call(this,a),this.requestUpdate(r,c,t)},init(a){return a!==void 0&&this.P(r,void 0,t),a}}}if(o==="setter"){const{name:r}=i;return function(a){const c=this[r];e.call(this,a),this.requestUpdate(r,c,t)}}throw Error("Unsupported decorator location: "+o)};function M(t){return(e,i)=>typeof i=="object"?ki(t,e,i):((o,n,s)=>{const r=n.hasOwnProperty(s);return n.constructor.createProperty(s,r?{...o,wrapped:!0}:o),r?Object.getOwnPropertyDescriptor(n,s):void 0})(t,e,i)}/**
 * @license
 * Copyright 2017 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */function g(t){return M({...t,state:!0,attribute:!1})}function Pt(t,e){return function(){return t.apply(e,arguments)}}const{toString:Ii}=Object.prototype,{getPrototypeOf:Qe}=Object,Ee=(t=>e=>{const i=Ii.call(e);return t[i]||(t[i]=i.slice(8,-1).toLowerCase())})(Object.create(null)),F=t=>(t=t.toLowerCase(),e=>Ee(e)===t),Pe=t=>e=>typeof e===t,{isArray:ae}=Array,ge=Pe("undefined");function Fi(t){return t!==null&&!ge(t)&&t.constructor!==null&&!ge(t.constructor)&&_(t.constructor.isBuffer)&&t.constructor.isBuffer(t)}const St=F("ArrayBuffer");function Mi(t){let e;return typeof ArrayBuffer<"u"&&ArrayBuffer.isView?e=ArrayBuffer.isView(t):e=t&&t.buffer&&St(t.buffer),e}const Ui=Pe("string"),_=Pe("function"),Lt=Pe("number"),Se=t=>t!==null&&typeof t=="object",zi=t=>t===!0||t===!1,Le=t=>{if(Ee(t)!=="object")return!1;const e=Qe(t);return(e===null||e===Object.prototype||Object.getPrototypeOf(e)===null)&&!(Symbol.toStringTag in t)&&!(Symbol.iterator in t)},Vi=F("Date"),Bi=F("File"),Hi=F("Blob"),Gi=F("FileList"),ji=t=>Se(t)&&_(t.pipe),qi=t=>{let e;return t&&(typeof FormData=="function"&&t instanceof FormData||_(t.append)&&((e=Ee(t))==="formdata"||e==="object"&&_(t.toString)&&t.toString()==="[object FormData]"))},Wi=F("URLSearchParams"),[Ji,Qi,Ki,Zi]=["ReadableStream","Request","Response","Headers"].map(F),Xi=t=>t.trim?t.trim():t.replace(/^[\s\uFEFF\xA0]+|[\s\uFEFF\xA0]+$/g,"");function be(t,e,{allOwnKeys:i=!1}={}){if(t===null||typeof t>"u")return;let o,n;if(typeof t!="object"&&(t=[t]),ae(t))for(o=0,n=t.length;o<n;o++)e.call(null,t[o],o,t);else{const s=i?Object.getOwnPropertyNames(t):Object.keys(t),r=s.length;let a;for(o=0;o<r;o++)a=s[o],e.call(null,t[a],a,t)}}function Rt(t,e){e=e.toLowerCase();const i=Object.keys(t);let o=i.length,n;for(;o-- >0;)if(n=i[o],e===n.toLowerCase())return n;return null}const Y=typeof globalThis<"u"?globalThis:typeof self<"u"?self:typeof window<"u"?window:global,Tt=t=>!ge(t)&&t!==Y;function Ke(){const{caseless:t}=Tt(this)&&this||{},e={},i=(o,n)=>{const s=t&&Rt(e,n)||n;Le(e[s])&&Le(o)?e[s]=Ke(e[s],o):Le(o)?e[s]=Ke({},o):ae(o)?e[s]=o.slice():e[s]=o};for(let o=0,n=arguments.length;o<n;o++)arguments[o]&&be(arguments[o],i);return e}const Yi=(t,e,i,{allOwnKeys:o}={})=>(be(e,(n,s)=>{i&&_(n)?t[s]=Pt(n,i):t[s]=n},{allOwnKeys:o}),t),eo=t=>(t.charCodeAt(0)===65279&&(t=t.slice(1)),t),to=(t,e,i,o)=>{t.prototype=Object.create(e.prototype,o),t.prototype.constructor=t,Object.defineProperty(t,"super",{value:e.prototype}),i&&Object.assign(t.prototype,i)},io=(t,e,i,o)=>{let n,s,r;const a={};if(e=e||{},t==null)return e;do{for(n=Object.getOwnPropertyNames(t),s=n.length;s-- >0;)r=n[s],(!o||o(r,t,e))&&!a[r]&&(e[r]=t[r],a[r]=!0);t=i!==!1&&Qe(t)}while(t&&(!i||i(t,e))&&t!==Object.prototype);return e},oo=(t,e,i)=>{t=String(t),(i===void 0||i>t.length)&&(i=t.length),i-=e.length;const o=t.indexOf(e,i);return o!==-1&&o===i},no=t=>{if(!t)return null;if(ae(t))return t;let e=t.length;if(!Lt(e))return null;const i=new Array(e);for(;e-- >0;)i[e]=t[e];return i},so=(t=>e=>t&&e instanceof t)(typeof Uint8Array<"u"&&Qe(Uint8Array)),ro=(t,e)=>{const o=(t&&t[Symbol.iterator]).call(t);let n;for(;(n=o.next())&&!n.done;){const s=n.value;e.call(t,s[0],s[1])}},ao=(t,e)=>{let i;const o=[];for(;(i=t.exec(e))!==null;)o.push(i);return o},lo=F("HTMLFormElement"),co=t=>t.toLowerCase().replace(/[-_\s]([a-z\d])(\w*)/g,function(i,o,n){return o.toUpperCase()+n}),At=(({hasOwnProperty:t})=>(e,i)=>t.call(e,i))(Object.prototype),uo=F("RegExp"),Ot=(t,e)=>{const i=Object.getOwnPropertyDescriptors(t),o={};be(i,(n,s)=>{let r;(r=e(n,s,t))!==!1&&(o[s]=r||n)}),Object.defineProperties(t,o)},ho=t=>{Ot(t,(e,i)=>{if(_(t)&&["arguments","caller","callee"].indexOf(i)!==-1)return!1;const o=t[i];if(_(o)){if(e.enumerable=!1,"writable"in e){e.writable=!1;return}e.set||(e.set=()=>{throw Error("Can not rewrite read-only method '"+i+"'")})}})},po=(t,e)=>{const i={},o=n=>{n.forEach(s=>{i[s]=!0})};return ae(t)?o(t):o(String(t).split(e)),i},mo=()=>{},fo=(t,e)=>t!=null&&Number.isFinite(t=+t)?t:e,Ze="abcdefghijklmnopqrstuvwxyz",Nt="0123456789",_t={DIGIT:Nt,ALPHA:Ze,ALPHA_DIGIT:Ze+Ze.toUpperCase()+Nt},go=(t=16,e=_t.ALPHA_DIGIT)=>{let i="";const{length:o}=e;for(;t--;)i+=e[Math.random()*o|0];return i};function bo(t){return!!(t&&_(t.append)&&t[Symbol.toStringTag]==="FormData"&&t[Symbol.iterator])}const yo=t=>{const e=new Array(10),i=(o,n)=>{if(Se(o)){if(e.indexOf(o)>=0)return;if(!("toJSON"in o)){e[n]=o;const s=ae(o)?[]:{};return be(o,(r,a)=>{const c=i(r,n+1);!ge(c)&&(s[a]=c)}),e[n]=void 0,s}}return o};return i(t,0)},vo=F("AsyncFunction"),xo=t=>t&&(Se(t)||_(t))&&_(t.then)&&_(t.catch),kt=((t,e)=>t?setImmediate:e?((i,o)=>(Y.addEventListener("message",({source:n,data:s})=>{n===Y&&s===i&&o.length&&o.shift()()},!1),n=>{o.push(n),Y.postMessage(i,"*")}))(`axios@${Math.random()}`,[]):i=>setTimeout(i))(typeof setImmediate=="function",_(Y.postMessage)),$o=typeof queueMicrotask<"u"?queueMicrotask.bind(Y):typeof process<"u"&&process.nextTick||kt,l={isArray:ae,isArrayBuffer:St,isBuffer:Fi,isFormData:qi,isArrayBufferView:Mi,isString:Ui,isNumber:Lt,isBoolean:zi,isObject:Se,isPlainObject:Le,isReadableStream:Ji,isRequest:Qi,isResponse:Ki,isHeaders:Zi,isUndefined:ge,isDate:Vi,isFile:Bi,isBlob:Hi,isRegExp:uo,isFunction:_,isStream:ji,isURLSearchParams:Wi,isTypedArray:so,isFileList:Gi,forEach:be,merge:Ke,extend:Yi,trim:Xi,stripBOM:eo,inherits:to,toFlatObject:io,kindOf:Ee,kindOfTest:F,endsWith:oo,toArray:no,forEachEntry:ro,matchAll:ao,isHTMLForm:lo,hasOwnProperty:At,hasOwnProp:At,reduceDescriptors:Ot,freezeMethods:ho,toObjectSet:po,toCamelCase:co,noop:mo,toFiniteNumber:fo,findKey:Rt,global:Y,isContextDefined:Tt,ALPHABET:_t,generateString:go,isSpecCompliantForm:bo,toJSONObject:yo,isAsyncFn:vo,isThenable:xo,setImmediate:kt,asap:$o};function b(t,e,i,o,n){Error.call(this),Error.captureStackTrace?Error.captureStackTrace(this,this.constructor):this.stack=new Error().stack,this.message=t,this.name="AxiosError",e&&(this.code=e),i&&(this.config=i),o&&(this.request=o),n&&(this.response=n,this.status=n.status?n.status:null)}l.inherits(b,Error,{toJSON:function(){return{message:this.message,name:this.name,description:this.description,number:this.number,fileName:this.fileName,lineNumber:this.lineNumber,columnNumber:this.columnNumber,stack:this.stack,config:l.toJSONObject(this.config),code:this.code,status:this.status}}});const It=b.prototype,Ft={};["ERR_BAD_OPTION_VALUE","ERR_BAD_OPTION","ECONNABORTED","ETIMEDOUT","ERR_NETWORK","ERR_FR_TOO_MANY_REDIRECTS","ERR_DEPRECATED","ERR_BAD_RESPONSE","ERR_BAD_REQUEST","ERR_CANCELED","ERR_NOT_SUPPORT","ERR_INVALID_URL"].forEach(t=>{Ft[t]={value:t}}),Object.defineProperties(b,Ft),Object.defineProperty(It,"isAxiosError",{value:!0}),b.from=(t,e,i,o,n,s)=>{const r=Object.create(It);return l.toFlatObject(t,r,function(c){return c!==Error.prototype},a=>a!=="isAxiosError"),b.call(r,t.message,e,i,o,n),r.cause=t,r.name=t.name,s&&Object.assign(r,s),r};const wo=null;function Xe(t){return l.isPlainObject(t)||l.isArray(t)}function Mt(t){return l.endsWith(t,"[]")?t.slice(0,-2):t}function Ut(t,e,i){return t?t.concat(e).map(function(n,s){return n=Mt(n),!i&&s?"["+n+"]":n}).join(i?".":""):e}function Co(t){return l.isArray(t)&&!t.some(Xe)}const Do=l.toFlatObject(l,{},null,function(e){return/^is[A-Z]/.test(e)});function Re(t,e,i){if(!l.isObject(t))throw new TypeError("target must be an object");e=e||new FormData,i=l.toFlatObject(i,{metaTokens:!0,dots:!1,indexes:!1},!1,function(y,f){return!l.isUndefined(f[y])});const o=i.metaTokens,n=i.visitor||u,s=i.dots,r=i.indexes,c=(i.Blob||typeof Blob<"u"&&Blob)&&l.isSpecCompliantForm(e);if(!l.isFunction(n))throw new TypeError("visitor must be a function");function d(m){if(m===null)return"";if(l.isDate(m))return m.toISOString();if(!c&&l.isBlob(m))throw new b("Blob is not supported. Use a Buffer instead.");return l.isArrayBuffer(m)||l.isTypedArray(m)?c&&typeof Blob=="function"?new Blob([m]):Buffer.from(m):m}function u(m,y,f){let C=m;if(m&&!f&&typeof m=="object"){if(l.endsWith(y,"{}"))y=o?y:y.slice(0,-2),m=JSON.stringify(m);else if(l.isArray(m)&&Co(m)||(l.isFileList(m)||l.endsWith(y,"[]"))&&(C=l.toArray(m)))return y=Mt(y),C.forEach(function(T,B){!(l.isUndefined(T)||T===null)&&e.append(r===!0?Ut([y],B,s):r===null?y:y+"[]",d(T))}),!1}return Xe(m)?!0:(e.append(Ut(f,y,s),d(m)),!1)}const h=[],v=Object.assign(Do,{defaultVisitor:u,convertValue:d,isVisitable:Xe});function x(m,y){if(!l.isUndefined(m)){if(h.indexOf(m)!==-1)throw Error("Circular reference detected in "+y.join("."));h.push(m),l.forEach(m,function(C,R){(!(l.isUndefined(C)||C===null)&&n.call(e,C,l.isString(R)?R.trim():R,y,v))===!0&&x(C,y?y.concat(R):[R])}),h.pop()}}if(!l.isObject(t))throw new TypeError("data must be an object");return x(t),e}function zt(t){const e={"!":"%21","'":"%27","(":"%28",")":"%29","~":"%7E","%20":"+","%00":"\0"};return encodeURIComponent(t).replace(/[!'()~]|%20|%00/g,function(o){return e[o]})}function Ye(t,e){this._pairs=[],t&&Re(t,this,e)}const Vt=Ye.prototype;Vt.append=function(e,i){this._pairs.push([e,i])},Vt.toString=function(e){const i=e?function(o){return e.call(this,o,zt)}:zt;return this._pairs.map(function(n){return i(n[0])+"="+i(n[1])},"").join("&")};function Eo(t){return encodeURIComponent(t).replace(/%3A/gi,":").replace(/%24/g,"$").replace(/%2C/gi,",").replace(/%20/g,"+").replace(/%5B/gi,"[").replace(/%5D/gi,"]")}function Bt(t,e,i){if(!e)return t;const o=i&&i.encode||Eo;l.isFunction(i)&&(i={serialize:i});const n=i&&i.serialize;let s;if(n?s=n(e,i):s=l.isURLSearchParams(e)?e.toString():new Ye(e,i).toString(o),s){const r=t.indexOf("#");r!==-1&&(t=t.slice(0,r)),t+=(t.indexOf("?")===-1?"?":"&")+s}return t}class Ht{constructor(){this.handlers=[]}use(e,i,o){return this.handlers.push({fulfilled:e,rejected:i,synchronous:o?o.synchronous:!1,runWhen:o?o.runWhen:null}),this.handlers.length-1}eject(e){this.handlers[e]&&(this.handlers[e]=null)}clear(){this.handlers&&(this.handlers=[])}forEach(e){l.forEach(this.handlers,function(o){o!==null&&e(o)})}}const Gt={silentJSONParsing:!0,forcedJSONParsing:!0,clarifyTimeoutError:!1},Po={isBrowser:!0,classes:{URLSearchParams:typeof URLSearchParams<"u"?URLSearchParams:Ye,FormData:typeof FormData<"u"?FormData:null,Blob:typeof Blob<"u"?Blob:null},protocols:["http","https","file","blob","url","data"]},et=typeof window<"u"&&typeof document<"u",tt=typeof navigator=="object"&&navigator||void 0,So=et&&(!tt||["ReactNative","NativeScript","NS"].indexOf(tt.product)<0),Lo=typeof WorkerGlobalScope<"u"&&self instanceof WorkerGlobalScope&&typeof self.importScripts=="function",Ro=et&&window.location.href||"http://localhost",A={...Object.freeze(Object.defineProperty({__proto__:null,hasBrowserEnv:et,hasStandardBrowserEnv:So,hasStandardBrowserWebWorkerEnv:Lo,navigator:tt,origin:Ro},Symbol.toStringTag,{value:"Module"})),...Po};function To(t,e){return Re(t,new A.classes.URLSearchParams,Object.assign({visitor:function(i,o,n,s){return A.isNode&&l.isBuffer(i)?(this.append(o,i.toString("base64")),!1):s.defaultVisitor.apply(this,arguments)}},e))}function Ao(t){return l.matchAll(/\w+|\[(\w*)]/g,t).map(e=>e[0]==="[]"?"":e[1]||e[0])}function Oo(t){const e={},i=Object.keys(t);let o;const n=i.length;let s;for(o=0;o<n;o++)s=i[o],e[s]=t[s];return e}function jt(t){function e(i,o,n,s){let r=i[s++];if(r==="__proto__")return!0;const a=Number.isFinite(+r),c=s>=i.length;return r=!r&&l.isArray(n)?n.length:r,c?(l.hasOwnProp(n,r)?n[r]=[n[r],o]:n[r]=o,!a):((!n[r]||!l.isObject(n[r]))&&(n[r]=[]),e(i,o,n[r],s)&&l.isArray(n[r])&&(n[r]=Oo(n[r])),!a)}if(l.isFormData(t)&&l.isFunction(t.entries)){const i={};return l.forEachEntry(t,(o,n)=>{e(Ao(o),n,i,0)}),i}return null}function No(t,e,i){if(l.isString(t))try{return(e||JSON.parse)(t),l.trim(t)}catch(o){if(o.name!=="SyntaxError")throw o}return(0,JSON.stringify)(t)}const ye={transitional:Gt,adapter:["xhr","http","fetch"],transformRequest:[function(e,i){const o=i.getContentType()||"",n=o.indexOf("application/json")>-1,s=l.isObject(e);if(s&&l.isHTMLForm(e)&&(e=new FormData(e)),l.isFormData(e))return n?JSON.stringify(jt(e)):e;if(l.isArrayBuffer(e)||l.isBuffer(e)||l.isStream(e)||l.isFile(e)||l.isBlob(e)||l.isReadableStream(e))return e;if(l.isArrayBufferView(e))return e.buffer;if(l.isURLSearchParams(e))return i.setContentType("application/x-www-form-urlencoded;charset=utf-8",!1),e.toString();let a;if(s){if(o.indexOf("application/x-www-form-urlencoded")>-1)return To(e,this.formSerializer).toString();if((a=l.isFileList(e))||o.indexOf("multipart/form-data")>-1){const c=this.env&&this.env.FormData;return Re(a?{"files[]":e}:e,c&&new c,this.formSerializer)}}return s||n?(i.setContentType("application/json",!1),No(e)):e}],transformResponse:[function(e){const i=this.transitional||ye.transitional,o=i&&i.forcedJSONParsing,n=this.responseType==="json";if(l.isResponse(e)||l.isReadableStream(e))return e;if(e&&l.isString(e)&&(o&&!this.responseType||n)){const r=!(i&&i.silentJSONParsing)&&n;try{return JSON.parse(e)}catch(a){if(r)throw a.name==="SyntaxError"?b.from(a,b.ERR_BAD_RESPONSE,this,null,this.response):a}}return e}],timeout:0,xsrfCookieName:"XSRF-TOKEN",xsrfHeaderName:"X-XSRF-TOKEN",maxContentLength:-1,maxBodyLength:-1,env:{FormData:A.classes.FormData,Blob:A.classes.Blob},validateStatus:function(e){return e>=200&&e<300},headers:{common:{Accept:"application/json, text/plain, */*","Content-Type":void 0}}};l.forEach(["delete","get","head","post","put","patch"],t=>{ye.headers[t]={}});const _o=l.toObjectSet(["age","authorization","content-length","content-type","etag","expires","from","host","if-modified-since","if-unmodified-since","last-modified","location","max-forwards","proxy-authorization","referer","retry-after","user-agent"]),ko=t=>{const e={};let i,o,n;return t&&t.split(`
`).forEach(function(r){n=r.indexOf(":"),i=r.substring(0,n).trim().toLowerCase(),o=r.substring(n+1).trim(),!(!i||e[i]&&_o[i])&&(i==="set-cookie"?e[i]?e[i].push(o):e[i]=[o]:e[i]=e[i]?e[i]+", "+o:o)}),e},qt=Symbol("internals");function ve(t){return t&&String(t).trim().toLowerCase()}function Te(t){return t===!1||t==null?t:l.isArray(t)?t.map(Te):String(t)}function Io(t){const e=Object.create(null),i=/([^\s,;=]+)\s*(?:=\s*([^,;]+))?/g;let o;for(;o=i.exec(t);)e[o[1]]=o[2];return e}const Fo=t=>/^[-_a-zA-Z0-9^`|~,!#$%&'*+.]+$/.test(t.trim());function it(t,e,i,o,n){if(l.isFunction(o))return o.call(this,e,i);if(n&&(e=i),!!l.isString(e)){if(l.isString(o))return e.indexOf(o)!==-1;if(l.isRegExp(o))return o.test(e)}}function Mo(t){return t.trim().toLowerCase().replace(/([a-z\d])(\w*)/g,(e,i,o)=>i.toUpperCase()+o)}function Uo(t,e){const i=l.toCamelCase(" "+e);["get","set","has"].forEach(o=>{Object.defineProperty(t,o+i,{value:function(n,s,r){return this[o].call(this,e,n,s,r)},configurable:!0})})}class O{constructor(e){e&&this.set(e)}set(e,i,o){const n=this;function s(a,c,d){const u=ve(c);if(!u)throw new Error("header name must be a non-empty string");const h=l.findKey(n,u);(!h||n[h]===void 0||d===!0||d===void 0&&n[h]!==!1)&&(n[h||c]=Te(a))}const r=(a,c)=>l.forEach(a,(d,u)=>s(d,u,c));if(l.isPlainObject(e)||e instanceof this.constructor)r(e,i);else if(l.isString(e)&&(e=e.trim())&&!Fo(e))r(ko(e),i);else if(l.isHeaders(e))for(const[a,c]of e.entries())s(c,a,o);else e!=null&&s(i,e,o);return this}get(e,i){if(e=ve(e),e){const o=l.findKey(this,e);if(o){const n=this[o];if(!i)return n;if(i===!0)return Io(n);if(l.isFunction(i))return i.call(this,n,o);if(l.isRegExp(i))return i.exec(n);throw new TypeError("parser must be boolean|regexp|function")}}}has(e,i){if(e=ve(e),e){const o=l.findKey(this,e);return!!(o&&this[o]!==void 0&&(!i||it(this,this[o],o,i)))}return!1}delete(e,i){const o=this;let n=!1;function s(r){if(r=ve(r),r){const a=l.findKey(o,r);a&&(!i||it(o,o[a],a,i))&&(delete o[a],n=!0)}}return l.isArray(e)?e.forEach(s):s(e),n}clear(e){const i=Object.keys(this);let o=i.length,n=!1;for(;o--;){const s=i[o];(!e||it(this,this[s],s,e,!0))&&(delete this[s],n=!0)}return n}normalize(e){const i=this,o={};return l.forEach(this,(n,s)=>{const r=l.findKey(o,s);if(r){i[r]=Te(n),delete i[s];return}const a=e?Mo(s):String(s).trim();a!==s&&delete i[s],i[a]=Te(n),o[a]=!0}),this}concat(...e){return this.constructor.concat(this,...e)}toJSON(e){const i=Object.create(null);return l.forEach(this,(o,n)=>{o!=null&&o!==!1&&(i[n]=e&&l.isArray(o)?o.join(", "):o)}),i}[Symbol.iterator](){return Object.entries(this.toJSON())[Symbol.iterator]()}toString(){return Object.entries(this.toJSON()).map(([e,i])=>e+": "+i).join(`
`)}get[Symbol.toStringTag](){return"AxiosHeaders"}static from(e){return e instanceof this?e:new this(e)}static concat(e,...i){const o=new this(e);return i.forEach(n=>o.set(n)),o}static accessor(e){const o=(this[qt]=this[qt]={accessors:{}}).accessors,n=this.prototype;function s(r){const a=ve(r);o[a]||(Uo(n,r),o[a]=!0)}return l.isArray(e)?e.forEach(s):s(e),this}}O.accessor(["Content-Type","Content-Length","Accept","Accept-Encoding","User-Agent","Authorization"]),l.reduceDescriptors(O.prototype,({value:t},e)=>{let i=e[0].toUpperCase()+e.slice(1);return{get:()=>t,set(o){this[i]=o}}}),l.freezeMethods(O);function ot(t,e){const i=this||ye,o=e||i,n=O.from(o.headers);let s=o.data;return l.forEach(t,function(a){s=a.call(i,s,n.normalize(),e?e.status:void 0)}),n.normalize(),s}function Wt(t){return!!(t&&t.__CANCEL__)}function le(t,e,i){b.call(this,t??"canceled",b.ERR_CANCELED,e,i),this.name="CanceledError"}l.inherits(le,b,{__CANCEL__:!0});function Jt(t,e,i){const o=i.config.validateStatus;!i.status||!o||o(i.status)?t(i):e(new b("Request failed with status code "+i.status,[b.ERR_BAD_REQUEST,b.ERR_BAD_RESPONSE][Math.floor(i.status/100)-4],i.config,i.request,i))}function zo(t){const e=/^([-+\w]{1,25})(:?\/\/|:)/.exec(t);return e&&e[1]||""}function Vo(t,e){t=t||10;const i=new Array(t),o=new Array(t);let n=0,s=0,r;return e=e!==void 0?e:1e3,function(c){const d=Date.now(),u=o[s];r||(r=d),i[n]=c,o[n]=d;let h=s,v=0;for(;h!==n;)v+=i[h++],h=h%t;if(n=(n+1)%t,n===s&&(s=(s+1)%t),d-r<e)return;const x=u&&d-u;return x?Math.round(v*1e3/x):void 0}}function Bo(t,e){let i=0,o=1e3/e,n,s;const r=(d,u=Date.now())=>{i=u,n=null,s&&(clearTimeout(s),s=null),t.apply(null,d)};return[(...d)=>{const u=Date.now(),h=u-i;h>=o?r(d,u):(n=d,s||(s=setTimeout(()=>{s=null,r(n)},o-h)))},()=>n&&r(n)]}const Ae=(t,e,i=3)=>{let o=0;const n=Vo(50,250);return Bo(s=>{const r=s.loaded,a=s.lengthComputable?s.total:void 0,c=r-o,d=n(c),u=r<=a;o=r;const h={loaded:r,total:a,progress:a?r/a:void 0,bytes:c,rate:d||void 0,estimated:d&&a&&u?(a-r)/d:void 0,event:s,lengthComputable:a!=null,[e?"download":"upload"]:!0};t(h)},i)},Qt=(t,e)=>{const i=t!=null;return[o=>e[0]({lengthComputable:i,total:t,loaded:o}),e[1]]},Kt=t=>(...e)=>l.asap(()=>t(...e)),Ho=A.hasStandardBrowserEnv?((t,e)=>i=>(i=new URL(i,A.origin),t.protocol===i.protocol&&t.host===i.host&&(e||t.port===i.port)))(new URL(A.origin),A.navigator&&/(msie|trident)/i.test(A.navigator.userAgent)):()=>!0,Go=A.hasStandardBrowserEnv?{write(t,e,i,o,n,s){const r=[t+"="+encodeURIComponent(e)];l.isNumber(i)&&r.push("expires="+new Date(i).toGMTString()),l.isString(o)&&r.push("path="+o),l.isString(n)&&r.push("domain="+n),s===!0&&r.push("secure"),document.cookie=r.join("; ")},read(t){const e=document.cookie.match(new RegExp("(^|;\\s*)("+t+")=([^;]*)"));return e?decodeURIComponent(e[3]):null},remove(t){this.write(t,"",Date.now()-864e5)}}:{write(){},read(){return null},remove(){}};function jo(t){return/^([a-z][a-z\d+\-.]*:)?\/\//i.test(t)}function qo(t,e){return e?t.replace(/\/?\/$/,"")+"/"+e.replace(/^\/+/,""):t}function Zt(t,e){return t&&!jo(e)?qo(t,e):e}const Xt=t=>t instanceof O?{...t}:t;function ee(t,e){e=e||{};const i={};function o(d,u,h,v){return l.isPlainObject(d)&&l.isPlainObject(u)?l.merge.call({caseless:v},d,u):l.isPlainObject(u)?l.merge({},u):l.isArray(u)?u.slice():u}function n(d,u,h,v){if(l.isUndefined(u)){if(!l.isUndefined(d))return o(void 0,d,h,v)}else return o(d,u,h,v)}function s(d,u){if(!l.isUndefined(u))return o(void 0,u)}function r(d,u){if(l.isUndefined(u)){if(!l.isUndefined(d))return o(void 0,d)}else return o(void 0,u)}function a(d,u,h){if(h in e)return o(d,u);if(h in t)return o(void 0,d)}const c={url:s,method:s,data:s,baseURL:r,transformRequest:r,transformResponse:r,paramsSerializer:r,timeout:r,timeoutMessage:r,withCredentials:r,withXSRFToken:r,adapter:r,responseType:r,xsrfCookieName:r,xsrfHeaderName:r,onUploadProgress:r,onDownloadProgress:r,decompress:r,maxContentLength:r,maxBodyLength:r,beforeRedirect:r,transport:r,httpAgent:r,httpsAgent:r,cancelToken:r,socketPath:r,responseEncoding:r,validateStatus:a,headers:(d,u,h)=>n(Xt(d),Xt(u),h,!0)};return l.forEach(Object.keys(Object.assign({},t,e)),function(u){const h=c[u]||n,v=h(t[u],e[u],u);l.isUndefined(v)&&h!==a||(i[u]=v)}),i}const Yt=t=>{const e=ee({},t);let{data:i,withXSRFToken:o,xsrfHeaderName:n,xsrfCookieName:s,headers:r,auth:a}=e;e.headers=r=O.from(r),e.url=Bt(Zt(e.baseURL,e.url),t.params,t.paramsSerializer),a&&r.set("Authorization","Basic "+btoa((a.username||"")+":"+(a.password?unescape(encodeURIComponent(a.password)):"")));let c;if(l.isFormData(i)){if(A.hasStandardBrowserEnv||A.hasStandardBrowserWebWorkerEnv)r.setContentType(void 0);else if((c=r.getContentType())!==!1){const[d,...u]=c?c.split(";").map(h=>h.trim()).filter(Boolean):[];r.setContentType([d||"multipart/form-data",...u].join("; "))}}if(A.hasStandardBrowserEnv&&(o&&l.isFunction(o)&&(o=o(e)),o||o!==!1&&Ho(e.url))){const d=n&&s&&Go.read(s);d&&r.set(n,d)}return e},Wo=typeof XMLHttpRequest<"u"&&function(t){return new Promise(function(i,o){const n=Yt(t);let s=n.data;const r=O.from(n.headers).normalize();let{responseType:a,onUploadProgress:c,onDownloadProgress:d}=n,u,h,v,x,m;function y(){x&&x(),m&&m(),n.cancelToken&&n.cancelToken.unsubscribe(u),n.signal&&n.signal.removeEventListener("abort",u)}let f=new XMLHttpRequest;f.open(n.method.toUpperCase(),n.url,!0),f.timeout=n.timeout;function C(){if(!f)return;const T=O.from("getAllResponseHeaders"in f&&f.getAllResponseHeaders()),N={data:!a||a==="text"||a==="json"?f.responseText:f.response,status:f.status,statusText:f.statusText,headers:T,config:t,request:f};Jt(function(oe){i(oe),y()},function(oe){o(oe),y()},N),f=null}"onloadend"in f?f.onloadend=C:f.onreadystatechange=function(){!f||f.readyState!==4||f.status===0&&!(f.responseURL&&f.responseURL.indexOf("file:")===0)||setTimeout(C)},f.onabort=function(){f&&(o(new b("Request aborted",b.ECONNABORTED,t,f)),f=null)},f.onerror=function(){o(new b("Network Error",b.ERR_NETWORK,t,f)),f=null},f.ontimeout=function(){let B=n.timeout?"timeout of "+n.timeout+"ms exceeded":"timeout exceeded";const N=n.transitional||Gt;n.timeoutErrorMessage&&(B=n.timeoutErrorMessage),o(new b(B,N.clarifyTimeoutError?b.ETIMEDOUT:b.ECONNABORTED,t,f)),f=null},s===void 0&&r.setContentType(null),"setRequestHeader"in f&&l.forEach(r.toJSON(),function(B,N){f.setRequestHeader(N,B)}),l.isUndefined(n.withCredentials)||(f.withCredentials=!!n.withCredentials),a&&a!=="json"&&(f.responseType=n.responseType),d&&([v,m]=Ae(d,!0),f.addEventListener("progress",v)),c&&f.upload&&([h,x]=Ae(c),f.upload.addEventListener("progress",h),f.upload.addEventListener("loadend",x)),(n.cancelToken||n.signal)&&(u=T=>{f&&(o(!T||T.type?new le(null,t,f):T),f.abort(),f=null)},n.cancelToken&&n.cancelToken.subscribe(u),n.signal&&(n.signal.aborted?u():n.signal.addEventListener("abort",u)));const R=zo(n.url);if(R&&A.protocols.indexOf(R)===-1){o(new b("Unsupported protocol "+R+":",b.ERR_BAD_REQUEST,t));return}f.send(s||null)})},Jo=(t,e)=>{const{length:i}=t=t?t.filter(Boolean):[];if(e||i){let o=new AbortController,n;const s=function(d){if(!n){n=!0,a();const u=d instanceof Error?d:this.reason;o.abort(u instanceof b?u:new le(u instanceof Error?u.message:u))}};let r=e&&setTimeout(()=>{r=null,s(new b(`timeout ${e} of ms exceeded`,b.ETIMEDOUT))},e);const a=()=>{t&&(r&&clearTimeout(r),r=null,t.forEach(d=>{d.unsubscribe?d.unsubscribe(s):d.removeEventListener("abort",s)}),t=null)};t.forEach(d=>d.addEventListener("abort",s));const{signal:c}=o;return c.unsubscribe=()=>l.asap(a),c}},Qo=function*(t,e){let i=t.byteLength;if(i<e){yield t;return}let o=0,n;for(;o<i;)n=o+e,yield t.slice(o,n),o=n},Ko=async function*(t,e){for await(const i of Zo(t))yield*Qo(i,e)},Zo=async function*(t){if(t[Symbol.asyncIterator]){yield*t;return}const e=t.getReader();try{for(;;){const{done:i,value:o}=await e.read();if(i)break;yield o}}finally{await e.cancel()}},ei=(t,e,i,o)=>{const n=Ko(t,e);let s=0,r,a=c=>{r||(r=!0,o&&o(c))};return new ReadableStream({async pull(c){try{const{done:d,value:u}=await n.next();if(d){a(),c.close();return}let h=u.byteLength;if(i){let v=s+=h;i(v)}c.enqueue(new Uint8Array(u))}catch(d){throw a(d),d}},cancel(c){return a(c),n.return()}},{highWaterMark:2})},Oe=typeof fetch=="function"&&typeof Request=="function"&&typeof Response=="function",ti=Oe&&typeof ReadableStream=="function",Xo=Oe&&(typeof TextEncoder=="function"?(t=>e=>t.encode(e))(new TextEncoder):async t=>new Uint8Array(await new Response(t).arrayBuffer())),ii=(t,...e)=>{try{return!!t(...e)}catch{return!1}},Yo=ti&&ii(()=>{let t=!1;const e=new Request(A.origin,{body:new ReadableStream,method:"POST",get duplex(){return t=!0,"half"}}).headers.has("Content-Type");return t&&!e}),oi=64*1024,nt=ti&&ii(()=>l.isReadableStream(new Response("").body)),Ne={stream:nt&&(t=>t.body)};Oe&&(t=>{["text","arrayBuffer","blob","formData","stream"].forEach(e=>{!Ne[e]&&(Ne[e]=l.isFunction(t[e])?i=>i[e]():(i,o)=>{throw new b(`Response type '${e}' is not supported`,b.ERR_NOT_SUPPORT,o)})})})(new Response);const en=async t=>{if(t==null)return 0;if(l.isBlob(t))return t.size;if(l.isSpecCompliantForm(t))return(await new Request(A.origin,{method:"POST",body:t}).arrayBuffer()).byteLength;if(l.isArrayBufferView(t)||l.isArrayBuffer(t))return t.byteLength;if(l.isURLSearchParams(t)&&(t=t+""),l.isString(t))return(await Xo(t)).byteLength},tn=async(t,e)=>{const i=l.toFiniteNumber(t.getContentLength());return i??en(e)},st={http:wo,xhr:Wo,fetch:Oe&&(async t=>{let{url:e,method:i,data:o,signal:n,cancelToken:s,timeout:r,onDownloadProgress:a,onUploadProgress:c,responseType:d,headers:u,withCredentials:h="same-origin",fetchOptions:v}=Yt(t);d=d?(d+"").toLowerCase():"text";let x=Jo([n,s&&s.toAbortSignal()],r),m;const y=x&&x.unsubscribe&&(()=>{x.unsubscribe()});let f;try{if(c&&Yo&&i!=="get"&&i!=="head"&&(f=await tn(u,o))!==0){let N=new Request(e,{method:"POST",body:o,duplex:"half"}),W;if(l.isFormData(o)&&(W=N.headers.get("content-type"))&&u.setContentType(W),N.body){const[oe,ze]=Qt(f,Ae(Kt(c)));o=ei(N.body,oi,oe,ze)}}l.isString(h)||(h=h?"include":"omit");const C="credentials"in Request.prototype;m=new Request(e,{...v,signal:x,method:i.toUpperCase(),headers:u.normalize().toJSON(),body:o,duplex:"half",credentials:C?h:void 0});let R=await fetch(m);const T=nt&&(d==="stream"||d==="response");if(nt&&(a||T&&y)){const N={};["status","statusText","headers"].forEach(fi=>{N[fi]=R[fi]});const W=l.toFiniteNumber(R.headers.get("content-length")),[oe,ze]=a&&Qt(W,Ae(Kt(a),!0))||[];R=new Response(ei(R.body,oi,oe,()=>{ze&&ze(),y&&y()}),N)}d=d||"text";let B=await Ne[l.findKey(Ne,d)||"text"](R,t);return!T&&y&&y(),await new Promise((N,W)=>{Jt(N,W,{data:B,headers:O.from(R.headers),status:R.status,statusText:R.statusText,config:t,request:m})})}catch(C){throw y&&y(),C&&C.name==="TypeError"&&/fetch/i.test(C.message)?Object.assign(new b("Network Error",b.ERR_NETWORK,t,m),{cause:C.cause||C}):b.from(C,C&&C.code,t,m)}})};l.forEach(st,(t,e)=>{if(t){try{Object.defineProperty(t,"name",{value:e})}catch{}Object.defineProperty(t,"adapterName",{value:e})}});const ni=t=>`- ${t}`,on=t=>l.isFunction(t)||t===null||t===!1,si={getAdapter:t=>{t=l.isArray(t)?t:[t];const{length:e}=t;let i,o;const n={};for(let s=0;s<e;s++){i=t[s];let r;if(o=i,!on(i)&&(o=st[(r=String(i)).toLowerCase()],o===void 0))throw new b(`Unknown adapter '${r}'`);if(o)break;n[r||"#"+s]=o}if(!o){const s=Object.entries(n).map(([a,c])=>`adapter ${a} `+(c===!1?"is not supported by the environment":"is not available in the build"));let r=e?s.length>1?`since :
`+s.map(ni).join(`
`):" "+ni(s[0]):"as no adapter specified";throw new b("There is no suitable adapter to dispatch the request "+r,"ERR_NOT_SUPPORT")}return o},adapters:st};function rt(t){if(t.cancelToken&&t.cancelToken.throwIfRequested(),t.signal&&t.signal.aborted)throw new le(null,t)}function ri(t){return rt(t),t.headers=O.from(t.headers),t.data=ot.call(t,t.transformRequest),["post","put","patch"].indexOf(t.method)!==-1&&t.headers.setContentType("application/x-www-form-urlencoded",!1),si.getAdapter(t.adapter||ye.adapter)(t).then(function(o){return rt(t),o.data=ot.call(t,t.transformResponse,o),o.headers=O.from(o.headers),o},function(o){return Wt(o)||(rt(t),o&&o.response&&(o.response.data=ot.call(t,t.transformResponse,o.response),o.response.headers=O.from(o.response.headers))),Promise.reject(o)})}const ai="1.7.9",_e={};["object","boolean","number","function","string","symbol"].forEach((t,e)=>{_e[t]=function(o){return typeof o===t||"a"+(e<1?"n ":" ")+t}});const li={};_e.transitional=function(e,i,o){function n(s,r){return"[Axios v"+ai+"] Transitional option '"+s+"'"+r+(o?". "+o:"")}return(s,r,a)=>{if(e===!1)throw new b(n(r," has been removed"+(i?" in "+i:"")),b.ERR_DEPRECATED);return i&&!li[r]&&(li[r]=!0,console.warn(n(r," has been deprecated since v"+i+" and will be removed in the near future"))),e?e(s,r,a):!0}},_e.spelling=function(e){return(i,o)=>(console.warn(`${o} is likely a misspelling of ${e}`),!0)};function nn(t,e,i){if(typeof t!="object")throw new b("options must be an object",b.ERR_BAD_OPTION_VALUE);const o=Object.keys(t);let n=o.length;for(;n-- >0;){const s=o[n],r=e[s];if(r){const a=t[s],c=a===void 0||r(a,s,t);if(c!==!0)throw new b("option "+s+" must be "+c,b.ERR_BAD_OPTION_VALUE);continue}if(i!==!0)throw new b("Unknown option "+s,b.ERR_BAD_OPTION)}}const ke={assertOptions:nn,validators:_e},U=ke.validators;class te{constructor(e){this.defaults=e,this.interceptors={request:new Ht,response:new Ht}}async request(e,i){try{return await this._request(e,i)}catch(o){if(o instanceof Error){let n={};Error.captureStackTrace?Error.captureStackTrace(n):n=new Error;const s=n.stack?n.stack.replace(/^.+\n/,""):"";try{o.stack?s&&!String(o.stack).endsWith(s.replace(/^.+\n.+\n/,""))&&(o.stack+=`
`+s):o.stack=s}catch{}}throw o}}_request(e,i){typeof e=="string"?(i=i||{},i.url=e):i=e||{},i=ee(this.defaults,i);const{transitional:o,paramsSerializer:n,headers:s}=i;o!==void 0&&ke.assertOptions(o,{silentJSONParsing:U.transitional(U.boolean),forcedJSONParsing:U.transitional(U.boolean),clarifyTimeoutError:U.transitional(U.boolean)},!1),n!=null&&(l.isFunction(n)?i.paramsSerializer={serialize:n}:ke.assertOptions(n,{encode:U.function,serialize:U.function},!0)),ke.assertOptions(i,{baseUrl:U.spelling("baseURL"),withXsrfToken:U.spelling("withXSRFToken")},!0),i.method=(i.method||this.defaults.method||"get").toLowerCase();let r=s&&l.merge(s.common,s[i.method]);s&&l.forEach(["delete","get","head","post","put","patch","common"],m=>{delete s[m]}),i.headers=O.concat(r,s);const a=[];let c=!0;this.interceptors.request.forEach(function(y){typeof y.runWhen=="function"&&y.runWhen(i)===!1||(c=c&&y.synchronous,a.unshift(y.fulfilled,y.rejected))});const d=[];this.interceptors.response.forEach(function(y){d.push(y.fulfilled,y.rejected)});let u,h=0,v;if(!c){const m=[ri.bind(this),void 0];for(m.unshift.apply(m,a),m.push.apply(m,d),v=m.length,u=Promise.resolve(i);h<v;)u=u.then(m[h++],m[h++]);return u}v=a.length;let x=i;for(h=0;h<v;){const m=a[h++],y=a[h++];try{x=m(x)}catch(f){y.call(this,f);break}}try{u=ri.call(this,x)}catch(m){return Promise.reject(m)}for(h=0,v=d.length;h<v;)u=u.then(d[h++],d[h++]);return u}getUri(e){e=ee(this.defaults,e);const i=Zt(e.baseURL,e.url);return Bt(i,e.params,e.paramsSerializer)}}l.forEach(["delete","get","head","options"],function(e){te.prototype[e]=function(i,o){return this.request(ee(o||{},{method:e,url:i,data:(o||{}).data}))}}),l.forEach(["post","put","patch"],function(e){function i(o){return function(s,r,a){return this.request(ee(a||{},{method:e,headers:o?{"Content-Type":"multipart/form-data"}:{},url:s,data:r}))}}te.prototype[e]=i(),te.prototype[e+"Form"]=i(!0)});class at{constructor(e){if(typeof e!="function")throw new TypeError("executor must be a function.");let i;this.promise=new Promise(function(s){i=s});const o=this;this.promise.then(n=>{if(!o._listeners)return;let s=o._listeners.length;for(;s-- >0;)o._listeners[s](n);o._listeners=null}),this.promise.then=n=>{let s;const r=new Promise(a=>{o.subscribe(a),s=a}).then(n);return r.cancel=function(){o.unsubscribe(s)},r},e(function(s,r,a){o.reason||(o.reason=new le(s,r,a),i(o.reason))})}throwIfRequested(){if(this.reason)throw this.reason}subscribe(e){if(this.reason){e(this.reason);return}this._listeners?this._listeners.push(e):this._listeners=[e]}unsubscribe(e){if(!this._listeners)return;const i=this._listeners.indexOf(e);i!==-1&&this._listeners.splice(i,1)}toAbortSignal(){const e=new AbortController,i=o=>{e.abort(o)};return this.subscribe(i),e.signal.unsubscribe=()=>this.unsubscribe(i),e.signal}static source(){let e;return{token:new at(function(n){e=n}),cancel:e}}}function sn(t){return function(i){return t.apply(null,i)}}function rn(t){return l.isObject(t)&&t.isAxiosError===!0}const lt={Continue:100,SwitchingProtocols:101,Processing:102,EarlyHints:103,Ok:200,Created:201,Accepted:202,NonAuthoritativeInformation:203,NoContent:204,ResetContent:205,PartialContent:206,MultiStatus:207,AlreadyReported:208,ImUsed:226,MultipleChoices:300,MovedPermanently:301,Found:302,SeeOther:303,NotModified:304,UseProxy:305,Unused:306,TemporaryRedirect:307,PermanentRedirect:308,BadRequest:400,Unauthorized:401,PaymentRequired:402,Forbidden:403,NotFound:404,MethodNotAllowed:405,NotAcceptable:406,ProxyAuthenticationRequired:407,RequestTimeout:408,Conflict:409,Gone:410,LengthRequired:411,PreconditionFailed:412,PayloadTooLarge:413,UriTooLong:414,UnsupportedMediaType:415,RangeNotSatisfiable:416,ExpectationFailed:417,ImATeapot:418,MisdirectedRequest:421,UnprocessableEntity:422,Locked:423,FailedDependency:424,TooEarly:425,UpgradeRequired:426,PreconditionRequired:428,TooManyRequests:429,RequestHeaderFieldsTooLarge:431,UnavailableForLegalReasons:451,InternalServerError:500,NotImplemented:501,BadGateway:502,ServiceUnavailable:503,GatewayTimeout:504,HttpVersionNotSupported:505,VariantAlsoNegotiates:506,InsufficientStorage:507,LoopDetected:508,NotExtended:510,NetworkAuthenticationRequired:511};Object.entries(lt).forEach(([t,e])=>{lt[e]=t});function ci(t){const e=new te(t),i=Pt(te.prototype.request,e);return l.extend(i,te.prototype,e,{allOwnKeys:!0}),l.extend(i,e,null,{allOwnKeys:!0}),i.create=function(n){return ci(ee(t,n))},i}const E=ci(ye);E.Axios=te,E.CanceledError=le,E.CancelToken=at,E.isCancel=Wt,E.VERSION=ai,E.toFormData=Re,E.AxiosError=b,E.Cancel=E.CanceledError,E.all=function(e){return Promise.all(e)},E.spread=sn,E.isAxiosError=rn,E.mergeConfig=ee,E.AxiosHeaders=O,E.formToJSON=t=>jt(l.isHTMLForm(t)?new FormData(t):t),E.getAdapter=si.getAdapter,E.HttpStatusCode=lt,E.default=E;async function S(t,e,i,o,n,s,r){try{const a=await E.request({method:e,baseURL:t+`${s||"G2OnlineServices"}/`+i,headers:{Authorization:`Bearer ${o}`},data:n,...r});return{data:a.data,status:a.status}}catch(a){const c=a;if(c.response)return{data:c.response.data,status:c.response.status};throw c.request?new Error("No response received"):new Error("Request configuration error")}}const an=[{id:"-",label:"-",isSort:!1},{id:"IDVeiculo",label:"Código",isSort:!0},{id:"DataVenda",label:"Data da Venda",isSort:!0},{id:"Descricao",label:"Descrição",isSort:!0},{id:"ValorTotal",label:"Valor Total",isSort:!0},{id:"LancamentosQuitados",label:"Status Pagamento",isSort:!0},{id:"TipoVenda",label:"Tipo de Venda",isSort:!0},{id:"Download",label:"Download Nota",isSort:!1}];function di(t,e="pt-BR"){return new Intl.NumberFormat(e,{currency:"BRL",style:"currency"}).format(t)}const ln=ne`
  .container-documentation {
    display: flex;
    flex-direction: column;
  }

  .container-documentation .section-step {
    margin-bottom: 12px;
  }

  .documentation-header {
    display: flex;
    align-items: center;
    justify-content: space-between;

    margin-bottom: 12px;
  }

  .documentation-header h1 {
    font-size: var(--text-headline-lg);
    font-weight: var(--weight-bold);
    color: red;
  }

  .documentation-header .header-actions {
    display: flex;
    align-items: center;
    gap: 12px;

    > a {
      display: flex;
      align-items: center;
      gap: 6px;

      font-size: var(--text-small-sm);
      font-weight: var(--weight-semibold);
      color: var(--gray-700);

      &:hover {
        color: var(--blue-600);
        text-decoration: underline;
      }
    }
  }

  .box {
    overflow: visible;
    border: 1px solid #ddd;
    position: relative;
    border-radius: 4px;

    background-color: #fff;
  }

  .section-box-header {
    display: flex;
    flex-direction: column;
    padding: 8px 10px;
  }

  .section-box-header .filter-header {
    display: flex;
    align-items: flex-end;
    justify-content: space-between;
    margin-bottom: 10px;
    gap: 12px;
  }

  @media (max-width: 620px) {
    .filter-header {
      flex-direction: column;
    }
  }

  .section-box-header .selcted-head {
    display: flex;
    align-items: flex-end;
    gap: 6px;

    .filter-mobile {
      display: none;
    }

    @media (max-width: 620px) {
      .filter-desktop {
        display: none;
      }
    }

    @media (max-width: 620px) {
      .filter-mobile {
        display: block
      }
    }
  }

  .section-box-header .filter-header .field-group {
    display: flex;
    align-items: flex-end;
    gap: 1rem;
    width: 100%;

    .field-filter {
      display: flex;
      gap: 12px;
      flex-direction: row;
    }

    @media (max-width: 620px) {
      display: none;
      .field-filter {
        flex: 1;
        flex-direction: column;
        align-items: baseline;
      }
    }
  }

  .section-box-filter {
    padding: 8px 10px;
  }

  .section-box-table {
    overflow: auto;
  }

  .dialog-container {
    display: flex;
    flex-direction: column;
    width: clamp(400px, 1000px, 95vw);
    padding-right: 2px;
    overflow: auto;

    @media (max-width: 620px) {
      grid-template-columns: 1fr;
      width: 100%;
    }
  }

  .dialog-container .dialog-content {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1rem;
    margin-bottom: 12px;
    padding: 12px;
    overflow: auto;

    @media (max-width: 620px) {
      grid-template-columns: 1fr;
      max-height: 50vh;
    }
  }

  .dialog-container .dialog-content .dialog-section-left {
    width: 100%;
    border-right: 1px solid var(--gray-100);
    padding-right: 12px;
  }

  .dialog-box-group {
    display: flex;
    flex-direction: column;
    gap: 12px;
  }

  .dialog-container .dialog-content .dialog-section-right {
    width: 100%;
  }

  .dialog-container .dialog-footer {
    display: flex;
    align-items: center;
    justify-content: right;
    gap: 12px;

    padding: 12px;
    border-top: 1px solid var(--gray-100);

    @media (max-width: 620px) {
      flex-direction: column;
    }
  }

  .footer-group {
    display: flex;
    gap: 12px;
  }

  .dialog-container .card-error {
    display: flex;
    align-items: center;
    gap: 1rem;

    padding: 8px;

    border-radius: 4px;
    border-top: 1px;
    border-right: 1px;
    border-bottom: 1px;
    border-left: 4px;
    border-color: #f79009;
    border-style: solid;
    background-color: #fffcf5;
    margin-bottom: 1rem;
    margin-top: 6px;
  }

  .dialog-container .field-group {
    display: flex;
    align-items: flex-end;
    gap: 1rem;
    width: 100%;

    .field-filter {
      display: flex;
      flex-direction: column;
      gap: 12px;
      flex: 1;
    }
  }

  .dialog-container .card-error .card-error-alert-icon {
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .dialog-container .card-error .card-error-box-info {
    display: flex;
    flex-direction: column;
    gap: 4px;
  }

  .dialog-container .card-error .card-error-box-info .card-error-title {
    font-size: 1rem;
    font-weight: 700;
    color: #b54708;
  }

  .dialog-container .card-error .card-error-box-info .card-error-info {
    display: flex;
    flex-direction: column;
  }

  .dialog-container .card-error .card-error-box-info .card-error-info span {
    font-size: 14px;
    font-weight: 600;
    color: #b54708;
  }

  .upload-docs {
    display: flex;
    flex-direction: column;
    gap: 8px;
  }

  .upload-docs-form {
    display: flex;
    flex-direction: column;
    gap: 10px;
  }

  .field-group {
    display: flex;
    align-items: center;
    gap: 4px;
  }

  .card-error-info a {
    text-decoration: underline;
  }

  .card-error-info a:hover {
    color: var(--blue-600);
  }

  .field-group .button-clear-file {
    display: grid;
    place-items: center;

    border: none;
    background-color: transparent;

    padding: 4px;
    border-radius: 4px;

    margin-top: 21px;
    height: 36px;
    width: 36px;

    &:hover {
      background-color: #fff0f0;
    }
  }
`,Ie=ne`
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    list-style: none;
    text-decoration: none;
  }

  html {
    scroll-behavior: smooth;
    /* scrollbar-width: thin;
    scrollbar-color: var(--gray-200) var(--gray-300); */
  }

  body {
    font-family: 'Red Hat Display', sans-serif;

    font-synthesis: none;
    text-rendering: optimizeLegibility;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    -webkit-text-size-adjust: 100%;
  }

  ul {
    list-style: none;
    margin: 0;
    padding: 0;
  }

  li {
    margin: 0;
    padding: 0;
  }

  body,
  input,
  textarea,
  button {
    color: var(--gray-500);
  }

  img,
  picture,
  video,
  svg {
    display: block;
    max-width: 100%;
  }

  input,
  button,
  textarea,
  select {
    font: inherit;
  }

  p,
  h1,
  h2,
  h3,
  h4,
  h5,
  h6 {
    overflow-wrap: break-word;
    font-family: 'Red Hat Display', sans-serif;
    color: var(--gray-800);
    font-weight: 600;
  }

  #root,
  #__next {
    isolation: isolate;
  }

  button {
    cursor: pointer;
  }

  @media (max-width: 1080px) {
    html {
      font-size: 93.75%;
    }
  }

  @media (max-width: 720px) {
    html {
      font-size: 87.5%;
    }
  }
  .container-app {
    display: flex;
    flex-direction: column;
    width: 100%;
    height: 100vh;
  }

  .main-app {
    height: calc(100vh - 60px);
  }

  .scroll-bar {
    scrollbar-width: thin;
    scrollbar-color: var(--gray-300) var(--gray-200);
  }

  .bar {
    &::-webkit-scrollbar {
      width: 4px;
      height: 5px;
    }

    &::-webkit-scrollbar-track {
      background: transparent;
    }
    &::-webkit-scrollbar-thumb {
      background-color: var(--gray-300);
      border-radius: 2px;
    }
  }
`,z=t=>{dispatchEvent(new CustomEvent("colibri-common-g2-alert-content",{bubbles:!0,composed:!0,detail:{title:t.title,description:t.description,type:t.type,action:t.action,onCancel:t.onCancel}})),dispatchEvent(new CustomEvent("colibri-common-g2-alert-container-action",{bubbles:!0,composed:!0,detail:{intervalId:t.action?1:void 0}}))};function ie(t){const e=atob(t.content),i=new Uint8Array(e.length);for(let c=0;c<e.length;c++)i[c]=e.charCodeAt(c);const o=t.name.split(".").pop(),n=cn(o),s=new Blob([i],{type:n}),r=URL.createObjectURL(s),a=document.createElement("a");a.href=r,a.download=t.name,document.body.appendChild(a),a.click(),document.body.removeChild(a),URL.revokeObjectURL(r)}function cn(t){switch(t.toLowerCase()){case"txt":return"text/plain";case"pdf":return"application/pdf";default:return"application/octet-stream"}}const dn=p`
  <svg
    width="20"
    height="20"
    viewBox="0 0 20 20"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path
      d="M6.66661 14.1667L9.99994 17.5M9.99994 17.5L13.3333 14.1667M9.99994 17.5V10M17.3999 15.075C18.1244 14.5655 18.6677 13.8385 18.951 12.9993C19.2343 12.1601 19.2428 11.2525 18.9753 10.4082C18.7078 9.56387 18.1782 8.82675 17.4633 8.30381C16.7485 7.78087 15.8856 7.49931 14.9999 7.50001H13.9499C13.6993 6.52323 13.2304 5.61605 12.5784 4.84674C11.9264 4.07743 11.1084 3.46606 10.186 3.05863C9.2635 2.65121 8.26065 2.45836 7.25288 2.4946C6.24512 2.53084 5.25871 2.79523 4.36791 3.26786C3.47711 3.74049 2.70513 4.40905 2.1101 5.2232C1.51507 6.03735 1.11249 6.97588 0.932662 7.96813C0.752836 8.96038 0.800453 9.9805 1.07193 10.9517C1.3434 11.9229 1.83166 12.8198 2.49994 13.575"
      stroke="#667085"
      stroke-width="1.66667"
      stroke-linecap="round"
      stroke-linejoin="round"
    />
    <defs>
      <clipPath id="clip0_4994_9652">
        <rect width="20" height="20" fill="white" />
      </clipPath>
    </defs>
  </svg>
`,un=p`
  <svg
    width="20"
    height="20"
    viewBox="0 0 20 20"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path
      d="M16.5865 7.15533C16.547 7.06488 16.4917 6.9822 16.4232 6.91116L11.4232 1.91116C11.3521 1.84264 11.2694 1.78734 11.179 1.74783C11.154 1.73616 11.1273 1.72949 11.1007 1.72033C11.0309 1.6966 10.9583 1.6823 10.8848 1.67783C10.8673 1.67616 10.8515 1.66699 10.834 1.66699H5.00065C4.08148 1.66699 3.33398 2.41449 3.33398 3.33366V16.667C3.33398 17.5862 4.08148 18.3337 5.00065 18.3337H15.0007C15.9198 18.3337 16.6673 17.5862 16.6673 16.667V7.50033C16.6673 7.48283 16.6582 7.46699 16.6565 7.44866C16.6524 7.37509 16.6381 7.30245 16.614 7.23283C16.6057 7.20616 16.5982 7.18033 16.5865 7.15533ZM13.8223 6.66699H11.6673V4.51199L13.8223 6.66699ZM5.00065 16.667V3.33366H10.0007V7.50033C10.0007 7.72134 10.0884 7.9333 10.2447 8.08958C10.401 8.24586 10.613 8.33366 10.834 8.33366H15.0007L15.0023 16.667H5.00065Z"
      fill="#667085"
    />
    <path
      d="M6.66602 10.0003H13.3327V11.667H6.66602V10.0003ZM6.66602 13.3337H13.3327V15.0003H6.66602V13.3337ZM6.66602 6.66699H8.33268V8.33366H6.66602V6.66699Z"
      fill="#667085"
    />
  </svg>
`,ui=p`
  <svg
    width="20"
    height="20"
    viewBox="0 0 20 20"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path
      fill-rule="evenodd"
      clip-rule="evenodd"
      d="M12.0294 2.13827L19.6888 15.543C20.5788 17.101 19.4538 19.0401 17.6597 19.0401H2.34088C0.545791 19.0401 -0.579267 17.101 0.311779 15.543L7.97117 2.13827C8.86822 0.567191 11.1323 0.567191 12.0294 2.13827Z"
      fill="#F79009"
    />
    <path
      d="M10.4167 11.45V8.33337"
      stroke="white"
      stroke-width="1.5"
      stroke-linecap="round"
      stroke-linejoin="round"
    />
    <path
      d="M10.4158 13.9542C10.3008 13.9542 10.2075 14.0475 10.2083 14.1625C10.2083 14.2775 10.3017 14.3708 10.4167 14.3708C10.5317 14.3708 10.625 14.2775 10.625 14.1625C10.625 14.0475 10.5317 13.9542 10.4158 13.9542"
      stroke="white"
      stroke-width="1.5"
      stroke-linecap="round"
      stroke-linejoin="round"
    />
  </svg>
`,hn=p`
  <svg
    width="20"
    height="20"
    viewBox="0 0 20 20"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path
      fill-rule="evenodd"
      clip-rule="evenodd"
      d="M10 20V20C4.47667 20 0 15.5233 0 10V10C0 4.47667 4.47667 0 10 0V0C15.5233 0 20 4.47667 20 10V10C20 15.5233 15.5233 20 10 20Z"
      fill="#12B76A"
    />
    <path
      d="M13.6108 8.33337L8.74967 13.1945L5.83301 10.2778"
      stroke="#F6FEF9"
      stroke-width="1.75"
      stroke-linecap="round"
      stroke-linejoin="round"
    />
  </svg>
`,pn=p`
  <svg
    width="20"
    height="20"
    viewBox="0 0 20 20"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path
      fill-rule="evenodd"
      clip-rule="evenodd"
      d="M10 20V20C4.47667 20 0 15.5233 0 10V10C0 4.47667 4.47667 0 10 0V0C15.5233 0 20 4.47667 20 10V10C20 15.5233 15.5233 20 10 20Z"
      fill="#F04438"
    />
    <path
      d="M9.99935 13.5415V9.37488H9.16602"
      stroke="white"
      stroke-width="1.5"
      stroke-linecap="round"
      stroke-linejoin="round"
    />
    <path
      d="M9.78986 6.04159C9.67486 6.04159 9.58153 6.13492 9.58236 6.24992C9.58236 6.36492 9.67569 6.45825 9.79069 6.45825C9.90569 6.45825 9.99903 6.36492 9.99903 6.24992C9.99903 6.13492 9.90569 6.04159 9.78986 6.04159"
      stroke="white"
      stroke-width="1.5"
      stroke-linecap="round"
      stroke-linejoin="round"
    />
  </svg>
`,mn=p`
  <svg
    width="20"
    height="20"
    viewBox="0 0 20 20"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path
      fill-rule="evenodd"
      clip-rule="evenodd"
      d="M10 20V20C4.47667 20 0 15.5233 0 10V10C0 4.47667 4.47667 0 10 0V0C15.5233 0 20 4.47667 20 10V10C20 15.5233 15.5233 20 10 20Z"
      fill="#0045B5"
    />
    <path
      d="M9.99935 13.5415V9.37488H9.16602"
      stroke="white"
      stroke-width="1.5"
      stroke-linecap="round"
      stroke-linejoin="round"
    />
    <path
      d="M9.78986 6.04159C9.67486 6.04159 9.58153 6.13492 9.58236 6.24992C9.58236 6.36492 9.67569 6.45825 9.79069 6.45825C9.90569 6.45825 9.99903 6.36492 9.99903 6.24992C9.99903 6.13492 9.90569 6.04159 9.78986 6.04159"
      stroke="white"
      stroke-width="1.5"
      stroke-linecap="round"
      stroke-linejoin="round"
    />
  </svg>
`,fn=p`
  <svg
    width="24"
    height="24"
    viewBox="0 0 24 24"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path
      d="M8 8L16 16"
      stroke="#667085"
      stroke-width="1.5"
      stroke-linecap="round"
      stroke-linejoin="round"
    />
    <path
      d="M16 8L8 16"
      stroke="#667085"
      stroke-width="1.5"
      stroke-linecap="round"
      stroke-linejoin="round"
    />
  </svg>
`;function gn(t,e){return p`
    <svg
      width=${t}
      height=${e}
      viewBox="0 0 20 20"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
    >
      <path
        fill-rule="evenodd"
        clip-rule="evenodd"
        d="M10 20V20C4.47667 20 0 15.5233 0 10V10C0 4.47667 4.47667 0 10 0V0C15.5233 0 20 4.47667 20 10V10C20 15.5233 15.5233 20 10 20Z"
        fill="#12B76A"
      />
      <path
        d="M13.6108 8.33337L8.74967 13.1945L5.83301 10.2778"
        stroke="#F6FEF9"
        stroke-width="1.75"
        stroke-linecap="round"
        stroke-linejoin="round"
      />
    </svg>
  `}/**
 * @license
 * Copyright 2017 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */const bn={ATTRIBUTE:1,CHILD:2,PROPERTY:3,BOOLEAN_ATTRIBUTE:4,EVENT:5,ELEMENT:6},yn=t=>(...e)=>({_$litDirective$:t,values:e});class vn{constructor(e){}get _$AU(){return this._$AM._$AU}_$AT(e,i,o){this._$Ct=e,this._$AM=i,this._$Ci=o}_$AS(e,i){return this.update(e,i)}update(e,i){return this.render(...i)}}/**
 * @license
 * Copyright 2017 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */class ct extends vn{constructor(e){if(super(e),this.it=D,e.type!==bn.CHILD)throw Error(this.constructor.directiveName+"() can only be used in child bindings")}render(e){if(e===D||e==null)return this._t=void 0,this.it=e;if(e===Z)return e;if(typeof e!="string")throw Error(this.constructor.directiveName+"() called with a non-string value");if(e===this.it)return this._t;this.it=e;const i=[e];return i.raw=i,this._t={_$litType$:this.constructor.resultType,strings:i,values:[]}}}ct.directiveName="unsafeHTML",ct.resultType=1;const xn=yn(ct);var $n=Object.defineProperty,wn=Object.getOwnPropertyDescriptor,w=(t,e,i,o)=>{for(var n=o>1?void 0:o?wn(e,i):e,s=t.length-1,r;s>=0;s--)(r=t[s])&&(n=(o?r(e,i,n):r(n))||n);return o&&n&&$n(e,i,n),n};let $=class extends j{constructor(){super(...arguments),this.memberId="",this.servicesUrl="",this.token="",this.activeStep="documentos",this.loadDataList=!1,this.dataListLots=[],this.pagination={baseQuery:"",pageSize:20,pageNumber:1,sortField:"",sortOrder:"",totalPages:0,numFound:0},this.filterList="",this.filterVehile="",this.filterIsAuction="",this.selectedLots=[],this.modalLotDetail=!1,this.loadDetail=!1,this.dataLotDetail={member:{Erros:[],PendingDocuments:[],ErrosPassiveisDeRevisao:[],OfferOnlineTermPurshase:!1,Detail:{Bairro:"",CEP:"",CPFCNPJ:"",CidadeEstado:"",Complemento:"",Endereco:"",IERG:"",Nome:"",TelefoneCelular:""}},vehicles:[],serviceUrl:""},this.formDocuments=[],this.loadDocuments=!1,this.loadGatePass=!1,this.loadDownloadNote=!1,this.loadRevisao=!1,this.modalFilter=!1,this.modalOnlineTerms=!1}static get styles(){return[ln,Ie]}async firstUpdated(){await this.getLotsWithPendingIssuanceOfSalesNote()}async getLotsWithPendingIssuanceOfSalesNote(){const e=this.filterList===""?null:this.filterList==="true"?!0:this.filterList==="false"?!1:null,i=this.filterIsAuction===""?null:this.filterIsAuction==="true"?!0:this.filterIsAuction==="false"?!1:null;try{this.loadDataList=!0;const o={memberId:this.memberId,pageSize:this.pagination.pageSize,pageNumber:this.pagination.pageNumber,sortField:this.pagination.sortField,sortOrder:this.pagination.sortOrder,lancamentosQuitados:e,isAuction:i,idVeiculo:this.filterVehile},{data:n}=await S(this.servicesUrl,"POST","GetLotsWithPendingIssuanceOfSalesNote",this.token,o);this.dataListLots=n.items,this.pagination={...this.pagination,numFound:n.pagination.numFound,pageSize:n.pagination.pageSize,pageNumber:Number(n.pagination.currentPage),totalPages:n.pagination.totalPages};const s=this.dataListLots.map(r=>({dataVenda:r.DataVenda,idVeiculo:r.IDVeiculo,descricao:r.Descricao,valorTotal:r.ValorTotal,lancamentosQuitados:r.LancamentosQuitados,tipoVenda:r.TipoVenda}));this.dispatchEvent(new CustomEvent("dataPrint",{detail:s})),this.modalFilter=!1,this.loadDataList=!1}catch(o){console.error("Error fetching data:",o)}}handleOnSelectedLots(e,i,o,n,s){const r={IDTipoVendaReferencia:e,IsAuction:i,NotaEmitida:o,LancamentosQuitados:n,TipoVenda:s};this.selectedLots.findIndex(c=>c.IDTipoVendaReferencia===e)>=0?(this.selectedLots=this.selectedLots.filter(c=>c.IDTipoVendaReferencia!==e),this.selectedLots.length===0&&this.getLotsWithPendingIssuanceOfSalesNote()):(this.selectedLots.every(d=>d.TipoVenda===s)||this.selectedLots.length===0)&&(this.selectedLots=[...this.selectedLots,r],this.selectedLots.length===1&&this.getLotsWithPendingIssuanceOfSalesNote()),this.requestUpdate()}formatDatalots(e){const i=this.selectedLots.length>0?this.selectedLots[0].TipoVenda:null;return e.map(n=>{const s=!!this.selectedLots.filter(c=>c.IDTipoVendaReferencia===n.IDTipoVendaReferencia).length,r=i&&n.TipoVenda!==i,a=!n.LancamentosQuitados;return{"-":p`<colibri-common-g2-checkbox
          title=${r?"Tipo é diferente do selecionado":a?"Aguardando Pagamento":""}
          .isChecked=${s}
          .isDisabled=${r||a||!!n.NotaEmitida}
          @on-input=${()=>this.handleOnSelectedLots(n.IDTipoVendaReferencia,n.IsAuction,n.NotaEmitida,n.LancamentosQuitados,n.TipoVenda)}
        ></colibri-common-g2-checkbox>`,IDVeiculo:n.IDVeiculo,DataVenda:n.DataVenda,Descricao:n.Descricao,ValorTotal:di(n.ValorTotal),LancamentosQuitados:p`<colibri-common-g2-badge
          type=${n.LancamentosQuitados?"success":"warning"}
          size="sm"
          text=${n.LancamentosQuitados?"Pagamento concluido":"Aguardando pagamento"}
        ></colibri-common-g2-badge>`,TipoVenda:n.DescricaoTipoVenda,Download:n.NotaEmitida?p`<div
              style="display: grid; place-items: center; width: min-content; margin-left: 12px;"
            >
              <colibri-common-g2-button-icon
                variant="success"
                size="xs"
                .icon=${dn}
                .load=${this.loadDownloadNote}
                .isDisabled=${!n.NotaEmitida}
                @onClick=${()=>this.handleOnDownloadSalesNoteAndReceiptDocument(n.IDTipoVendaReferencia,n.IsAuction)}
              ></colibri-common-g2-button-icon>
            </div> `:null}})}async handleOnChangePagination(e,i){e==="pageSize"&&(this.pagination={...this.pagination,pageNumber:1}),this.pagination={...this.pagination,[e]:i},await this.getLotsWithPendingIssuanceOfSalesNote()}async handleOnVerifyAndGetSalesNoteIssuanceDetails(){try{this.loadDetail=!0;const e={memberId:this.memberId,vehicles:this.selectedLots},{data:i}=await S(this.servicesUrl,"POST","VerifyAndGetSalesNoteIssuanceDetails",this.token,e),o={member:{Erros:i.member.Erros,PendingDocuments:i.member.PendingDocuments,ErrosPassiveisDeRevisao:i.member.ErrosPassiveisDeRevisao,Detail:i.member.Detail,OfferOnlineTermPurshase:i.member.OfferOnlineTermPurshase},serviceUrl:i.serviceUrl,vehicles:i.vehicles};this.dataLotDetail=o}catch(e){console.error("Error fetching data:",e)}finally{this.loadDetail=!1}}handleOnChangeFile(e,i){const o={idTipoAnexo:i,base64Content:e.file.split("base64,")[1],fileExtension:e.data.type.split("/")[1]};if(this.formDocuments.findIndex(s=>s.idTipoAnexo)>=0){const s=this.formDocuments.filter(r=>r.idTipoAnexo!==i);this.formDocuments=[...s,o]}else this.formDocuments=[...this.formDocuments,o]}handleOnClearFile(e){this.formDocuments=this.formDocuments.filter(i=>i.idTipoAnexo!==e)}handleOnCloseModalDetail(){this.formDocuments=[],this.dataLotDetail={member:{Erros:[],PendingDocuments:[],ErrosPassiveisDeRevisao:[],OfferOnlineTermPurshase:!1,Detail:{Bairro:"",CEP:"",CPFCNPJ:"",CidadeEstado:"",Complemento:"",Endereco:"",IERG:"",Nome:"",TelefoneCelular:""}},serviceUrl:"",vehicles:[]},this.modalLotDetail=!1}async handleOnDownloadSalesNoteAndReceiptDocument(e,i){try{this.loadDownloadNote=!0;const o={IDTipoVendaReferencia:e,IsAuction:i},{data:n}=await S(this.servicesUrl,"POST","DownloadSalesNoteAndReceiptDocument",this.token,o),s={name:n.detail.fileName,content:n.detail.content};ie(s)}catch{this.loadDownloadNote=!1}finally{this.loadDownloadNote=!1}}async handleOnDownloadSalesNotesAndReceiptsDocuments(e){try{this.loadDownloadNote=!0;const{data:i}=await S(this.servicesUrl,"POST","DownloadSalesNotesAndReceiptsDocuments",this.token,e);i.files.map(o=>{const n={name:o.fileName,content:o.content};ie(n)})}catch{this.loadDownloadNote=!1}finally{this.loadDownloadNote=!1}}dataBoxMember(e){return[{name:"Comprador",value:this.memberId},{name:"Nome",value:e.Nome},{name:"CPF/CNPJ",value:e.CPFCNPJ},{name:"IERG",value:e.IERG},{name:"Telefone Celular",value:e.TelefoneCelular},{name:"Endereço",value:e.Endereco},{name:"CEP",value:e.CEP},{name:"Bairro",value:e.Bairro},{name:"Cidade - Estado",value:e.CidadeEstado},{name:"Complemento",value:e.Complemento}]}datavehicle(e){const i=this.selectedLots.every(n=>n.NotaEmitida===!0),o=[{name:"Veículo",value:String(e.IDVeiculo)},{name:"Nome",value:String(e.NomeComitente)},{name:"Descrição",value:String(e.Descricao)},...e.Erros.map(n=>({name:"Pendência",value:p`<colibri-common-g2-text
          color="warning-600"
          weight="weight-light"
          >${n}</colibri-common-g2-text
        >`})),{name:"Tipo de Venda",value:e.IsAuction===!0?"Leilão: "+e.DescricaoEvento:"Compre Agora: "+e.DescricaoEvento}];return i&&o.push({name:`Download ${e.IsAuction?"nota de venda":"recibo de venda"} `,value:p`
          <colibri-common-g2-button
            size="xs"
            variant="yellow"
            @onClick=${()=>this.handleOnDownloadSalesNoteAndReceiptDocument(e.IDTipoVendaReferencia,e.IsAuction)}
            .load=${this.loadDownloadNote}
          >
            Download
          </colibri-common-g2-button>
        `}),o}async handleOnUploadDocuments(){try{this.loadDocuments=!0;const e={memberId:this.memberId,documents:this.formDocuments},{data:i}=await S(this.servicesUrl,"POST","UploadPendingMemberDocuments",this.token,e);i.resultCode===0&&(z({title:"Atenção",type:"success",description:"Documentos enviados com sucesso"}),this.handleOnVerifyAndGetSalesNoteIssuanceDetails(),this.formDocuments=[],this.dataLotDetail={member:{Erros:[],PendingDocuments:[],ErrosPassiveisDeRevisao:[],OfferOnlineTermPurshase:!1,Detail:{Bairro:"",CEP:"",CPFCNPJ:"",CidadeEstado:"",Complemento:"",Endereco:"",IERG:"",Nome:"",TelefoneCelular:""}},serviceUrl:"",vehicles:[]},this.formatDatalots(this.dataListLots))}catch(e){console.error("Error fetching data:",e)}finally{this.loadDocuments=!1}}async handleOnGeneratedGatePass(){try{this.loadGatePass=!0;const e={vehicles:this.selectedLots,memberId:this.memberId},{data:i}=await S(this.servicesUrl,"POST","GenerateSalesDocuments",this.token,e);if(i.resultCode===1)throw new Error(i.resultMessage);if(i.resultCode===0){z({title:"Atenção",type:"success",description:"Documento(s) gerado(s) com sucesso"});const o=this.selectedLots.map(n=>({idTipoVendaReferencia:n.IDTipoVendaReferencia,isAuction:n.IsAuction}));setTimeout(()=>{this.handleOnDownloadSalesNotesAndReceiptsDocuments(o)},4e3),this.formDocuments=[],this.dataLotDetail={member:{Erros:[],PendingDocuments:[],ErrosPassiveisDeRevisao:[],OfferOnlineTermPurshase:!1,Detail:{Bairro:"",CEP:"",CPFCNPJ:"",CidadeEstado:"",Complemento:"",Endereco:"",IERG:"",Nome:"",TelefoneCelular:""}},serviceUrl:"",vehicles:[]},this.selectedLots=[],this.modalLotDetail=!1,this.getLotsWithPendingIssuanceOfSalesNote()}}catch(e){console.error("Error fetching data:",e);const i=e;console.error("error",i.message),z({title:"Atencao",type:"warning",description:i.message})}finally{this.loadGatePass=!1}}async handleOnRequestsRegistrationDataReview(e){try{this.loadRevisao=!0;const i={memberId:this.memberId,errosPassiveisDeRevisao:e},{data:o}=await S(this.servicesUrl,"POST","RequestsRegistrationDataReview",this.token,i);if(o.resultCode===1)throw new Error(o.resultMessage);o.resultCode===0&&z({title:"Sucesso",type:"success",description:o.resultMessage})}catch(i){const o=i;console.error("error",o.message),z({title:"Atencao",type:"warning",description:o.message})}finally{this.loadRevisao=!1}}handleOnSortBy(e){const i=e.detail;i.sortBy==="LancamentosQuitados"&&(this.pagination={...this.pagination,sortOrder:i.sortAsc===!0?"desc":"asc",sortField:i.sortBy},this.getLotsWithPendingIssuanceOfSalesNote())}renderErrorMessage(){return this.dataLotDetail.member.Erros.find(e=>e.includes("para entrega no pátio"))?this.dataLotDetail.member.Erros.map(e=>e.includes("para entrega no pátio")?p` <span>${e} <a href="https://${this.dataLotDetail.serviceUrl}/content/br/pt-br/support/faq-topics/index">clicando aqui</a></span> `:p` <span>${e}</span> `):this.dataLotDetail.member.Erros.find(e=>e.includes("Não paga"))?this.dataLotDetail.member.Erros.map(e=>e.includes("Não paga")?p` <span>${e} <a href="https://${this.dataLotDetail.serviceUrl}/myPayments">clicando aqui</a></span> `:p` <span>${e}</span> `):this.dataLotDetail.member.Erros.map(e=>p` <span>${e}</span> `)}handleToggleModalFilter(){this.modalFilter=!1,this.modalOnlineTerms=!1}handleOfferOnlineTermPurchase(){this.modalLotDetail=!1,this.modalFilter=!1,this.modalOnlineTerms=!0}render(){var n;const e=!!this.dataLotDetail.member.PendingDocuments.length||!!this.dataLotDetail.member.Erros.length||!!this.dataLotDetail.member.ErrosPassiveisDeRevisao.length,i=!!((n=this.dataLotDetail.vehicles[0])!=null&&n.Erros.length),o=this.selectedLots.every(s=>s.LancamentosQuitados===!0&&s.NotaEmitida===!1);return p`
      <div class="container-documentation">
        <div class="box">
          <div class="section-box-header">
            <div class="filter-header">
              <div class="field-group">
                <div class="field-filter">
                  <colibri-common-g2-select
                    isLabel="Tipo de Venda"
                    .value=${this.filterList}
                    @on-input=${s=>this.filterIsAuction=s.detail.value}
                    .isChildren=${[{id:0,name:"Selecione uma opção",value:""},{id:1,name:"Compre Agora",value:"false"},{id:2,name:"Leilão",value:"true"}]}
                  ></colibri-common-g2-select>

                  <colibri-common-g2-select
                    isLabel="Status Pagamento"
                    .value=${this.filterList}
                    @on-input=${s=>this.filterList=s.detail.value}
                    .isChildren=${[{id:0,name:"Selecione uma opção",value:""},{id:1,name:"Aguardando pagamento",value:"false"},{id:2,name:"Pagamento concluido",value:"true"}]}
                  ></colibri-common-g2-select>

                  <colibri-common-g2-input
                    isLabel="Código Veículo"
                    isPlaceholder="Busque pelo código"
                    value=""
                    name="codigo"
                    @on-input=${s=>this.filterVehile=s.detail.value}
                  >
                  </colibri-common-g2-input>
                </div>
              </div>
              <div class="selcted-head">
                <colibri-common-g2-button
                  radius="radius-sm"
                  variant="dark"
                  size="xs"
                  class="filter-mobile"
                  @onClick=${this.handleToggleModalFilter}
                >
                  <ph-funnel-simple
                    color="var(--gray-50)"
                    weight="bold"
                    size="18px"
                  ></ph-funnel-simple>
                  Filtrar
                </colibri-common-g2-button>

                <colibri-common-g2-button
                  radius="radius-sm"
                  variant="dark"
                  size="xs"
                  class="filter-desktop"
                  @onClick=${this.getLotsWithPendingIssuanceOfSalesNote}
                >
                  <ph-funnel-simple
                    color="var(--gray-50)"
                    weight="bold"
                    size="18px"
                  ></ph-funnel-simple>
                  Filtrar
                </colibri-common-g2-button>

                <colibri-common-g2-button
                  size="xs"
                  radius="radius-sm"
                  .isDisabled=${!this.selectedLots.length||this.dataLotDetail==null}
                  @onClick=${()=>{this.modalLotDetail=!0,this.handleOnVerifyAndGetSalesNoteIssuanceDetails()}}
                >
                  Emitir
                  ${this.selectedLots.length>0?this.selectedLots.length:""}
                  Documento(s)
                </colibri-common-g2-button>
              </div>
            </div>

            <div class="box-pagination-content">
              <colibri-common-g2-pagination
                .load=${this.loadDataList}
                limit=${this.pagination.pageSize}
                total=${this.pagination.totalPages}
                offset=${this.pagination.pageNumber}
                @row-per-page=${s=>this.handleOnChangePagination("pageSize",s.detail)}
                @my-page-changed=${s=>this.handleOnChangePagination("pageNumber",s.detail.current)}
              >
              </colibri-common-g2-pagination>
            </div>
          </div>

          <div class="section-box-table scroll-bar">
            ${this.loadDataList?p`
                  <colibri-common-g2-load-table></colibri-common-g2-load-table>
                `:p`
                  <colibri-common-g2-table-default
                    .load=${this.loadDataList}
                    .theadData=${an}
                    .tbodyData=${this.formatDatalots(this.dataListLots)}
                    isSort
                    .sortBy=${this.pagination.sortField}
                    @my-sortBy=${s=>this.handleOnSortBy(s)}
                    type="alternate"
                  ></colibri-common-g2-table-default>
                `}
          </div>

          <div class="section-box-filter">
            <div class="box-pagination-content">
              <colibri-common-g2-pagination
                .load=${this.loadDataList}
                limit=${this.pagination.pageSize}
                total=${this.pagination.totalPages}
                offset=${this.pagination.pageNumber}
                @row-per-page=${s=>this.handleOnChangePagination("pageSize",s.detail)}
                @my-page-changed=${s=>this.handleOnChangePagination("pageNumber",s.detail.current)}
              >
              </colibri-common-g2-pagination>
            </div>
          </div>
        </div>

        ${this.modalLotDetail?p`
              <colibri-common-g2-modal
                @on-close=${this.handleOnCloseModalDetail}
                title="Detalhes do lote"
                size="size-lg"
              >
                <div class="dialog-container">
                  ${this.loadDetail?p` <g2-load-modal></g2-load-modal> `:p`
                        <div class="dialog-content bar">
                          <div class="dialog-section-left">
                            <colibri-common-g2-heading weight="weight-bold"
                              >Dados comprador</colibri-common-g2-heading
                            >

                            ${this.dataLotDetail.member.ErrosPassiveisDeRevisao.length?p`
                                  <div class="card-error">
                                    <div class="card-error-alert-icon">
                                      <ph-warning
                                        color="var(--warning-600)"
                                        weight="bold"
                                        size="22"
                                      ></ph-warning>
                                    </div>

                                    <div class="card-error-box-info">
                                      <h1 class="card-error-title">
                                        Divergência no cadastro
                                      </h1>

                                      <div class="card-error-info">
                                        ${this.dataLotDetail.member.ErrosPassiveisDeRevisao.map(s=>p`<span>${xn(s)}</span>`)}
                                      </div>
                                    </div>
                                  </div>
                                `:null}
                            ${this.dataLotDetail.member.Erros.length?p`
                                  <div class="card-error">
                                    <div class="card-error-alert-icon">
                                      <ph-warning
                                        color="var(--warning-600)"
                                        weight="bold"
                                        size="22"
                                      ></ph-warning>
                                    </div>

                                    <div class="card-error-box-info">
                                      <h1 class="card-error-title">
                                        Divergência no cadastro
                                      </h1>

                                      <div class="card-error-info">
                                        ${this.renderErrorMessage()}
                                      </div>
                                    </div>
                                  </div>
                                `:null}
                            ${this.dataLotDetail.member.PendingDocuments.length?p`
                      <div class="upload-docs">
                        <colibri-common-g2-heading weight="weight-bold"
                          >Documentos pendentes de envio</colibri-common-g2-heading
                        >
                        <colibri-common-g2-text size="size-1" color="warning-400">
                        Para emissão da Nota/Recibo de Venda é necessário anexar os seguintes documentos abaixo.
                      </colibri-common-g2-text>
      
                        <div class="upload-docs-form">
                          ${this.dataLotDetail.member.PendingDocuments.map(s=>{var r,a;return p`
                              <div class="field-group">
                                <colibri-common-g2-input
                                  type="file"
                                  isLabel=${s.Item2}
                                  value=${(a=(r=this.formDocuments)==null?void 0:r.filter(c=>c.idTipoAnexo===s.Item1)[0])==null?void 0:a.base64Content}
                                  name="doc"
                                  @on-input=${c=>this.handleOnChangeFile(c.detail.file,s.Item1)}
                                >
                                </colibri-common-g2-input>
                                ${this.formDocuments.filter(c=>c.idTipoAnexo===s.Item1).length?p`
                                      <button
                                        class="button-clear-file"
                                        @click=${()=>this.handleOnClearFile(s.Item1)}
                                      >
                                        <ph-x
                                          color="#F04438"
                                          weight="bold"
                                          size="16px"
                                        ></ph-x>
                                      </button>
                                    `:null}
                              </div>
                            `})}
  
                        </div>
                      </div>
                    </div>
                    `:null}
                            ${!this.dataLotDetail.member.Erros.length&&!this.dataLotDetail.member.PendingDocuments.length&&this.loadDetail===!1?p`
                                  <colibri-common-g2-box
                                    .data=${this.dataBoxMember(this.dataLotDetail.member.Detail)}
                                  >
                                  </colibri-common-g2-box>
                                `:null}
                          </div>

                          <div class="dialog-section-right">
                            <colibri-common-g2-heading weight="weight-bold"
                              >Dados veículo</colibri-common-g2-heading
                            >
                            <div class="dialog-box-group">
                              ${this.dataLotDetail.vehicles.map(s=>p`
                                  <colibri-common-g2-box
                                    .data=${this.datavehicle({...s})}
                                  >
                                  </colibri-common-g2-box>
                                `)}
                            </div>
                          </div>
                        </div>

                        <div class="dialog-footer" style="justify-content: space-between;">
                          <div class="message-warning">
                            ${!i&&!e&&o?p`
                                    <colibri-common-g2-text
                                      size="size-3"
                                      color="warning-400"
                                    >
                                      Ao emitir a nota/recibo de venda, você está
                                      concordando que os seus dados estão corretos.
                                    </colibri-common-g2-text>
                                  `:null}
                          </div>

                          <div class="footer-group">
                            <colibri-common-g2-button
                              size="sm"
                              variant="gray"
                              @onClick=${this.handleOnCloseModalDetail}
                              .isDisabled=${this.loadDocuments}
                              >Cancelar</colibri-common-g2-button
                            >

                            ${this.dataLotDetail.member.PendingDocuments.length?p`
                                  <colibri-common-g2-button
                                    variant="yellow"
                                    .load=${this.loadDocuments}
                                    size="sm"
                                    .isDisabled=${!this.formDocuments.length}
                                    @onClick=${()=>this.handleOnUploadDocuments()}
                                    >Enviar documentos</colibri-common-g2-button
                                  >
                                `:null}

                            ${this.dataLotDetail.member.OfferOnlineTermPurshase?p`
                             <colibri-common-g2-button
                                variant="yellow"
                                .load=${this.loadDocuments}
                                size="sm"
                                @onClick=${()=>this.handleOfferOnlineTermPurchase()}
                                >Autenticação On-line</colibri-common-g2-button
                              >
                            `:null}
                            ${!i&&!e&&o?p`
                                  <colibri-common-g2-button
                                    variant="yellow"
                                    .load=${this.loadGatePass}
                                    size="sm"
                                    .isDisabled=${!!this.formDocuments.length}
                                    @onClick=${()=>this.handleOnGeneratedGatePass()}
                                    >Emitir documento</colibri-common-g2-button
                                  >
                                `:p``}
                            ${this.dataLotDetail.member.ErrosPassiveisDeRevisao.length?p`
                                  <colibri-common-g2-button
                                    variant="yellow"
                                    size="sm"
                                    .load=${this.loadRevisao}
                                    @onClick=${()=>this.handleOnRequestsRegistrationDataReview(this.dataLotDetail.member.ErrosPassiveisDeRevisao)}
                                    >Solicitar revisão</colibri-common-g2-button
                                  >
                                `:null}
                          </div>
                        </div>
                      `}
                </div>
              </colibri-common-g2-modal>
            `:null}
        ${this.modalFilter?p`
              <colibri-common-g2-modal
                @on-close=${this.handleToggleModalFilter}
                title="Filtro"
                size="size-sm"
              >
                <div class="dialog-container">
                  <div class="dialog-content">
                    <div class="field-group">
                      <div class="field-filter">
                        <colibri-common-g2-select
                          isLabel="Tipo de Venda"
                          .value=${this.filterList}
                          @on-input=${s=>this.filterIsAuction=s.detail.value}
                          .isChildren=${[{id:0,name:"Selecione uma opção",value:""},{id:1,name:"Compre Agora",value:"false"},{id:2,name:"Leilão",value:"true"}]}
                        ></colibri-common-g2-select>

                        <colibri-common-g2-select
                          isLabel="Status Pagamento"
                          .value=${this.filterList}
                          @on-input=${s=>this.filterList=s.detail.value}
                          .isChildren=${[{id:0,name:"Selecione uma opção",value:""},{id:1,name:"Aguardando pagamento",value:"false"},{id:2,name:"Pagamento concluido",value:"true"}]}
                        ></colibri-common-g2-select>

                        <colibri-common-g2-input
                          isLabel="Código Veículo"
                          isPlaceholder="Busque pelo código"
                          value=""
                          name="codigo"
                          @on-input=${s=>this.filterVehile=s.detail.value}
                        >
                        </colibri-common-g2-input>
                      </div>
                    </div>
                  </div>

                  <div class="dialog-footer">
                    <colibri-common-g2-button
                      radius="radius-sm"
                      variant="gray"
                      size="xs"
                      @onClick=${this.handleToggleModalFilter}
                    >
                      Cancelar
                    </colibri-common-g2-button>
                    <colibri-common-g2-button
                      radius="radius-sm"
                      variant="dark"
                      size="xs"
                      @onClick=${this.getLotsWithPendingIssuanceOfSalesNote}
                    >
                      <ph-funnel-simple
                        color="var(--gray-50)"
                        weight="bold"
                        size="18px"
                      ></ph-funnel-simple>
                      Filtrar
                    </colibri-common-g2-button>
                  </div>
                </div>
              </colibri-common-g2-modal>
            `:null}

          ${this.modalOnlineTerms?p`
              <colibri-common-g2-modal
                @on-close=${this.handleToggleModalFilter}
                title="Autenticação do termo de responsabilidade"
                size="size-sm">
                  <online-term-purchase
                    .servicesUrl=${this.servicesUrl}
                    .token=${this.token}
                  ></online-term-purchase>
              </colibri-common-g2-modal>`:null}
      </div>
    `}};w([M()],$.prototype,"memberId",2),w([M()],$.prototype,"servicesUrl",2),w([M()],$.prototype,"token",2),w([g()],$.prototype,"activeStep",2),w([g()],$.prototype,"loadDataList",2),w([g()],$.prototype,"dataListLots",2),w([g()],$.prototype,"pagination",2),w([g()],$.prototype,"filterList",2),w([g()],$.prototype,"filterVehile",2),w([g()],$.prototype,"filterIsAuction",2),w([g()],$.prototype,"selectedLots",2),w([g()],$.prototype,"modalLotDetail",2),w([g()],$.prototype,"loadDetail",2),w([g()],$.prototype,"dataLotDetail",2),w([g()],$.prototype,"formDocuments",2),w([g()],$.prototype,"loadDocuments",2),w([g()],$.prototype,"loadGatePass",2),w([g()],$.prototype,"loadDownloadNote",2),w([g()],$.prototype,"loadRevisao",2),w([g()],$.prototype,"modalFilter",2),w([g()],$.prototype,"modalOnlineTerms",2),$=w([De("page-documents")],$);const Cn=ne`
  .container-documentation {
    display: flex;
    flex-direction: column;
  }

  .container-documentation .section-step {
    margin-bottom: 12px;
  }

  .documentation-header {
    display: flex;
    align-items: center;
    justify-content: space-between;

    margin-bottom: 12px;
  }

  .documentation-header h1 {
    font-size: var(--text-headline-lg);
    font-weight: var(--weight-bold);
    color: var(--blue-400);
  }

  .documentation-header .header-actions {
    display: flex;
    align-items: center;
    gap: 12px;

    > a {
      display: flex;
      align-items: center;
      gap: 6px;

      font-size: var(--text-small-sm);
      font-weight: var(--weight-semibold);
      color: var(--gray-700);

      &:hover {
        color: var(--blue-600);
        text-decoration: underline;
      }
    }
  }

  .box {
    overflow: visible;
    border: 1px solid #ddd;
    position: relative;
    border-radius: 4px;

    background-color: #fff;
  }

  .section-box-header {
    display: flex;
    flex-direction: column;
    padding: 8px 10px;
  }

  .section-box-header .filter-header {
    display: flex;
    align-items: flex-end;
    justify-content: end;
    margin-bottom: 10px;
  }

  .section-box-header .selcted-head {
    display: flex;
    align-items: flex-end;
  }

  .section-box-header .filter-header .field-group {
    display: flex;
    align-items: flex-end;
    gap: 1rem;

    .field {
      display: flex;
      flex-direction: column;
      gap: 2px;
    }
  }

  .section-box-filter {
    padding: 8px 10px;
  }


  .section-box-table {
    overflow: auto;
  }

  .section-table {
    display: flex;
    flex-direction: column;
    gap: 12px;
  }

  .dialog-container {
    display: flex;
    flex-direction: column;
    width: clamp(400px, 1000px, 95vw);
    padding-right: 2px;
    overflow: auto;
  }

  .dialog-container .dialog-content {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1rem;
    padding: 12px;
    overflow: auto;
  }

  .dialog-container .dialog-content .dialog-section-left {
    width: 100%;
    border-right: 1px solid var(--gray-100);
    padding-right: 12px;
  }

  .dialog-box-group {
    display: flex;
    flex-direction: column;
    gap: 12px;
    width: 100%;
  }

  .dialog-container .dialog-content .dialog-section-right {
    width: 100%;
  }

  .dialog-container .dialog-footer {
    display: flex;
    align-items: center;
    justify-content: right;
    gap: 12px;

    padding: 12px;
    border-top: 1px solid var(--gray-100);
  }

  .upload-docs {
    display: flex;
    flex-direction: column;
    gap: 8px;
  }

  .upload-docs-form {
    display: flex;
    flex-direction: column;
    gap: 10px;
  }

  .field-group {
    display: flex;
    align-items: center;
    gap: 4px;
  }

  .field-group .button-clear-file {
    display: grid;
    place-items: center;

    border: none;
    background-color: transparent;

    padding: 4px;
    border-radius: 4px;

    margin-top: 21px;
    height: 36px;
    width: 36px;

    &:hover {
      background-color: #fff0f0;
    }
  }
`,Dn=[{id:"-",label:"-",isSort:!1},{id:"IDVeiculo",label:"Código",isSort:!0},{id:"DataVenda",label:"Data da Venda",isSort:!0},{id:"LancamentosQuitados",label:"Estadia Pendente",isSort:!0},{id:"Descricao",label:"Descrição",isSort:!0},{id:"ValorTotal",label:"Valor Total",isSort:!0},{id:"DataValidadeGatePass",label:"Vencimento",isSort:!0},{id:"TipoDocumento",label:"Documento",isSort:!0},{id:"TipoMonta",label:"Monta",isSort:!0},{id:"TipoVenda",label:"Tipo de Venda",isSort:!0}];function Fe(t){const e=new Date(t),i={day:"2-digit",month:"2-digit",year:"numeric"};return new Intl.DateTimeFormat("pt-BR",i).format(e)}var En=Object.defineProperty,Pn=Object.getOwnPropertyDescriptor,I=(t,e,i,o)=>{for(var n=o>1?void 0:o?Pn(e,i):e,s=t.length-1,r;s>=0;s--)(r=t[s])&&(n=(o?r(e,i,n):r(n))||n);return o&&n&&En(e,i,n),n};let k=class extends j{constructor(){super(...arguments),this.memberId="",this.servicesUrl="",this.token="",this.loadDataList=!1,this.dataList=[],this.pagination={baseQuery:"",pageSize:20,pageNumber:1,sortField:"",sortOrder:"",totalPages:0,numFound:0},this.modalGatePass=!1,this.loadGenerateGatePass=!1,this.errorGenerateGatePass="",this.detailGatePass=[],this.selectedLots=[]}static get styles(){return[Cn,Ie]}async firstUpdated(){await this.GetLotsWithPendingIssuanceOfGatePass()}async GetLotsWithPendingIssuanceOfGatePass(){try{this.loadDataList=!0;const t={memberId:this.memberId,pageSize:this.pagination.pageSize,pageNumber:this.pagination.pageNumber,sortField:this.pagination.sortField,sortOrder:this.pagination.sortOrder},{data:e}=await S(this.servicesUrl,"POST","GetLotsWithPendingIssuanceOfGatePass",this.token,t);this.dataList=e.items,this.pagination={...this.pagination,numFound:e.pagination.numFound,pageSize:e.pagination.pageSize,pageNumber:Number(e.pagination.currentPage),totalPages:e.pagination.totalPages};const i=this.dataList.map(o=>({dataVenda:o.DataVenda,idVeiculo:o.IDVeiculo,descricao:o.Descricao,valorTotal:o.ValorTotal,lancamentosQuitados:o.LancamentosQuitados,tipoVenda:o.TipoVenda,dataValidadeGatePass:o.DataValidadeGatePass,tipoDocumento:o.TipoDocumento,tipoMonta:o.TipoMonta,descricaoEvento:o.DescricaoEvento}));this.dispatchEvent(new CustomEvent("dataPrint",{detail:i})),this.loadDataList=!1}catch(t){console.error("Error fetching data:",t)}}async handleOnChangePagination(t,e){t==="pageSize"&&(this.pagination={...this.pagination,pageNumber:1}),this.pagination={...this.pagination,[t]:e},await this.GetLotsWithPendingIssuanceOfGatePass()}handleOnShowDetail(t){this.detailGatePass=t,this.modalGatePass=!this.modalGatePass}handleOnCloseDetail(){this.detailGatePass=[],this.modalGatePass=!this.modalGatePass}async handleOnGenerateGatePass(){try{this.loadGenerateGatePass=!0;const t={vehicles:this.detailGatePass.map(o=>({IDTipoVendaReferencia:o.IDTipoVendaReferencia,IsAuction:o.IsAuction}))},{data:e}=await S(this.servicesUrl,"POST","GenerateGatePass",this.token,t);if(e.resultCode===1)throw this.errorGenerateGatePass=e.resultCode,e.resultMessage;const i={name:e.items[0].FileName,content:e.items[0].Content};ie(i),this.handleOnCloseDetail(),this.GetLotsWithPendingIssuanceOfGatePass()}catch(t){console.error("Error fetching data:",t)}finally{this.loadGenerateGatePass=!1}}handleOnSelectedLots(t,e){const i={...e,IDTipoVendaReferencia:t};if(this.selectedLots.findIndex(n=>n.IDTipoVendaReferencia===t)>=0){const n=this.selectedLots.filter(s=>s.IDTipoVendaReferencia!==t);this.selectedLots=n}else this.selectedLots=[...this.selectedLots,i]}formatDatalots(t){return t.map(i=>({"-":p`<colibri-common-g2-checkbox
      title=${i.LancamentosQuitados?"":"Aguardando Pagamento"}
        .isDisabled=${!i.LancamentosQuitados}
        .isChecked=${!!this.selectedLots.filter(o=>o.IDTipoVendaReferencia===i.IDTipoVendaReferencia).length}
        @on-input=${()=>this.handleOnSelectedLots(i.IDTipoVendaReferencia,i)}
      ></colibri-common-g2-checkbox>`,IDVeiculo:i.IDVeiculo,DataVenda:Fe(i.DataVenda),LancamentosQuitados:p`<colibri-common-g2-badge
        size="sm"
        text=${i.LancamentosQuitados?"Não":"Sim"}
        type=${i.LancamentosQuitados?"success":"orange"}
      ></colibri-common-g2-badge>`,Descricao:i.Descricao,ValorTotal:di(i.ValorTotal),DataValidadeGatePass:Fe(i.DataValidadeGatePass),TipoDocumento:i.TipoDocumento,TipoMonta:i.TipoMonta,TipoVenda:i.TipoVenda+": "+i.DescricaoEvento,Doc:p`
        <div style="margin-left: 32px;">
          <colibri-common-g2-button-icon
            variant="gray"
            size="xs"
            .icon=${un}
          >
          </colibri-common-g2-button-icon>
        </div>
      `}))}dataBoxGatePass(t,e){return[{name:"Dados Gatepass",value:`${e+1}`},{name:"Veículo",value:t.IDVeiculo},{name:"Data Venda",value:Fe(t.DataVenda?t.DataVenda:Date())},{name:"Vencimento",value:Fe(t.DataValidadeGatePass?t.DataValidadeGatePass:Date())},{name:"Tipo de Venda",value:t.IsAuction===!0?"Leilão: "+t.DescricaoEvento:"Compre Agora: "+t.DescricaoEvento},{name:"Descrição",value:t.DescricaoResumida}]}render(){return p`
      <div class="container-documentation">
        <div class="box">
          <div class="section-box-header">
            <div class="filter-header">
              <div class="selcted-head">
                <colibri-common-g2-button
                  size="xs"
                  radius="radius-sm"
                  .isDisabled=${!this.selectedLots.length}
                  @onClick=${()=>this.handleOnShowDetail(this.selectedLots)}
                >
                  Emitir ${this.selectedLots.length>0?this.selectedLots.length:""} Documento(s) 
                  
                </colibri-common-g2-button>
              </div>
            </div>

            <div class="box-pagination-content">
              <colibri-common-g2-pagination
                .load=${this.loadDataList}
                limit=${this.pagination.pageSize}
                total=${this.pagination.totalPages}
                offset=${this.pagination.pageNumber}
                @row-per-page=${t=>this.handleOnChangePagination("pageSize",t.detail)}
                @my-page-changed=${t=>this.handleOnChangePagination("pageNumber",t.detail.current)}
              >
              </colibri-common-g2-pagination>
            </div>
          </div>

          <div class="section-box-table scroll-bar">
            ${this.loadDataList?p`
                  <colibri-common-g2-load-table></colibri-common-g2-load-table>
                `:p`
                  <colibri-common-g2-table-default
                    .load=${this.loadDataList}
                    .theadData=${Dn}
                    .tbodyData=${this.formatDatalots(this.dataList)}
                    isSort
                    type="alternate"
                  ></colibri-common-g2-table-default>
                `}
          </div>

          <div class="section-box-filter">
            <div class="box-pagination-content">
              <colibri-common-g2-pagination
                .load=${this.loadDataList}
                limit=${this.pagination.pageSize}
                total=${this.pagination.totalPages}
                offset=${this.pagination.pageNumber}
                @row-per-page=${t=>this.handleOnChangePagination("pageSize",t.detail)}
                @my-page-changed=${t=>this.handleOnChangePagination("pageNumber",t.detail.current)}
              >
              </colibri-common-g2-pagination>
            </div>
          </div>
        </div>

        ${this.modalGatePass?p`
          <colibri-common-g2-modal
            title="Detalhe Gatepass"
            @on-close=${this.handleOnCloseDetail}
          >
            <div class="dialog-container">
              <div class="dialog-content bar">
                ${this.errorGenerateGatePass?p`
                      <card-message
                        .messages=${[{title:"Atenção",message:this.errorGenerateGatePass}]}
                        type="warning"
                      ></card-message>
                    `:null}
  
                <div class="dialog-box-group">
                  ${this.detailGatePass.map((t,e)=>p`
                      <colibri-common-g2-box
                        .data=${this.dataBoxGatePass(t,e)}
                      >
                      </colibri-common-g2-box>
                    `)}
                </div>
              </div>
              <div class="dialog-footer">
                <colibri-common-g2-button
                  .load=${this.loadGenerateGatePass}
                  size="sm"
                  variant="yellow"
                  @onClick=${()=>this.handleOnGenerateGatePass()}
                >
                  Baixar Gatepass
                </colibri-common-g2-button>
              </div>
            </div>
          </colibri-common-g2-modal>
          `:null}

      </div>
    `}};I([M()],k.prototype,"memberId",2),I([M()],k.prototype,"servicesUrl",2),I([M()],k.prototype,"token",2),I([g()],k.prototype,"loadDataList",2),I([g()],k.prototype,"dataList",2),I([g()],k.prototype,"pagination",2),I([g()],k.prototype,"modalGatePass",2),I([g()],k.prototype,"loadGenerateGatePass",2),I([g()],k.prototype,"errorGenerateGatePass",2),I([g()],k.prototype,"detailGatePass",2),I([g()],k.prototype,"selectedLots",2),k=I([De("page-gate-pass")],k);const Sn=ne`
  :root{
    display: flex;
    flex-direction: column;
    height: 100%;
  }

  .container-documentation {
    display: flex;
    flex-direction: column;
  }

  .container-documentation .section-step {
    margin-bottom: 12px;
  }

  .documentation-header {
    display: flex;
    align-items: center;
    justify-content: space-between;

    margin-bottom: 12px;
  }

  .documentation-header h1 {
    font-size: var(--text-headline-lg);
    font-weight: var(--weight-bold);
    color: red;
  }

  .documentation-header .header-actions {
    display: flex;
    align-items: center;
    gap: 12px;

    > a {
      display: flex;
      align-items: center;
      gap: 6px;

      font-size: var(--text-small-sm);
      font-weight: var(--weight-semibold);
      color: var(--gray-700);

      &:hover {
        color: var(--blue-600);
        text-decoration: underline;
      }
    }
  }

  .box {
    overflow: visible;
    border: 1px solid #ddd;
    position: relative;
    border-radius: 4px;

    background-color: #fff;
  }

  .section-box-header {
    display: flex;
    flex-direction: column;
    padding: 8px 10px;
  }

  .section-box-header .filter-header {
    display: flex;
    align-items: flex-end;
    justify-content: space-between;
    margin-bottom: 10px;
    gap: 12px;
  }

  @media (max-width: 620px) {
    .filter-header {
      flex-direction: column;
    }
  }

  .section-box-header .selcted-head {
    display: flex;
    align-items: flex-end;
    gap: 6px;

    .filter-mobile {
      display: none;
    }

    @media (max-width: 620px) {
      .filter-desktop {
        display: none;
      }
    }

    @media (max-width: 620px) {
      .filter-mobile {
        display: block
      }
    }
  }

  .section-box-header .filter-header .field-group {
    display: flex;
    align-items: flex-end;
    gap: 1rem;
    width: 100%;

    .field-filter {
      display: flex;
      gap: 12px;
      flex-direction: row;
    }

    @media (max-width: 620px) {
      display: none;
      .field-filter {
        flex: 1;
        flex-direction: column;
        align-items: baseline;
      }
    }
  }

  .section-box-filter {
    padding: 8px 10px;
  }

  .section-box-table {
    overflow: auto;
  }

  .dialog-container {
    display: flex;
    flex-direction: column;
    width: clamp(400px, 1000px, 95vw);
    padding-right: 2px;
    overflow: auto;

    @media (max-width: 620px) {
      width: 100%;
    }
    
  }

  .dialog-container .dialog-content {
    display: grid;
    grid-template-columns: 1fr;
    gap: 1rem;
    margin-bottom: 12px;
    padding: 12px 0px 0px 12px;
    overflow: auto;

    @media (max-width: 620px) {
      grid-template-columns: 1fr;
    }
  }

  .dialog-container .dialog-content .dialog-section-left {
    width: 100%;
    border-right: 1px solid var(--gray-100);
    padding-right: 12px;
  }

  .dialog-box-group {
    display: flex;
    flex-direction: column;
    gap: 12px;
  }

  .dialog-container .dialog-content .dialog-section-right {
    width: 100%;
  }

  .dialog-container .dialog-footer {
    display: flex;
    align-items: center;
    justify-content: right;
    gap: 12px;

    padding: 12px;
    border-top: 1px solid var(--gray-100);
  }

  .footer-group {
    display: flex;
    gap: 12px;
  }

  .dialog-container .card-error {
    display: flex;
    align-items: center;
    gap: 1rem;

    padding: 8px;

    border-radius: 4px;
    border-top: 1px;
    border-right: 1px;
    border-bottom: 1px;
    border-left: 4px;
    border-color: #f79009;
    border-style: solid;
    background-color: #fffcf5;
    margin-bottom: 1rem;
    margin-top: 6px;
  }

  .dialog-container .field-group {
    display: flex;
    align-items: flex-end;
    gap: 1rem;
    width: 100%;

    .field-filter {
      display: flex;
      flex-direction: column;
      gap: 12px;
      flex: 1;
    }
  }

  .dialog-container .card-error .card-error-alert-icon {
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .dialog-container .card-error .card-error-box-info {
    display: flex;
    flex-direction: column;
    gap: 4px;
  }

  .dialog-container .card-error .card-error-box-info .card-error-title {
    font-size: 1rem;
    font-weight: 700;
    color: #b54708;
  }

  .dialog-container .card-error .card-error-box-info .card-error-info {
    display: flex;
    flex-direction: column;
  }

  .dialog-container .card-error .card-error-box-info .card-error-info span {
    font-size: 14px;
    font-weight: 600;
    color: #b54708;
  }

  .upload-docs {
    display: flex;
    flex-direction: column;
    gap: 8px;
  }

  .upload-docs-form {
    display: flex;
    flex-direction: column;
    gap: 10px;
  }

  .field-group {
    display: flex;
    align-items: center;
    gap: 4px;
  }

  .card-error-info a {
    text-decoration: underline;
  }

  .card-error-info a:hover {
    color: var(--blue-600);
  }

  .field-group .button-clear-file {
    display: grid;
    place-items: center;

    border: none;
    background-color: transparent;

    padding: 4px;
    border-radius: 4px;

    margin-top: 21px;
    height: 36px;
    width: 36px;

    &:hover {
      background-color: #fff0f0;
    }
  }

  .introduction-content{
    display: flex;
    flex-direction: column;
    align-items: center;
    height: 50vh;
  }

  .text-container{
    font-size: var(--text-small-sm);
    font-weight: var(--weight-medium);
    color: var(--gray-500);
    height: 90%;
    overflow-y: scroll;
    width: 100%;
    margin: 30px;

    @media (max-width: 620px) {
      width: 90%;        
      overflow-y: scroll;
      max-height: 49vh;
    }
  }

  .form-title{
    display: flex;
    flex-direction: column;
    align-items: center;
    border-bottom: 1px solid var(--gray-100);
  }

  .legal-representative-container{
    font-size: var(--text-small-sm);
    font-weight: var(--weight-medium);
    color: var(--gray-500);

    display: grid;
    grid-template-columns: repeat(3, 1fr);

    gap: 1rem;
    padding: 12px;

    @media (max-width: 620px) {
      grid-template-columns: 1fr;
      overflow-y: scroll;
      max-height: 49vh;
      gap: .5rem;
    }
  }

  .form-container{
    font-size: var(--text-small-sm);
    font-weight: var(--weight-medium);
    color: var(--gray-500);

    display: grid;
    grid-template-columns: repeat(3, 1fr);

    gap: 1rem;
    padding: 12px;

    @media (max-width: 620px) {
      grid-template-columns: 1fr;
      overflow-y: scroll;
      max-height: 49vh;
      gap: .5rem;
    }
  }

  .footer-content{
    border-top: 1px solid var(--gray-100);
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .amount-container{
    display: flex;
    align-items: center;
    justify-content: right;
    gap: 12px;
    padding: 12px;
  }

  .buttons-container{
    display: flex;
    align-items: center;
    justify-content: right;
    gap: 12px;
    padding: 12px;

    @media (max-width: 620px) {
      grid-template-columns: repeat(2, 1fr);
    }
  }

  .purchase-content{
    display: flex;
    flex-direction: column;
    align-items: center;
    overflow: hidden;
  }

  .pix-modal{
    display: flex;
    align-items: center;

    @media (max-width: 620px) {
      .wait-logo{
        height: 60vh;
      }
    }
  }

  .thank-you-title{
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .thank-you-container{
    display: flex;
    justify-content: center;
    gap: 2rem;

    @media (max-width: 620px) {
      .wait-logo{
       display: none;
      }
    }
  }

  .thank-you-text{
    display: flex;
    align-items: center;
    width: 30vw;
    font-size: 14pt;
    text-align: justify;
    padding: 20px;

    @media (max-width: 620px) {
      width: 100%;
    }
  }

  .hidden{
    display: none !important;
  }

  .accept-term-container{
    display: flex;
    font-size: var(--text-small-sm);
    font-weight: var(--weight-medium);
    color: var(--gray-600);
    flex-direction: column;
  }

  ::-webkit-scrollbar {
    width: 4px;
    height: 5px;
}
  ::-webkit-scrollbar-thumb {
      background-color: var(--gray-400);
      border-radius: 2px;
  }
  
  ::-webkit-scrollbar-track {
      background: transparent;
}
`;function hi(t){let e=t;return e=e.replace(/[^a-zA-Z ]/g,""),t=e,t}function Me(t){let e=t.replace(/\D/g,"");if(t.length<12)e=e.replace(/(\d{3})(\d)/,"$1.$2"),e=e.replace(/(\d{3})(\d)/,"$1.$2"),e=e.replace(/(\d{3})(\d{2})$/,"$1-$2");else{const i=/^(\d{2})(\d{3})(\d{3})(\d{4})(\d{2})$/;e=e.replace(i,"$1.$2.$3/$4-$5")}return e}function pi(t){let e=t;e=e.replace(/\D/g,"");const i=/^(\d{5})(\d{0,4})?$/;return e=e.replace(i,"$1-$2"),t=e,t}function Ue(t){const e=t.replace(/\D/g,""),i=/^(\d{2})(\d{4,5})(\d+)$/;return e.replace(i,"($1) $2-$3")}var Ln=Object.defineProperty,Rn=Object.getOwnPropertyDescriptor,L=(t,e,i,o)=>{for(var n=o>1?void 0:o?Rn(e,i):e,s=t.length-1,r;s>=0;s--)(r=t[s])&&(n=(o?r(e,i,n):r(n))||n);return o&&n&&Ln(e,i,n),n};let P=class extends j{constructor(){super(...arguments),this.servicesUrl="",this.token="",this.currentStep=0,this.hasFormErrors=!0,this.acceptTerms=!1,this.notifyBy="",this.isLoad=!1,this.isLoadCep=!1,this.isLoadCities=!1,this.signer={Nome:"",CPFCNPJ:"",IERG:"",CNH:"",Celular:"",DtNascimento:"",Logradouro:"",Numero:"",Complemento:"",Bairro:"",Cidade:"",IDMunicipio:0,UF:"",CEP:"",TipoPessoa:0,CNHRepresentanteLegal:"",CPFRepresentanteLegal:"",RazaoRepresentanteLegal:"",RGRepresentanteLegal:"",TelefoneRepresentanteLegal:"",EmailRepresentanteLegal:""},this.hasInvalidCep=!1,this.serviceAmount="",this.signingByOptions=[],this.ufOptions=[],this.citiesOptions=[],this.canEditBirthDate=!1,this.isPaid=!1}static get styles(){return[Sn,Ie]}async firstUpdated(){await this.getMemberDetail(),await this.requestStates(),window.innerWidth>620&&(this.hasFormErrors=!1)}async getMemberDetail(){this.isLoad=!0;try{const{data:t}=await S(this.servicesUrl,"GET","GetMemberDataOnlinePurchase",this.token);if(t.ResultCode===1)throw new Error(t.resultMessage);if(t.ResultCode===0){const e={Nome:t.MemberData.Nome,CPFCNPJ:t.MemberData.CPFCNPJ,Telefone:t.MemberData.Telefone,Email:t.MemberData.Email,IERG:t.MemberData.IERG,CNH:t.MemberData.CNH,Celular:t.MemberData.Celular,DtNascimento:t.MemberData.DtNascimento,Logradouro:t.MemberData.Logradouro,Numero:t.MemberData.Numero,Complemento:t.MemberData.Complemento,Bairro:t.MemberData.Bairro,Cidade:t.MemberData.Cidade,IDMunicipio:t.MemberData.IDMunicipio,UF:t.MemberData.UF,CEP:t.MemberData.CEP,TipoPessoa:t.MemberData.CPFCNPJ.length>11?1:0,CNHRepresentanteLegal:"",CPFRepresentanteLegal:"",RazaoRepresentanteLegal:"",RGRepresentanteLegal:"",TelefoneRepresentanteLegal:"",EmailRepresentanteLegal:""};(t.MemberData.DtNascimento==null||t.MemberData.DtNascimento=="")&&(this.canEditBirthDate=!0),this.cepResponse={streetName:t.MemberData.Logradouro,neighborhood:t.MemberData.Bairro,cityDescription:t.MemberData.Cidade,cityId:t.MemberData.IDMunicipio,state:t.MemberData.UF},this.requestCities(t.MemberData.UF),this.serviceAmount=t.ServiceAmount,this.signer=e,this.signingByOptions=t.OpcoesAssinatura.map(i=>({id:i.Value,value:i.Value,name:i.Label})),this.signingByOptions.unshift({id:"",value:"",name:"Selecione uma Opção..."})}}catch(t){const e=t;console.error("error",e.message),z({title:"Atencao",type:"warning",description:e.message})}finally{this.isLoad=!1}}async requestPurchase(){this.isLoad=!0;let t={signerName:this.signer.Nome,signerCPFCNPJ:this.signer.CPFCNPJ.replace(/\D/g,""),signerIERG:this.signer.IERG,signerCNH:this.signer.CNH,signerPhoneNumber:this.signer.Celular.replace(" ","").replace(/\D/g,""),SignerBirthDate:this.signer.DtNascimento,signerAddress:this.signer.Logradouro,signerAddressNumber:this.signer.Numero,signerNeighborhood:this.signer.Bairro,signerComplement:this.signer.Complemento,signerZipCode:this.signer.CEP,signerCityId:this.signer.IDMunicipio,legalRepresentativeName:this.signer.RazaoRepresentanteLegal,legalRepresentativeCPF:this.signer.CPFRepresentanteLegal.replace(/\D/g,""),legalRepresentativeRG:this.signer.RGRepresentanteLegal.replace(/\D/g,""),legalRepresentativeCNH:this.signer.CNHRepresentanteLegal.replace(/\D/g,""),legalRepresentativePhoneNumber:this.signer.TelefoneRepresentanteLegal.replace(/\D/g,""),legalRepresentativeEmail:this.signer.EmailRepresentanteLegal,notifyBy:this.notifyBy};try{const{data:e}=await S(this.servicesUrl,"POST","RequestSignTermsAndConditions",this.token,t);if(e.resultCode===1)throw new Error(e.resultMessage);e.resultCode===0&&(this.purshadeData={...e.invoice,Items:e.Items})}catch(e){const i=e;console.error("error",i.message),this.backStepClick(),z({title:"Atencao",type:"warning",description:i.message})}finally{this.isLoad=!1}}async requestCepDetail(t){this.isLoadCep=!0,this.hasInvalidCep=!1;let e={zipCode:t};try{const{data:i}=await S(this.servicesUrl,"POST","SearchZipCode",this.token,e,"G2Member");i.resultCode===-1&&(this.hasInvalidCep=!0,this.cepResponse={streetName:"",neighborhood:"",cityDescription:"",cityId:0,state:""},this.signer={...this.signer,CEP:"",Logradouro:"",Bairro:"",Cidade:"",IDMunicipio:0,UF:"",Numero:"",Complemento:""}),i.resultCode===0&&(this.cepResponse=i.zipCodeDetails,this.requestCities(i.zipCodeDetails.state),this.signer={...this.signer,CEP:t,Logradouro:i.zipCodeDetails.streetName,Bairro:i.zipCodeDetails.neighborhood,Cidade:i.zipCodeDetails.cityDescription,IDMunicipio:i.zipCodeDetails.cityId,UF:i.zipCodeDetails.state,Numero:"",Complemento:""})}catch(i){z({title:"Atencao",type:"warning",description:i.message})}finally{this.isLoadCep=!1}}async requestStates(){try{const{data:t}=await S(this.servicesUrl,"GET","GetAllStates",this.token);if(t.ResultCode===-1)throw new Error("Erro ao buscar os estados");t.ResultCode===0&&(this.ufOptions=t.Response.map(e=>({id:e.id,value:e.value,name:e.name})),this.ufOptions.unshift({id:"",value:"",name:"Selecione um opção"}))}catch(t){z({title:"Atencao",type:"warning",description:t.message})}finally{this.isLoadCep=!1}}async requestCities(t){this.isLoadCities=!0;try{const{data:e}=await S(this.servicesUrl,"GET",`GetCitiesByState?sigla=${t}`,this.token);if(e.ResultCode===-1)throw new Error("Erro ao buscar os estados");e.ResultCode===0&&(this.citiesOptions=e.Response.map(i=>({id:i.id.toString(),value:i.value.toString(),name:i.name})),this.citiesOptions.unshift({id:"",value:"",name:"Selecione um opção"}))}catch(e){z({title:"Atencao",type:"warning",description:e.message})}finally{this.isLoadCities=!1}}nextStepClick(){this.currentStep++,this.verifyStep(this.currentStep,!0)}backStepClick(){this.hasFormErrors=!1,this.currentStep--,this.verifyStep(this.currentStep,!1)}verifyStep(t,e){switch(t){case 2:{this.signer.TipoPessoa==0&&(this.acceptTerms=!1),this.signer.TipoPessoa==0&&e&&(this.currentStep++,this.verifyStep(this.currentStep,e)),this.signer.TipoPessoa==0&&!e&&(this.currentStep--,this.verifyStep(this.currentStep,e));break}case 3:this.requestPurchase();break}}render(){return p`
        <div class="dialog-container">
        ${this.isLoad||!this.serviceAmount?p`<g2-load-modal></g2-load-modal>`:p`
            <div class="dialog-content">
                ${this.renderCurrentStep()}
            </div>
            <div class="footer-content">
              <div class="amount-container">
                ${this.currentStep==0?p`
                    <colibri-common-g2-badge
                      .size=${"lg"}
                      type='warning'
                      .text=${`Valor do Serviço: ${this.serviceAmount}`}
                    ></colibri-common-g2-badge>
                  `:null}
              </div>
              <div class="buttons-container ${this.currentStep>2?"hidden":""}">
                <colibri-common-g2-button
                  size="sm"
                  variant="gray"
                  .hidden=${this.currentStep==0}
                  @onClick=${this.backStepClick}
                >
                  Voltar 
                </colibri-common-g2-button>
                <colibri-common-g2-button
                  size="sm"
                  .isDisabled=${this.canDisableNextButton()}
                  @onClick=${this.nextStepClick}
                >
                  ${this.getNameButton()} 
                </colibri-common-g2-button>
              </div>
            </div>
        `}
        </div>
      `}canDisableNextButton(){return!!(this.hasFormErrors||this.currentStep!=0&&!this.acceptTerms)}getNameButton(){return this.currentStep==1&&this.signer.TipoPessoa==0||this.currentStep==2?p`
        Finalizar Pagamento
      `:"Avançar"}renderCurrentStep(){switch(this.currentStep){case 0:return this.renderIntroductionStep();case 1:return this.renderFormStep();case 2:return this.renderLegalRepresentativeStep();case 3:return this.renderPurchaseStep();case 4:return this.renderThankYouStep()}}renderIntroductionStep(){var e;let t=parseFloat((e=this.serviceAmount)==null?void 0:e.replace("R$","").replace(",","."));return this.serviceAmount?p`
      <div class="introduction-content">
          <colibri-common-g2-heading weight="weight-bold">
            Informações Importantes
          </colibri-common-g2-heading>
          <colibri-common-g2-ui-textarea 
            id="aceept-term" 
            class="text-container"
            isReadOnly=${!0}
            @on-scroll=${this.handleScroll}
            value="
              - O Termo de Responsabilidade, com assinatura física reconhecida por um tabelião ou com assinatura eletrônica/digital em conformidade com as disposições legais e certificada através do ICP-Brasil, é um documento obrigatório para emissão de nota/recibo de venda de veículos adquiridos através dos Leilões ou Compre Agora.
              
              - Para os interessados, informamos que o serviço de assinatura eletrônica do Termo de Responsabilidade poderá ser adquirido nessa plataforma pelo valor de ${this.serviceAmount} (${this.valorPorExtenso(t)}) a ser pago via PIX, através do código aleatório a ser disponibilizado no ato do registro da contratação. O serviço será realizado por meio de uma plataforma de assinatura eletrônica em conformidade com as disposições legais. 
            
              - Após realizar a contratação do serviço de assinatura e certificação digital com o efetivo pagamento, não será possível solicitar o cancelamento e o contratante deverá seguir as instruções para concluir a assinatura eletrônica.
            
              - A nota fiscal do serviço de assinatura eletrônica será emitida respeitando os dados cadastrais informados pelo comprador, seja pessoa física ou pessoa jurídica representada legalmente.
            
              - Atenção para os prazos de assinatura, pois o comprador terá que observar o prazo descrito nas Condições de Venda para a emissão de nota/recibo de venda que serão emitidos somente com a apresentação do Termo de Responsabilidade devidamente assinado, seja com o reconhecimento de firma ou por meio de assinatura eletrônica com certificação de autenticidade."
            ></colibri-common-g2-ui-textarea>
      </div>
    `:null}handleScroll(t){const{scrollTop:e,scrollHeight:i,clientHeight:o}=t.detail;e+o>=i&&(this.hasFormErrors=!1)}valorPorExtenso(t){if(t<0||t>=1e9)return"Valor fora do limite suportado";const e=["","um","dois","três","quatro","cinco","seis","sete","oito","nove"],i=["dez","onze","doze","treze","quatorze","quinze","dezesseis","dezessete","dezoito","dezenove"],o=["","","vinte","trinta","quarenta","cinquenta","sessenta","setenta","oitenta","noventa"],n=["","cem","duzentos","trezentos","quatrocentos","quinhentos","seiscentos","setecentos","oitocentos","novecentos"];function s(d){if(d===0)return"";if(d<10)return e[d];if(d<20)return i[d-10];if(d<100)return o[Math.floor(d/10)]+(d%10!==0?" e "+e[d%10]:"");if(d<1e3){let u=Math.floor(d/100),h=d%100;return(u===1&&h>0?"cento":n[u])+(h!==0?" e "+s(h):"")}if(d<1e6){let u=Math.floor(d/1e3),h=d%1e3;return(u>1?s(u)+" mil":"mil")+(h!==0?" "+s(h):"")}if(d<1e9){let u=Math.floor(d/1e6),h=d%1e6;return(u>1?s(u)+" milhões":"um milhão")+(h!==0?" "+s(h):"")}return"Valor muito alto"}const r=Math.floor(t),a=Math.round((t-r)*100);let c=r>0?s(r)+(r===1?" real":" reais"):"";if(a>0){let d=s(a)+(a===1?" centavo":" centavos");c+=c?" e "+d:d}return c||"zero reais"}handleChange(t){let{name:e,value:i}=t.detail;if(this.hasFormErrors=!1,e=="Aceite"){this.acceptTerms=i;return}if(e=="Notificacao"){this.notifyBy=i;return}e=="UF"&&this.requestCities(i),this.signer={...this.signer,[e]:i}}isValidMultiWord(t){return/^\s*\S+(?:\s+\S+)+\s*$/.test(t)}validErrorsForm(t){const e={Nome:{errorMessage:"Nome é de preenchimento obrigatório"},CNH:{errorMessage:"CNH é de preenchimento obrigatório"},Celular:{errorMessage:"Celular é de preenchimento obrigatório"},CEP:{errorMessage:"CEP é de preenchimento obrigatorio"},Logradouro:{errorMessage:"Logradouro é de preenchimento obrigatório"},Numero:{errorMessage:"Numero é de preenchimento obrigatório"},RazaoRepresentanteLegal:{errorMessage:"Nome do Representante Legal é de preenchimento obrigatório"},CPFRepresentanteLegal:{errorMessage:"CPF é de preenchimento obrigatório"},CNHRepresentanteLegal:{errorMessage:"CNH é de preenchimento obrigatório"},RGRepresentanteLegal:{errorMessage:"RG é de preenchimento obrigatório"},TelefoneRepresentanteLegal:{errorMessage:"Telefone é de preenchimento obrigatório"},EmailRepresentanteLegal:{errorMessage:"E-mail é de preenchimento obrigatório"},Aceite:{errorMessage:"É necessário dar o aceite para continuar"},Notificacao:{errorMessage:"Escolha alguma opção para continuar com a autenticação"},UF:{errorMessage:"UF é de preenchimento obrigatório"},IDMunicipio:{errorMessage:"Cidade é de preenchimento obrigatório"},DtNascimento:{errorMessage:"Data de nascimento é de preenchimento obrigatório"}},i=this.signer;switch(t){case"Nome":if(this.signer.TipoPessoa==0&&!this.isValidMultiWord(this.signer.Nome))return this.hasFormErrors=!0,e[t].errorMessage;break;case"RazaoRepresentanteLegal":if(this.signer.TipoPessoa==1&&!this.isValidMultiWord(this.signer.RazaoRepresentanteLegal))return this.hasFormErrors=!0,e[t].errorMessage;break;case"Aceite":if(!this.acceptTerms)return this.hasFormErrors=!0,e[t].errorMessage;break;case"CNH":if(this.signer.TipoPessoa==0&&this.signer.CNH.replace(/\D/g,"").length<11)return this.hasFormErrors=!0,e[t].errorMessage;break;case"CPFRepresentanteLegal":{if(this.signer.TipoPessoa==1&&this.signer.CPFRepresentanteLegal.replace(/\D/g,"").length<11)return this.hasFormErrors=!0,e[t].errorMessage;if(!this.validarCPF(this.signer.CPFRepresentanteLegal.replace(/\D/g,"")))return this.hasFormErrors=!0,"CPF está inválido"}break;case"CNHRepresentanteLegal":if(this.signer.TipoPessoa==1&&this.signer.CNHRepresentanteLegal.replace(/\D/g,"").length<11)return this.hasFormErrors=!0,e[t].errorMessage;break;case"TelefoneRepresentanteLegal":if(this.signer.TipoPessoa==1&&this.signer.TelefoneRepresentanteLegal.replace(/\D/g,"").length<11)return this.hasFormErrors=!0,e[t].errorMessage;break;case"Celular":if(this.signer.TipoPessoa==0&&this.signer.Celular.replace(/\D/g,"").length<11)return this.hasFormErrors=!0,e[t].errorMessage;break;case"EmailRepresentanteLegal":if(this.signer.TipoPessoa==1&&!this.validaEmail(this.signer.EmailRepresentanteLegal))return this.hasFormErrors=!0,e[t].errorMessage;break;case"Notificacao":if(this.notifyBy=="")return this.hasFormErrors=!0,e[t].errorMessage;break;case"IDMunicipio":if(this.signer.IDMunicipio==0)return this.hasFormErrors=!0,e[t].errorMessage;break;case"CEP":if(this.hasInvalidCep)return"CEP inválido";break;case"DtNascimento":if(this.signer.TipoPessoa==0&&this.signer.DtNascimento.length!=10)return this.hasFormErrors=!0,e[t].errorMessage;break;default:if(i[t]!=null&&i[t].length==0)return this.hasFormErrors=!0,e[t].errorMessage}}validaEmail(t){return/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(t)}validarCPF(t){if(t=t.replace(/\D/g,""),t.length!==11||/^(\d)\1+$/.test(t))return!1;const e=n=>{let s=0;for(let a=0;a<n;a++)s+=parseInt(t[a])*(n+1-a);let r=s%11;return r<2?0:11-r},i=e(9),o=e(10);return i===parseInt(t[9])&&o===parseInt(t[10])}handleCepChange(t){const{value:e}=t.detail;e.replace(/\D/g,"").length==8&&this.requestCepDetail(e)}renderFormStep(){var t,e,i,o,n;return p`
      <div class="form-title">
          <colibri-common-g2-heading weight="weight-bold">
            Informações do Cadastro
          </colibri-common-g2-heading>
      </div>
      <div class="form-container">
        <colibri-common-g2-input
          name="Nome"
          .isLabel=${this.signer.TipoPessoa==0?"Nome Completo":"Razão"}
          .isDisabled=${this.signer.TipoPessoa==1}
          .value=${this.signer.Nome}
          .error=${this.validErrorsForm("Nome")}
          .isPlaceholder=${"Digite o nome completo"}
          .isMask=${hi}
          @on-input=${s=>this.handleChange(s)}
        ></colibri-common-g2-input>
        <colibri-common-g2-input
          .isLabel=${this.signer.TipoPessoa==0?"CPF":"CNPJ"}
          .isDisabled=${!0}
          .value=${Me(this.signer.CPFCNPJ)}
          .isMask=${Me}
        ></colibri-common-g2-input> 
        
        ${this.signer.TipoPessoa==0?p`
           <colibri-common-g2-input
            name="DtNascimento"
            type="date"
            .value=${this.signer.DtNascimento}
            .isLabel=${"Dt. Nascimento"}
            .isDisabled=${!this.canEditBirthDate}
            .error=${this.validErrorsForm("DtNascimento")}
            @on-input=${s=>this.handleChange(s)}
          ></colibri-common-g2-input> 
            <colibri-common-g2-input
            name="Celular"
            .isLabel=${"Celular"}
            .value=${Ue(this.signer.Celular)}
            maxlength=15
            .error=${this.validErrorsForm("Celular")}
            .isPlaceholder=${"Digite o Celular (11988888888) ..."}
            .isMask=${Ue}
            @on-input=${s=>this.handleChange(s)}
          ></colibri-common-g2-input> 
          <colibri-common-g2-input
            .isLabel=${"E-mail"}
            .isDisabled=${!0}
            .value=${this.signer.Email}
          ></colibri-common-g2-input> 
          `:null}
        <colibri-common-g2-input
          .isLabel=${this.signer.TipoPessoa==0?"RG":"Inscrição Estadual"}
          .isDisabled=${!0}
          .value=${this.signer.IERG}
        ></colibri-common-g2-input> 
       <colibri-common-g2-input
          name="CNH"
          .isLabel=${"CNH"}
          .hidden=${this.signer.TipoPessoa==1}
          .isPlaceholder=${"Digite o nº da CNH..."}
          maxlength=11
          .isDisabled=${this.signer.TipoPessoa==1}
          .value=${this.signer.CNH}
          @on-input=${s=>this.handleChange(s)}
        ></colibri-common-g2-input> 
        ${this.isLoadCep?p`
            <ui-load-input isLabel="Logragouro" class="span"></ui-load-input>`:p`<colibri-common-g2-input
            name="CEP"
            .isLabel=${"CEP"}
            .isPlaceholder=${"Digite seu CEP..."}
            .isDisabled=${this.signer.TipoPessoa==1}
            .value=${pi(this.signer.CEP)}
            .isMaks=${pi}
            .error=${this.validErrorsForm("CEP")}
            @on-input=${s=>this.handleCepChange(s)}
          ></colibri-common-g2-input>`}
        ${this.isLoadCep?p`
            <ui-load-input isLabel="Logragouro" class="span"></ui-load-input>`:p`
            <colibri-common-g2-input
              name="Logradouro"
              .isLabel=${"Logragouro"}
              .isDisabled=${this.signer.TipoPessoa==1||((t=this.cepResponse)==null?void 0:t.streetName)||this.hasInvalidCep}
              .value=${this.signer.Logradouro}
              .error=${this.validErrorsForm("Logradouro")}
              @on-change=${s=>this.handleChange(s)}
            ></colibri-common-g2-input>
        `}
        <colibri-common-g2-input
          name="Numero"
          .isLabel=${"Número"}
          .isPlaceholder=${"Digite seu Número..."}
          .value=${this.signer.Numero}
          .isDisabled=${this.signer.TipoPessoa==1||this.hasInvalidCep}
          .error=${this.validErrorsForm("Numero")}
          @on-input=${s=>this.handleChange(s)}
        ></colibri-common-g2-input> 
        <colibri-common-g2-input
          name="Complemento"
          .isLabel=${"Complemento"}
          .isPlaceholder=${"Digite seu Complemento..."}
          .isDisabled=${this.signer.TipoPessoa==1||this.hasInvalidCep}
          .value=${this.signer.Complemento}
          @on-input=${s=>this.handleChange(s)}
        ></colibri-common-g2-input>  
        ${this.isLoadCep?p`
            <ui-load-input isLabel="Bairro" class="span"></ui-load-input>`:p`
            <colibri-common-g2-input
              name="Bairro"
              .isLabel=${"Bairro"}
              .isDisabled=${this.signer.TipoPessoa==1||((e=this.cepResponse)==null?void 0:e.neighborhood)||this.hasInvalidCep}
              .value=${this.signer.Bairro}
              @on-input=${s=>this.handleChange(s)}
            ></colibri-common-g2-input> 
        `}
        ${this.isLoadCep?p`
            <ui-load-input isLabel="Estado" class="span"></ui-load-input>`:p`
           <colibri-common-g2-select
              name="UF"
              isLabel="Estado"
              .value=${this.signer.UF}
              .isChildren=${this.ufOptions}
              .error=${this.validErrorsForm("UF")}
              .isDisabled=${this.signer.TipoPessoa==1||((i=this.cepResponse)==null?void 0:i.state)||this.hasInvalidCep}
              @on-input=${s=>this.handleChange(s)}
            ></colibri-common-g2-select>   
        `}
        ${this.isLoadCep||this.isLoadCities?p`
            <ui-load-input isLabel="Cidade" class="span"></ui-load-input>`:p`
            <colibri-common-g2-select
            name="IDMunicipio"
            isLabel="Cidade"
            .value=${(o=this.signer.IDMunicipio)==null?void 0:o.toString()}
            .isChildren=${this.citiesOptions}
            .error=${this.validErrorsForm("IDMunicipio")}
            .isDisabled=${this.signer.TipoPessoa==1||((n=this.cepResponse)==null?void 0:n.cityId)||this.hasInvalidCep}
            @on-input=${s=>this.handleChange(s)}
          ></colibri-common-g2-select>  
        `}
        ${this.signer.CPFCNPJ.length==11?p`
             <colibri-common-g2-select
              name="Notificacao"
              isLabel="Assinar via"
              .isChildren=${this.signingByOptions}
              .error=${this.validErrorsForm("Notificacao")}
              @on-input=${s=>this.handleChange(s)}
            ></colibri-common-g2-select>  
          `:null}
       
      </div>
      <div class="accept-term-container">
      ${this.signer.TipoPessoa==1?p`
            <colibri-common-g2-text
              size="size-3"
              color="warning-400"
            >Para atualização do cadastro, entre em contato com a Copart do Brasil
            </colibri-common-g2-text>
          `:null}
        <colibri-common-g2-checkbox
          name="Aceite"
          type="checkbox" 
          label="Eu declaro que todas as informações acima são verdadeiras e estou de acordo com o serviço."
          .isChecked=${this.acceptTerms}
          @on-input=${s=>this.handleChange(s)}
        ></colibri-common-g2-checkbox>
      </div>
    `}renderLegalRepresentativeStep(){return p`
    <div class="form-title">
        <colibri-common-g2-heading weight="weight-bold">
          Dados do Representante Legal
        </colibri-common-g2-heading>
    </div>
    <div class="legal-representative-container">
      <colibri-common-g2-input
        name="RazaoRepresentanteLegal"
        .isLabel=${"Nome"}
        .value=${this.signer.RazaoRepresentanteLegal}
        .error=${this.validErrorsForm("RazaoRepresentanteLegal")}
        .isPlaceholder=${"Digite o Nome..."}
        .isMask=${hi}
        @on-input=${t=>this.handleChange(t)}
      ></colibri-common-g2-input>
      <colibri-common-g2-input
        name="EmailRepresentanteLegal"
        .isLabel=${"E-mail"}
        .value=${this.signer.EmailRepresentanteLegal}
        .error=${this.validErrorsForm("EmailRepresentanteLegal")}
        .isPlaceholder=${"Digite o E-mail..."}
        @on-input=${t=>this.handleChange(t)}
      ></colibri-common-g2-input> 
      <colibri-common-g2-input
        name="CPFRepresentanteLegal"
        .isLabel=${"CPF"}
        .isMask=${Me}
        maxlength=13
        .value=${Me(this.signer.CPFRepresentanteLegal)}
        .error=${this.validErrorsForm("CPFRepresentanteLegal")}
        .isPlaceholder=${"Digite o nº do CPF..."}
        @on-input=${t=>this.handleChange(t)}
      ></colibri-common-g2-input>  
      <colibri-common-g2-input
        name="CNHRepresentanteLegal"
        .isLabel=${"CNH"}
        maxlength=11
        .isPlaceholder=${"Digite o nº da CNH..."}
        @on-input=${t=>this.handleChange(t)}
      ></colibri-common-g2-input> 
      <colibri-common-g2-input
        name="RGRepresentanteLegal"
        .isLabel=${"RG"}
        type="number"
        .value=${this.signer.RGRepresentanteLegal}
        .error=${this.validErrorsForm("RGRepresentanteLegal")}
        .isPlaceholder=${"Digite o nº do RG..."}
        @on-input=${t=>this.handleChange(t)}
      ></colibri-common-g2-input>
      <colibri-common-g2-input
        name="TelefoneRepresentanteLegal"
        .isLabel=${"Celular"}
        maxlength=15
        .isMask=${Ue}
        .value=${Ue(this.signer.TelefoneRepresentanteLegal)}
        .error=${this.validErrorsForm("TelefoneRepresentanteLegal")}
        .isPlaceholder=${"Digite o Celular (11988888888) ..."}
        @on-input=${t=>this.handleChange(t)}
      ></colibri-common-g2-input>   
      ${this.signer.CPFCNPJ.length>11?p`
             <colibri-common-g2-select
              name="Notificacao"
              isLabel="Assinar via"
              .isChildren=${this.signingByOptions}
              .error=${this.validErrorsForm("Notificacao")}
              @on-input=${t=>this.handleChange(t)}
            ></colibri-common-g2-select>  
          `:null}
    </div>
  `}renderPurchaseStep(){var e;const t=this.servicesUrl.endsWith("/")?this.servicesUrl.substring(0,this.servicesUrl.length-1):this.servicesUrl;return p`
    <div class="purchase-content">
      ${this.isPaid?p`
        <div class="thank-you-title">
          <colibri-common-g2-heading weight="weight-bold">
            <h3 style="text-align: center;">Recebemos seu pagamento<br> ${this.signer.Nome}!</h3>
            </colibri-common-g2-heading>
        </div>
        <div class="thank-you-text">
          <label>Agora é só aguardar. Em breve você receberá uma mensagem no seu WhatsApp, do <b>Click Sign</b>, para continuar com o processo de autenticação do termo de responsabilidade.</label>
        </div>
        `:null}
          <qrcode-visualizer
            id="pix"
            class="pix-modal"
            .dataQrCode=${this.purshadeData}
            .token=${this.token}
            .servicesUrl=${t}
            .requestId=${(e=this.purshadeData)==null?void 0:e.requestId}
            .cancelRequest=${!0}
            @paid=${this.nextStepClick}
          ></qrcode-visualizer>
    </div>
     
    `}getNotifyByOptionSelected(){var t;return(t=this.signingByOptions.find(e=>e.value==this.notifyBy))==null?void 0:t.name}renderThankYouStep(){return p`
      <div class="thank-you-title">
          ${gn(60,60)}
          <colibri-common-g2-heading weight="weight-bold">
            <div style="text-align: center">
              <h2>Pagamento confirmado, <br/><br/>${this.signer.Nome}</h2>
            </div>
          </colibri-common-g2-heading>
      </div>
      <div class="thank-you-container">
        <div class="thank-you-text">
          <label>Agora é só aguardar. Em breve você receberá, no seu ${this.getNotifyByOptionSelected()}, o link para seguir com a autenticação do termo de responsabilidade.</label>
        </div>
      </div>
    `}};L([g()],P.prototype,"servicesUrl",2),L([g()],P.prototype,"token",2),L([g()],P.prototype,"currentStep",2),L([g()],P.prototype,"hasFormErrors",2),L([g()],P.prototype,"acceptTerms",2),L([g()],P.prototype,"notifyBy",2),L([g()],P.prototype,"isLoad",2),L([g()],P.prototype,"isLoadCep",2),L([g()],P.prototype,"isLoadCities",2),L([g()],P.prototype,"purshadeData",2),L([g()],P.prototype,"signer",2),L([g()],P.prototype,"cepResponse",2),L([g()],P.prototype,"hasInvalidCep",2),L([g()],P.prototype,"serviceAmount",2),L([g()],P.prototype,"signingByOptions",2),L([g()],P.prototype,"ufOptions",2),L([g()],P.prototype,"citiesOptions",2),L([g()],P.prototype,"isPaid",2),P=L([De("online-term-purchase")],P);const Tn=ne`
  .container-documentation {
    display: flex;
    flex-direction: column;
  }

  .container-documentation .section-step {
    margin-bottom: 12px;
  }

  .documentation-header {
    display: flex;
    align-items: center;
    justify-content: space-between;

    margin-bottom: 12px;

    @media (max-width: 620px) {
      flex-direction: column;
      align-items: start;
      gap: 4px;
    }
  }

  .documentation-header .documentation-title {
    font-size: clamp(22px, 2.5vw, 3rem);
    font-weight: bolder;
    color: #1254ff;
  }

  .documentation-header .header-actions {
    display: flex;
    align-items: center;
    gap: 12px;

    @media (max-width: 620px) {
      justify-content: end;
      width: 100%;
    }
  }

  .button-print {
    display: flex;
    align-items: center;
    gap: 6px;

    font-size: var(--text-small-sm);
    font-weight: var(--weight-semibold);
    color: var(--gray-700);
    background-color: transparent;
    border: none;

    &:hover {
      color: var(--blue-600);
      text-decoration: underline;
    }

    &:disabled {
      cursor: not-allowed;
    }
  }
`,An={info:mn,success:hn,error:pn,warning:ui,ghost:ui};function On({title:t,type:e,action:i,description:o,closeToast:n}){const s={info:"blue",success:"green",error:"red",warning:"warning"};return p`
    <article
      style=${`background-color: var(--${s[e]}-50)`}
      popover="manual"
      id="toast-container"
      class=${`toast newest ${e}`}
    >
      ${An[e]||"info"}

      <div class="toast-message">
        <colibri-common-ui-text
          style="line-height: 16px"
          color=${`${s[e]}-600`}
          size="size-2"
          weight="weight-medium"
          >${t}</colibri-common-ui-text
        >

        ${o?p`
              <colibri-common-ui-text
                style="line-height: 14px"
                color=${`${s[e]}-400`}
                size="size-2"
                weight="weight-medium"
                >${o}</colibri-common-ui-text
              >
            `:null}
      </div>

      <button @click=${()=>n()} class="toast-close-button">
        ${fn}
      </button>

      ${i?p`
            <div style="display: flex; align-items: end; justify-content: end">
              <colibri-common-ui-g2online-services-button
                size="xs"
                variant="gray"
                @click=${()=>i.action()}
                >${i.text??"Ação"}</colibri-common-ui-g2online-services-button
              >
            </div>
          `:null}
    </article>
  `}ne`
  .failure {
    background: rgb(255, 100, 100);
  }

  .success {
    background: rgb(50, 255, 50);
  }
  &:popover-open {
    position: absolute;
    inset: unset;
    right: 5px;
    bottom: 5px;
  }

  #toast-container {
    position: relative;
    width: 390px;
    height: 80px;
    padding: 14px;
    border-radius: 10px;
    box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.2);
    display: flex;
    gap: 6px;
    border: none;

    /* box-shadow: 0 4px 12px #0000001a; */
  }

  .toast .toast-close-button {
    display: grid;
    place-items: center;

    padding: 4px;
    border: none;
    background-color: transparent;

    position: absolute;
    top: 2px;
    right: 6px;
    width: 24px;
    height: 24px;

    cursor: pointer;
  }

  .toast .toast-close-button:hover > svg path {
    stroke: var(--gray-700);
    transform: all 0.3s ease;
  }

  .toast .toast-close-button > svg path {
    stroke: var(--gray-500);
  }

  .toast-message {
    display: flex;
    flex-direction: column;
    gap: 2px;

    margin-left: 12px;
  }

  [popover]:popover-open {
    opacity: 1;
    position: absolute;
    inset: unset;
    right: 10px;
    top: 10px;
    transform: translateX(0px);
  }

  [popover] {
    font-size: 1.2rem;
    padding: 10px;
    opacity: 0;
    transform: translateX(-60px);

    transition:
      opacity 0.7s,
      transform 0.7s,
      overlay 0.7s allow-discrete,
      display 0.7s allow-discrete;
  }
  
  @starting-style {
    [popover]:popover-open {
      opacity: 0;
      transform: translateX(-60px);
    }
  }
`;function xe({title:t="",description:e="",type:i="info",action:o}){const n=On({title:t,type:i,action:o,description:e,closeToast:a}),s=document.createElement("div");Et(n,s);const r=s.firstElementChild;document.body.appendChild(r),r.showPopover(),setTimeout(()=>{r.hidePopover(),r.remove()},5e5),r.addEventListener("toggle",c=>{c.newState==="open"&&Nn()});function a(){r.hidePopover(),r.remove()}}function Nn(){document.querySelectorAll(".toast").forEach(e=>{if(e.classList.contains("newest"))e.style.top="16px",e.classList.remove("newest");else{const i=e.style.top.replace("px",""),o=parseInt(i)+88;e.style.top=`${o}px`}})}var _n=Object.defineProperty,kn=Object.getOwnPropertyDescriptor,q=(t,e,i,o)=>{for(var n=o>1?void 0:o?kn(e,i):e,s=t.length-1,r;s>=0;s--)(r=t[s])&&(n=(o?r(e,i,n):r(n))||n);return o&&n&&_n(e,i,n),n};let V=class extends j{constructor(){super(...arguments),this.memberId="",this.servicesUrl="",this.token="",this.activeStep="Nota/Recibo de Venda",this.dataprint=[],this.bannerLink="",this.bannerImg=""}static get styles(){return[Tn,Ie]}async connectedCallback(){super.connectedCallback(),await super.updateComplete,this.getBannerLinks()}handleStepChange(t){this.activeStep=t}async getBannerLinks(){try{const{data:t}=await S(this.servicesUrl,"GET","getBannerLinks",this.token);t.ResultCode===0&&(this.bannerLink=t.link,this.bannerImg=t.img)}catch{xe({title:"Atencao",type:"warning",description:"Não foi possivel gerar excel da página."})}}async exportLotsWithPendingIssuanceOfSalesNoteToExcel(){try{const t={itens:this.dataprint},{data:e}=await S(this.servicesUrl,"POST","exportLotsWithPendingIssuanceOfSalesNoteToExcel",this.token,t);if(e.resultCode===0){const i={name:`activeStep_${this.activeStep}.xlsx`,content:e.content};ie(i)}}catch{xe({title:"Atencao",type:"warning",description:"Não foi possivel gerar excel da página."})}}async exportLotsWithPendingIssuanceOfGatePassToExcel(){try{const t={itens:this.dataprint},{data:e}=await S(this.servicesUrl,"POST","exportLotsWithPendingIssuanceOfGatePassToExcel",this.token,t);if(e.resultCode===0){const i={name:`activeStep_${this.activeStep}.xlsx`,content:e.content};ie(i)}}catch{xe({title:"Atencao",type:"warning",description:"Não foi possivel gerar excel da página."})}}async printLotsWithPendingIssuanceOfSalesNoteToPdf(){try{const t={itens:this.dataprint},{data:e}=await S(this.servicesUrl,"POST","printLotsWithPendingIssuanceOfSalesNoteToPdf",this.token,t);if(e.resultCode===0){const i={name:`activeStep_${this.activeStep}.pdf`,content:e.content};ie(i)}}catch{xe({title:"Atencao",type:"warning",description:"Não foi possivel gerar excel da página."})}}async printLotsWithPendingIssuanceOfGatePassToPdf(){try{const t={itens:this.dataprint},{data:e}=await S(this.servicesUrl,"POST","printLotsWithPendingIssuanceOfGatePassToPdf",this.token,t);if(e.resultCode===0){const i={name:`activeStep_${this.activeStep}.pdf`,content:e.content};ie(i)}}catch{xe({title:"Atencao",type:"warning",description:"Não foi possivel gerar excel da página."})}}render(){const t=[{item:p`<page-documents
          memberId=${this.memberId}
          servicesUrl=${this.servicesUrl}
          token=${this.token}
          @dataPrint=${e=>this.dataprint=e.detail}
        ></page-documents>`,name:"Nota/Recibo de Venda"},{item:p`<page-gate-pass
          memberId=${this.memberId}
          servicesUrl=${this.servicesUrl}
          token=${this.token}
          @dataPrint=${e=>this.dataprint=e.detail}
        ></page-gate-pass>`,name:"Gatepass"}];return p`
      <div class="container-documentation">
        <g2-toast-container></g2-toast-container>
        <g2-alert-container></g2-alert-container>

        <div class="documentation-header">
          <h1 class="documentation-title">Emissão Nota/Recibo de Venda</h1>

          <div class="header-actions">
            <button
              class="button-print"
              .disabled=${!this.dataprint.length}
              @click=${()=>{this.activeStep==="getepass"?this.printLotsWithPendingIssuanceOfGatePassToPdf():this.printLotsWithPendingIssuanceOfSalesNoteToPdf()}}
            >
              <ph-file-pdf
                color="var(--gray-600)"
                size="16px"
                weight="bold"
              ></ph-file-pdf>
              exportar PDF
            </button>
            <button
              class="button-print"
              .disabled=${!this.dataprint.length}
              @click=${()=>{this.activeStep==="getepass"?this.exportLotsWithPendingIssuanceOfGatePassToExcel():this.exportLotsWithPendingIssuanceOfSalesNoteToExcel()}}
            >
              <ph-file-xls
                color="var(--gray-600)"
                size="16px"
                weight="bold"
              ></ph-file-xls>
              exportar excel
            </button>
          </div>
        </div>
        <div>
          <a .href=${this.bannerLink}>
            <img .src=${this.bannerImg}>
          </a>
        </div>
        <div class="section-step">
          <colibri-common-g2-step
            active=${this.activeStep}
            .data=${t}
            @onClick=${e=>this.handleStepChange(e.detail.name)}
          >
          </colibri-common-g2-step>
        </div>

        <div class="member-content bar">
          ${t.filter(e=>e.name===this.activeStep)[0].item}
        </div>
      </div>
    `}};q([M()],V.prototype,"memberId",2),q([M()],V.prototype,"servicesUrl",2),q([M()],V.prototype,"token",2),q([g()],V.prototype,"activeStep",2),q([g()],V.prototype,"dataprint",2),q([g()],V.prototype,"bannerLink",2),q([g()],V.prototype,"bannerImg",2),V=q([De("page-documentation")],V)});
