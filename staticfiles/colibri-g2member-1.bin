(function(z){typeof define=="function"&&define.amd?define(z):z()})(function(){"use strict";/*! colibri-g2member - v1.0.0 *//**
 * @license
 * Copyright 2019 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */var li;const z=globalThis,Re=z.ShadowRoot&&(z.ShadyCSS===void 0||z.ShadyCSS.nativeShadow)&&"adoptedStyleSheets"in Document.prototype&&"replace"in CSSStyleSheet.prototype,Ne=Symbol(),rt=new WeakMap;let at=class{constructor(e,i,o){if(this._$cssResult$=!0,o!==Ne)throw Error("CSSResult is not constructable. Use `unsafeCSS` or `css` instead.");this.cssText=e,this.t=i}get styleSheet(){let e=this.o;const i=this.t;if(Re&&e===void 0){const o=i!==void 0&&i.length===1;o&&(e=rt.get(i)),e===void 0&&((this.o=e=new CSSStyleSheet).replaceSync(this.cssText),o&&rt.set(i,e))}return e}toString(){return this.cssText}};const di=t=>new at(typeof t=="string"?t:t+"",void 0,Ne),se=(t,...e)=>{const i=t.length===1?t[0]:e.reduce((o,n,s)=>o+(r=>{if(r._$cssResult$===!0)return r.cssText;if(typeof r=="number")return r;throw Error("Value passed to 'css' function must be a 'css' function result: "+r+". Use 'unsafeCSS' to pass non-literal values, but take care to ensure page security.")})(n)+t[s+1],t[0]);return new at(i,t,Ne)},ui=(t,e)=>{if(Re)t.adoptedStyleSheets=e.map(i=>i instanceof CSSStyleSheet?i:i.styleSheet);else for(const i of e){const o=document.createElement("style"),n=z.litNonce;n!==void 0&&o.setAttribute("nonce",n),o.textContent=i.cssText,t.appendChild(o)}},lt=Re?t=>t:t=>t instanceof CSSStyleSheet?(e=>{let i="";for(const o of e.cssRules)i+=o.cssText;return di(i)})(t):t;/**
 * @license
 * Copyright 2017 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */const{is:hi,defineProperty:pi,getOwnPropertyDescriptor:fi,getOwnPropertyNames:mi,getOwnPropertySymbols:gi,getPrototypeOf:bi}=Object,U=globalThis,ct=U.trustedTypes,yi=ct?ct.emptyScript:"",ke=U.reactiveElementPolyfillSupport,re=(t,e)=>t,be={toAttribute(t,e){switch(e){case Boolean:t=t?yi:null;break;case Object:case Array:t=t==null?t:JSON.stringify(t)}return t},fromAttribute(t,e){let i=t;switch(e){case Boolean:i=t!==null;break;case Number:i=t===null?null:Number(t);break;case Object:case Array:try{i=JSON.parse(t)}catch{i=null}}return i}},Ie=(t,e)=>!hi(t,e),dt={attribute:!0,type:String,converter:be,reflect:!1,hasChanged:Ie};Symbol.metadata??(Symbol.metadata=Symbol("metadata")),U.litPropertyMetadata??(U.litPropertyMetadata=new WeakMap);class ee extends HTMLElement{static addInitializer(e){this._$Ei(),(this.l??(this.l=[])).push(e)}static get observedAttributes(){return this.finalize(),this._$Eh&&[...this._$Eh.keys()]}static createProperty(e,i=dt){if(i.state&&(i.attribute=!1),this._$Ei(),this.elementProperties.set(e,i),!i.noAccessor){const o=Symbol(),n=this.getPropertyDescriptor(e,o,i);n!==void 0&&pi(this.prototype,e,n)}}static getPropertyDescriptor(e,i,o){const{get:n,set:s}=fi(this.prototype,e)??{get(){return this[i]},set(r){this[i]=r}};return{get(){return n==null?void 0:n.call(this)},set(r){const a=n==null?void 0:n.call(this);s.call(this,r),this.requestUpdate(e,a,o)},configurable:!0,enumerable:!0}}static getPropertyOptions(e){return this.elementProperties.get(e)??dt}static _$Ei(){if(this.hasOwnProperty(re("elementProperties")))return;const e=bi(this);e.finalize(),e.l!==void 0&&(this.l=[...e.l]),this.elementProperties=new Map(e.elementProperties)}static finalize(){if(this.hasOwnProperty(re("finalized")))return;if(this.finalized=!0,this._$Ei(),this.hasOwnProperty(re("properties"))){const i=this.properties,o=[...mi(i),...gi(i)];for(const n of o)this.createProperty(n,i[n])}const e=this[Symbol.metadata];if(e!==null){const i=litPropertyMetadata.get(e);if(i!==void 0)for(const[o,n]of i)this.elementProperties.set(o,n)}this._$Eh=new Map;for(const[i,o]of this.elementProperties){const n=this._$Eu(i,o);n!==void 0&&this._$Eh.set(n,i)}this.elementStyles=this.finalizeStyles(this.styles)}static finalizeStyles(e){const i=[];if(Array.isArray(e)){const o=new Set(e.flat(1/0).reverse());for(const n of o)i.unshift(lt(n))}else e!==void 0&&i.push(lt(e));return i}static _$Eu(e,i){const o=i.attribute;return o===!1?void 0:typeof o=="string"?o:typeof e=="string"?e.toLowerCase():void 0}constructor(){super(),this._$Ep=void 0,this.isUpdatePending=!1,this.hasUpdated=!1,this._$Em=null,this._$Ev()}_$Ev(){var e;this._$ES=new Promise(i=>this.enableUpdating=i),this._$AL=new Map,this._$E_(),this.requestUpdate(),(e=this.constructor.l)==null||e.forEach(i=>i(this))}addController(e){var i;(this._$EO??(this._$EO=new Set)).add(e),this.renderRoot!==void 0&&this.isConnected&&((i=e.hostConnected)==null||i.call(e))}removeController(e){var i;(i=this._$EO)==null||i.delete(e)}_$E_(){const e=new Map,i=this.constructor.elementProperties;for(const o of i.keys())this.hasOwnProperty(o)&&(e.set(o,this[o]),delete this[o]);e.size>0&&(this._$Ep=e)}createRenderRoot(){const e=this.shadowRoot??this.attachShadow(this.constructor.shadowRootOptions);return ui(e,this.constructor.elementStyles),e}connectedCallback(){var e;this.renderRoot??(this.renderRoot=this.createRenderRoot()),this.enableUpdating(!0),(e=this._$EO)==null||e.forEach(i=>{var o;return(o=i.hostConnected)==null?void 0:o.call(i)})}enableUpdating(e){}disconnectedCallback(){var e;(e=this._$EO)==null||e.forEach(i=>{var o;return(o=i.hostDisconnected)==null?void 0:o.call(i)})}attributeChangedCallback(e,i,o){this._$AK(e,o)}_$EC(e,i){var s;const o=this.constructor.elementProperties.get(e),n=this.constructor._$Eu(e,o);if(n!==void 0&&o.reflect===!0){const r=(((s=o.converter)==null?void 0:s.toAttribute)!==void 0?o.converter:be).toAttribute(i,o.type);this._$Em=e,r==null?this.removeAttribute(n):this.setAttribute(n,r),this._$Em=null}}_$AK(e,i){var s;const o=this.constructor,n=o._$Eh.get(e);if(n!==void 0&&this._$Em!==n){const r=o.getPropertyOptions(n),a=typeof r.converter=="function"?{fromAttribute:r.converter}:((s=r.converter)==null?void 0:s.fromAttribute)!==void 0?r.converter:be;this._$Em=n,this[n]=a.fromAttribute(i,r.type),this._$Em=null}}requestUpdate(e,i,o){if(e!==void 0){if(o??(o=this.constructor.getPropertyOptions(e)),!(o.hasChanged??Ie)(this[e],i))return;this.P(e,i,o)}this.isUpdatePending===!1&&(this._$ES=this._$ET())}P(e,i,o){this._$AL.has(e)||this._$AL.set(e,i),o.reflect===!0&&this._$Em!==e&&(this._$Ej??(this._$Ej=new Set)).add(e)}async _$ET(){this.isUpdatePending=!0;try{await this._$ES}catch(i){Promise.reject(i)}const e=this.scheduleUpdate();return e!=null&&await e,!this.isUpdatePending}scheduleUpdate(){return this.performUpdate()}performUpdate(){var o;if(!this.isUpdatePending)return;if(!this.hasUpdated){if(this.renderRoot??(this.renderRoot=this.createRenderRoot()),this._$Ep){for(const[s,r]of this._$Ep)this[s]=r;this._$Ep=void 0}const n=this.constructor.elementProperties;if(n.size>0)for(const[s,r]of n)r.wrapped!==!0||this._$AL.has(s)||this[s]===void 0||this.P(s,this[s],r)}let e=!1;const i=this._$AL;try{e=this.shouldUpdate(i),e?(this.willUpdate(i),(o=this._$EO)==null||o.forEach(n=>{var s;return(s=n.hostUpdate)==null?void 0:s.call(n)}),this.update(i)):this._$EU()}catch(n){throw e=!1,this._$EU(),n}e&&this._$AE(i)}willUpdate(e){}_$AE(e){var i;(i=this._$EO)==null||i.forEach(o=>{var n;return(n=o.hostUpdated)==null?void 0:n.call(o)}),this.hasUpdated||(this.hasUpdated=!0,this.firstUpdated(e)),this.updated(e)}_$EU(){this._$AL=new Map,this.isUpdatePending=!1}get updateComplete(){return this.getUpdateComplete()}getUpdateComplete(){return this._$ES}shouldUpdate(e){return!0}update(e){this._$Ej&&(this._$Ej=this._$Ej.forEach(i=>this._$EC(i,this[i]))),this._$EU()}updated(e){}firstUpdated(e){}}ee.elementStyles=[],ee.shadowRootOptions={mode:"open"},ee[re("elementProperties")]=new Map,ee[re("finalized")]=new Map,ke==null||ke({ReactiveElement:ee}),(U.reactiveElementVersions??(U.reactiveElementVersions=[])).push("2.0.4");/**
 * @license
 * Copyright 2017 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */const ae=globalThis,ye=ae.trustedTypes,ut=ye?ye.createPolicy("lit-html",{createHTML:t=>t}):void 0,ht="$lit$",F=`lit$${Math.random().toFixed(9).slice(2)}$`,pt="?"+F,vi=`<${pt}>`,j=document,le=()=>j.createComment(""),ce=t=>t===null||typeof t!="object"&&typeof t!="function",Ve=Array.isArray,xi=t=>Ve(t)||typeof(t==null?void 0:t[Symbol.iterator])=="function",Ue=`[ 	
\f\r]`,de=/<(?:(!--|\/[^a-zA-Z])|(\/?[a-zA-Z][^>\s]*)|(\/?$))/g,ft=/-->/g,mt=/>/g,H=RegExp(`>|${Ue}(?:([^\\s"'>=/]+)(${Ue}*=${Ue}*(?:[^ 	
\f\r"'\`<>=]|("|')|))|$)`,"g"),gt=/'/g,bt=/"/g,yt=/^(?:script|style|textarea|title)$/i,wi=t=>(e,...i)=>({_$litType$:t,strings:e,values:i}),m=wi(1),G=Symbol.for("lit-noChange"),E=Symbol.for("lit-nothing"),vt=new WeakMap,q=j.createTreeWalker(j,129);function xt(t,e){if(!Ve(t)||!t.hasOwnProperty("raw"))throw Error("invalid template strings array");return ut!==void 0?ut.createHTML(e):e}const $i=(t,e)=>{const i=t.length-1,o=[];let n,s=e===2?"<svg>":e===3?"<math>":"",r=de;for(let a=0;a<i;a++){const c=t[a];let d,u,h=-1,y=0;for(;y<c.length&&(r.lastIndex=y,u=r.exec(c),u!==null);)y=r.lastIndex,r===de?u[1]==="!--"?r=ft:u[1]!==void 0?r=mt:u[2]!==void 0?(yt.test(u[2])&&(n=RegExp("</"+u[2],"g")),r=H):u[3]!==void 0&&(r=H):r===H?u[0]===">"?(r=n??de,h=-1):u[1]===void 0?h=-2:(h=r.lastIndex-u[2].length,d=u[1],r=u[3]===void 0?H:u[3]==='"'?bt:gt):r===bt||r===gt?r=H:r===ft||r===mt?r=de:(r=H,n=void 0);const v=r===H&&t[a+1].startsWith("/>")?" ":"";s+=r===de?c+vi:h>=0?(o.push(d),c.slice(0,h)+ht+c.slice(h)+F+v):c+F+(h===-2?a:v)}return[xt(t,s+(t[i]||"<?>")+(e===2?"</svg>":e===3?"</math>":"")),o]};class ue{constructor({strings:e,_$litType$:i},o){let n;this.parts=[];let s=0,r=0;const a=e.length-1,c=this.parts,[d,u]=$i(e,i);if(this.el=ue.createElement(d,o),q.currentNode=this.el.content,i===2||i===3){const h=this.el.content.firstChild;h.replaceWith(...h.childNodes)}for(;(n=q.nextNode())!==null&&c.length<a;){if(n.nodeType===1){if(n.hasAttributes())for(const h of n.getAttributeNames())if(h.endsWith(ht)){const y=u[r++],v=n.getAttribute(h).split(F),p=/([.?@])?(.*)/.exec(y);c.push({type:1,index:s,name:p[2],strings:v,ctor:p[1]==="."?Ei:p[1]==="?"?Di:p[1]==="@"?Pi:ve}),n.removeAttribute(h)}else h.startsWith(F)&&(c.push({type:6,index:s}),n.removeAttribute(h));if(yt.test(n.tagName)){const h=n.textContent.split(F),y=h.length-1;if(y>0){n.textContent=ye?ye.emptyScript:"";for(let v=0;v<y;v++)n.append(h[v],le()),q.nextNode(),c.push({type:2,index:++s});n.append(h[y],le())}}}else if(n.nodeType===8)if(n.data===pt)c.push({type:2,index:s});else{let h=-1;for(;(h=n.data.indexOf(F,h+1))!==-1;)c.push({type:7,index:s}),h+=F.length-1}s++}}static createElement(e,i){const o=j.createElement("template");return o.innerHTML=e,o}}function te(t,e,i=t,o){var r,a;if(e===G)return e;let n=o!==void 0?(r=i._$Co)==null?void 0:r[o]:i._$Cl;const s=ce(e)?void 0:e._$litDirective$;return(n==null?void 0:n.constructor)!==s&&((a=n==null?void 0:n._$AO)==null||a.call(n,!1),s===void 0?n=void 0:(n=new s(t),n._$AT(t,i,o)),o!==void 0?(i._$Co??(i._$Co=[]))[o]=n:i._$Cl=n),n!==void 0&&(e=te(t,n._$AS(t,e.values),n,o)),e}class Si{constructor(e,i){this._$AV=[],this._$AN=void 0,this._$AD=e,this._$AM=i}get parentNode(){return this._$AM.parentNode}get _$AU(){return this._$AM._$AU}u(e){const{el:{content:i},parts:o}=this._$AD,n=((e==null?void 0:e.creationScope)??j).importNode(i,!0);q.currentNode=n;let s=q.nextNode(),r=0,a=0,c=o[0];for(;c!==void 0;){if(r===c.index){let d;c.type===2?d=new he(s,s.nextSibling,this,e):c.type===1?d=new c.ctor(s,c.name,c.strings,this,e):c.type===6&&(d=new Ai(s,this,e)),this._$AV.push(d),c=o[++a]}r!==(c==null?void 0:c.index)&&(s=q.nextNode(),r++)}return q.currentNode=j,n}p(e){let i=0;for(const o of this._$AV)o!==void 0&&(o.strings!==void 0?(o._$AI(e,o,i),i+=o.strings.length-2):o._$AI(e[i])),i++}}class he{get _$AU(){var e;return((e=this._$AM)==null?void 0:e._$AU)??this._$Cv}constructor(e,i,o,n){this.type=2,this._$AH=E,this._$AN=void 0,this._$AA=e,this._$AB=i,this._$AM=o,this.options=n,this._$Cv=(n==null?void 0:n.isConnected)??!0}get parentNode(){let e=this._$AA.parentNode;const i=this._$AM;return i!==void 0&&(e==null?void 0:e.nodeType)===11&&(e=i.parentNode),e}get startNode(){return this._$AA}get endNode(){return this._$AB}_$AI(e,i=this){e=te(this,e,i),ce(e)?e===E||e==null||e===""?(this._$AH!==E&&this._$AR(),this._$AH=E):e!==this._$AH&&e!==G&&this._(e):e._$litType$!==void 0?this.$(e):e.nodeType!==void 0?this.T(e):xi(e)?this.k(e):this._(e)}O(e){return this._$AA.parentNode.insertBefore(e,this._$AB)}T(e){this._$AH!==e&&(this._$AR(),this._$AH=this.O(e))}_(e){this._$AH!==E&&ce(this._$AH)?this._$AA.nextSibling.data=e:this.T(j.createTextNode(e)),this._$AH=e}$(e){var s;const{values:i,_$litType$:o}=e,n=typeof o=="number"?this._$AC(e):(o.el===void 0&&(o.el=ue.createElement(xt(o.h,o.h[0]),this.options)),o);if(((s=this._$AH)==null?void 0:s._$AD)===n)this._$AH.p(i);else{const r=new Si(n,this),a=r.u(this.options);r.p(i),this.T(a),this._$AH=r}}_$AC(e){let i=vt.get(e.strings);return i===void 0&&vt.set(e.strings,i=new ue(e)),i}k(e){Ve(this._$AH)||(this._$AH=[],this._$AR());const i=this._$AH;let o,n=0;for(const s of e)n===i.length?i.push(o=new he(this.O(le()),this.O(le()),this,this.options)):o=i[n],o._$AI(s),n++;n<i.length&&(this._$AR(o&&o._$AB.nextSibling,n),i.length=n)}_$AR(e=this._$AA.nextSibling,i){var o;for((o=this._$AP)==null?void 0:o.call(this,!1,!0,i);e&&e!==this._$AB;){const n=e.nextSibling;e.remove(),e=n}}setConnected(e){var i;this._$AM===void 0&&(this._$Cv=e,(i=this._$AP)==null||i.call(this,e))}}class ve{get tagName(){return this.element.tagName}get _$AU(){return this._$AM._$AU}constructor(e,i,o,n,s){this.type=1,this._$AH=E,this._$AN=void 0,this.element=e,this.name=i,this._$AM=n,this.options=s,o.length>2||o[0]!==""||o[1]!==""?(this._$AH=Array(o.length-1).fill(new String),this.strings=o):this._$AH=E}_$AI(e,i=this,o,n){const s=this.strings;let r=!1;if(s===void 0)e=te(this,e,i,0),r=!ce(e)||e!==this._$AH&&e!==G,r&&(this._$AH=e);else{const a=e;let c,d;for(e=s[0],c=0;c<s.length-1;c++)d=te(this,a[o+c],i,c),d===G&&(d=this._$AH[c]),r||(r=!ce(d)||d!==this._$AH[c]),d===E?e=E:e!==E&&(e+=(d??"")+s[c+1]),this._$AH[c]=d}r&&!n&&this.j(e)}j(e){e===E?this.element.removeAttribute(this.name):this.element.setAttribute(this.name,e??"")}}class Ei extends ve{constructor(){super(...arguments),this.type=3}j(e){this.element[this.name]=e===E?void 0:e}}class Di extends ve{constructor(){super(...arguments),this.type=4}j(e){this.element.toggleAttribute(this.name,!!e&&e!==E)}}class Pi extends ve{constructor(e,i,o,n,s){super(e,i,o,n,s),this.type=5}_$AI(e,i=this){if((e=te(this,e,i,0)??E)===G)return;const o=this._$AH,n=e===E&&o!==E||e.capture!==o.capture||e.once!==o.once||e.passive!==o.passive,s=e!==E&&(o===E||n);n&&this.element.removeEventListener(this.name,this,o),s&&this.element.addEventListener(this.name,this,e),this._$AH=e}handleEvent(e){var i;typeof this._$AH=="function"?this._$AH.call(((i=this.options)==null?void 0:i.host)??this.element,e):this._$AH.handleEvent(e)}}class Ai{constructor(e,i,o){this.element=e,this.type=6,this._$AN=void 0,this._$AM=i,this.options=o}get _$AU(){return this._$AM._$AU}_$AI(e){te(this,e)}}const Fe=ae.litHtmlPolyfillSupport;Fe==null||Fe(ue,he),(ae.litHtmlVersions??(ae.litHtmlVersions=[])).push("3.2.1");const wt=(t,e,i)=>{const o=(i==null?void 0:i.renderBefore)??e;let n=o._$litPart$;if(n===void 0){const s=(i==null?void 0:i.renderBefore)??null;o._$litPart$=n=new he(e.insertBefore(le(),s),s,void 0,i??{})}return n._$AI(t),n};/**
 * @license
 * Copyright 2017 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */let W=class extends ee{constructor(){super(...arguments),this.renderOptions={host:this},this._$Do=void 0}createRenderRoot(){var i;const e=super.createRenderRoot();return(i=this.renderOptions).renderBefore??(i.renderBefore=e.firstChild),e}update(e){const i=this.render();this.hasUpdated||(this.renderOptions.isConnected=this.isConnected),super.update(e),this._$Do=wt(i,this.renderRoot,this.renderOptions)}connectedCallback(){var e;super.connectedCallback(),(e=this._$Do)==null||e.setConnected(!0)}disconnectedCallback(){var e;super.disconnectedCallback(),(e=this._$Do)==null||e.setConnected(!1)}render(){return G}};W._$litElement$=!0,W.finalized=!0,(li=globalThis.litElementHydrateSupport)==null||li.call(globalThis,{LitElement:W});const Be=globalThis.litElementPolyfillSupport;Be==null||Be({LitElement:W}),(globalThis.litElementVersions??(globalThis.litElementVersions=[])).push("4.1.1");/**
 * @license
 * Copyright 2017 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */const Me=t=>(e,i)=>{i!==void 0?i.addInitializer(()=>{customElements.define(t,e)}):customElements.define(t,e)};/**
 * @license
 * Copyright 2017 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */const Ci={attribute:!0,type:String,converter:be,reflect:!1,hasChanged:Ie},Ti=(t=Ci,e,i)=>{const{kind:o,metadata:n}=i;let s=globalThis.litPropertyMetadata.get(n);if(s===void 0&&globalThis.litPropertyMetadata.set(n,s=new Map),s.set(i.name,t),o==="accessor"){const{name:r}=i;return{set(a){const c=e.get.call(this);e.set.call(this,a),this.requestUpdate(r,c,t)},init(a){return a!==void 0&&this.P(r,void 0,t),a}}}if(o==="setter"){const{name:r}=i;return function(a){const c=this[r];e.call(this,a),this.requestUpdate(r,c,t)}}throw Error("Unsupported decorator location: "+o)};function I(t){return(e,i)=>typeof i=="object"?Ti(t,e,i):((o,n,s)=>{const r=n.hasOwnProperty(s);return n.constructor.createProperty(s,r?{...o,wrapped:!0}:o),r?Object.getOwnPropertyDescriptor(n,s):void 0})(t,e,i)}/**
 * @license
 * Copyright 2017 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */function x(t){return I({...t,state:!0,attribute:!1})}function $t(t,e){return function(){return t.apply(e,arguments)}}const{toString:_i}=Object.prototype,{getPrototypeOf:ze}=Object,xe=(t=>e=>{const i=_i.call(e);return t[i]||(t[i]=i.slice(8,-1).toLowerCase())})(Object.create(null)),k=t=>(t=t.toLowerCase(),e=>xe(e)===t),we=t=>e=>typeof e===t,{isArray:ie}=Array,pe=we("undefined");function Li(t){return t!==null&&!pe(t)&&t.constructor!==null&&!pe(t.constructor)&&L(t.constructor.isBuffer)&&t.constructor.isBuffer(t)}const St=k("ArrayBuffer");function Oi(t){let e;return typeof ArrayBuffer<"u"&&ArrayBuffer.isView?e=ArrayBuffer.isView(t):e=t&&t.buffer&&St(t.buffer),e}const Ri=we("string"),L=we("function"),Et=we("number"),$e=t=>t!==null&&typeof t=="object",Ni=t=>t===!0||t===!1,Se=t=>{if(xe(t)!=="object")return!1;const e=ze(t);return(e===null||e===Object.prototype||Object.getPrototypeOf(e)===null)&&!(Symbol.toStringTag in t)&&!(Symbol.iterator in t)},ki=k("Date"),Ii=k("File"),Vi=k("Blob"),Ui=k("FileList"),Fi=t=>$e(t)&&L(t.pipe),Bi=t=>{let e;return t&&(typeof FormData=="function"&&t instanceof FormData||L(t.append)&&((e=xe(t))==="formdata"||e==="object"&&L(t.toString)&&t.toString()==="[object FormData]"))},Mi=k("URLSearchParams"),[zi,ji,Hi,Gi]=["ReadableStream","Request","Response","Headers"].map(k),qi=t=>t.trim?t.trim():t.replace(/^[\s\uFEFF\xA0]+|[\s\uFEFF\xA0]+$/g,"");function fe(t,e,{allOwnKeys:i=!1}={}){if(t===null||typeof t>"u")return;let o,n;if(typeof t!="object"&&(t=[t]),ie(t))for(o=0,n=t.length;o<n;o++)e.call(null,t[o],o,t);else{const s=i?Object.getOwnPropertyNames(t):Object.keys(t),r=s.length;let a;for(o=0;o<r;o++)a=s[o],e.call(null,t[a],a,t)}}function Dt(t,e){e=e.toLowerCase();const i=Object.keys(t);let o=i.length,n;for(;o-- >0;)if(n=i[o],e===n.toLowerCase())return n;return null}const J=typeof globalThis<"u"?globalThis:typeof self<"u"?self:typeof window<"u"?window:global,Pt=t=>!pe(t)&&t!==J;function je(){const{caseless:t}=Pt(this)&&this||{},e={},i=(o,n)=>{const s=t&&Dt(e,n)||n;Se(e[s])&&Se(o)?e[s]=je(e[s],o):Se(o)?e[s]=je({},o):ie(o)?e[s]=o.slice():e[s]=o};for(let o=0,n=arguments.length;o<n;o++)arguments[o]&&fe(arguments[o],i);return e}const Wi=(t,e,i,{allOwnKeys:o}={})=>(fe(e,(n,s)=>{i&&L(n)?t[s]=$t(n,i):t[s]=n},{allOwnKeys:o}),t),Ji=t=>(t.charCodeAt(0)===65279&&(t=t.slice(1)),t),Qi=(t,e,i,o)=>{t.prototype=Object.create(e.prototype,o),t.prototype.constructor=t,Object.defineProperty(t,"super",{value:e.prototype}),i&&Object.assign(t.prototype,i)},Ki=(t,e,i,o)=>{let n,s,r;const a={};if(e=e||{},t==null)return e;do{for(n=Object.getOwnPropertyNames(t),s=n.length;s-- >0;)r=n[s],(!o||o(r,t,e))&&!a[r]&&(e[r]=t[r],a[r]=!0);t=i!==!1&&ze(t)}while(t&&(!i||i(t,e))&&t!==Object.prototype);return e},Zi=(t,e,i)=>{t=String(t),(i===void 0||i>t.length)&&(i=t.length),i-=e.length;const o=t.indexOf(e,i);return o!==-1&&o===i},Xi=t=>{if(!t)return null;if(ie(t))return t;let e=t.length;if(!Et(e))return null;const i=new Array(e);for(;e-- >0;)i[e]=t[e];return i},Yi=(t=>e=>t&&e instanceof t)(typeof Uint8Array<"u"&&ze(Uint8Array)),eo=(t,e)=>{const o=(t&&t[Symbol.iterator]).call(t);let n;for(;(n=o.next())&&!n.done;){const s=n.value;e.call(t,s[0],s[1])}},to=(t,e)=>{let i;const o=[];for(;(i=t.exec(e))!==null;)o.push(i);return o},io=k("HTMLFormElement"),oo=t=>t.toLowerCase().replace(/[-_\s]([a-z\d])(\w*)/g,function(i,o,n){return o.toUpperCase()+n}),At=(({hasOwnProperty:t})=>(e,i)=>t.call(e,i))(Object.prototype),no=k("RegExp"),Ct=(t,e)=>{const i=Object.getOwnPropertyDescriptors(t),o={};fe(i,(n,s)=>{let r;(r=e(n,s,t))!==!1&&(o[s]=r||n)}),Object.defineProperties(t,o)},so=t=>{Ct(t,(e,i)=>{if(L(t)&&["arguments","caller","callee"].indexOf(i)!==-1)return!1;const o=t[i];if(L(o)){if(e.enumerable=!1,"writable"in e){e.writable=!1;return}e.set||(e.set=()=>{throw Error("Can not rewrite read-only method '"+i+"'")})}})},ro=(t,e)=>{const i={},o=n=>{n.forEach(s=>{i[s]=!0})};return ie(t)?o(t):o(String(t).split(e)),i},ao=()=>{},lo=(t,e)=>t!=null&&Number.isFinite(t=+t)?t:e,He="abcdefghijklmnopqrstuvwxyz",Tt="0123456789",_t={DIGIT:Tt,ALPHA:He,ALPHA_DIGIT:He+He.toUpperCase()+Tt},co=(t=16,e=_t.ALPHA_DIGIT)=>{let i="";const{length:o}=e;for(;t--;)i+=e[Math.random()*o|0];return i};function uo(t){return!!(t&&L(t.append)&&t[Symbol.toStringTag]==="FormData"&&t[Symbol.iterator])}const ho=t=>{const e=new Array(10),i=(o,n)=>{if($e(o)){if(e.indexOf(o)>=0)return;if(!("toJSON"in o)){e[n]=o;const s=ie(o)?[]:{};return fe(o,(r,a)=>{const c=i(r,n+1);!pe(c)&&(s[a]=c)}),e[n]=void 0,s}}return o};return i(t,0)},po=k("AsyncFunction"),fo=t=>t&&($e(t)||L(t))&&L(t.then)&&L(t.catch),Lt=((t,e)=>t?setImmediate:e?((i,o)=>(J.addEventListener("message",({source:n,data:s})=>{n===J&&s===i&&o.length&&o.shift()()},!1),n=>{o.push(n),J.postMessage(i,"*")}))(`axios@${Math.random()}`,[]):i=>setTimeout(i))(typeof setImmediate=="function",L(J.postMessage)),mo=typeof queueMicrotask<"u"?queueMicrotask.bind(J):typeof process<"u"&&process.nextTick||Lt,l={isArray:ie,isArrayBuffer:St,isBuffer:Li,isFormData:Bi,isArrayBufferView:Oi,isString:Ri,isNumber:Et,isBoolean:Ni,isObject:$e,isPlainObject:Se,isReadableStream:zi,isRequest:ji,isResponse:Hi,isHeaders:Gi,isUndefined:pe,isDate:ki,isFile:Ii,isBlob:Vi,isRegExp:no,isFunction:L,isStream:Fi,isURLSearchParams:Mi,isTypedArray:Yi,isFileList:Ui,forEach:fe,merge:je,extend:Wi,trim:qi,stripBOM:Ji,inherits:Qi,toFlatObject:Ki,kindOf:xe,kindOfTest:k,endsWith:Zi,toArray:Xi,forEachEntry:eo,matchAll:to,isHTMLForm:io,hasOwnProperty:At,hasOwnProp:At,reduceDescriptors:Ct,freezeMethods:so,toObjectSet:ro,toCamelCase:oo,noop:ao,toFiniteNumber:lo,findKey:Dt,global:J,isContextDefined:Pt,ALPHABET:_t,generateString:co,isSpecCompliantForm:uo,toJSONObject:ho,isAsyncFn:po,isThenable:fo,setImmediate:Lt,asap:mo};function g(t,e,i,o,n){Error.call(this),Error.captureStackTrace?Error.captureStackTrace(this,this.constructor):this.stack=new Error().stack,this.message=t,this.name="AxiosError",e&&(this.code=e),i&&(this.config=i),o&&(this.request=o),n&&(this.response=n,this.status=n.status?n.status:null)}l.inherits(g,Error,{toJSON:function(){return{message:this.message,name:this.name,description:this.description,number:this.number,fileName:this.fileName,lineNumber:this.lineNumber,columnNumber:this.columnNumber,stack:this.stack,config:l.toJSONObject(this.config),code:this.code,status:this.status}}});const Ot=g.prototype,Rt={};["ERR_BAD_OPTION_VALUE","ERR_BAD_OPTION","ECONNABORTED","ETIMEDOUT","ERR_NETWORK","ERR_FR_TOO_MANY_REDIRECTS","ERR_DEPRECATED","ERR_BAD_RESPONSE","ERR_BAD_REQUEST","ERR_CANCELED","ERR_NOT_SUPPORT","ERR_INVALID_URL"].forEach(t=>{Rt[t]={value:t}}),Object.defineProperties(g,Rt),Object.defineProperty(Ot,"isAxiosError",{value:!0}),g.from=(t,e,i,o,n,s)=>{const r=Object.create(Ot);return l.toFlatObject(t,r,function(c){return c!==Error.prototype},a=>a!=="isAxiosError"),g.call(r,t.message,e,i,o,n),r.cause=t,r.name=t.name,s&&Object.assign(r,s),r};const go=null;function Ge(t){return l.isPlainObject(t)||l.isArray(t)}function Nt(t){return l.endsWith(t,"[]")?t.slice(0,-2):t}function kt(t,e,i){return t?t.concat(e).map(function(n,s){return n=Nt(n),!i&&s?"["+n+"]":n}).join(i?".":""):e}function bo(t){return l.isArray(t)&&!t.some(Ge)}const yo=l.toFlatObject(l,{},null,function(e){return/^is[A-Z]/.test(e)});function Ee(t,e,i){if(!l.isObject(t))throw new TypeError("target must be an object");e=e||new FormData,i=l.toFlatObject(i,{metaTokens:!0,dots:!1,indexes:!1},!1,function(b,f){return!l.isUndefined(f[b])});const o=i.metaTokens,n=i.visitor||u,s=i.dots,r=i.indexes,c=(i.Blob||typeof Blob<"u"&&Blob)&&l.isSpecCompliantForm(e);if(!l.isFunction(n))throw new TypeError("visitor must be a function");function d(p){if(p===null)return"";if(l.isDate(p))return p.toISOString();if(!c&&l.isBlob(p))throw new g("Blob is not supported. Use a Buffer instead.");return l.isArrayBuffer(p)||l.isTypedArray(p)?c&&typeof Blob=="function"?new Blob([p]):Buffer.from(p):p}function u(p,b,f){let S=p;if(p&&!f&&typeof p=="object"){if(l.endsWith(b,"{}"))b=o?b:b.slice(0,-2),p=JSON.stringify(p);else if(l.isArray(p)&&bo(p)||(l.isFileList(p)||l.endsWith(b,"[]"))&&(S=l.toArray(p)))return b=Nt(b),S.forEach(function(A,V){!(l.isUndefined(A)||A===null)&&e.append(r===!0?kt([b],V,s):r===null?b:b+"[]",d(A))}),!1}return Ge(p)?!0:(e.append(kt(f,b,s),d(p)),!1)}const h=[],y=Object.assign(yo,{defaultVisitor:u,convertValue:d,isVisitable:Ge});function v(p,b){if(!l.isUndefined(p)){if(h.indexOf(p)!==-1)throw Error("Circular reference detected in "+b.join("."));h.push(p),l.forEach(p,function(S,P){(!(l.isUndefined(S)||S===null)&&n.call(e,S,l.isString(P)?P.trim():P,b,y))===!0&&v(S,b?b.concat(P):[P])}),h.pop()}}if(!l.isObject(t))throw new TypeError("data must be an object");return v(t),e}function It(t){const e={"!":"%21","'":"%27","(":"%28",")":"%29","~":"%7E","%20":"+","%00":"\0"};return encodeURIComponent(t).replace(/[!'()~]|%20|%00/g,function(o){return e[o]})}function qe(t,e){this._pairs=[],t&&Ee(t,this,e)}const Vt=qe.prototype;Vt.append=function(e,i){this._pairs.push([e,i])},Vt.toString=function(e){const i=e?function(o){return e.call(this,o,It)}:It;return this._pairs.map(function(n){return i(n[0])+"="+i(n[1])},"").join("&")};function vo(t){return encodeURIComponent(t).replace(/%3A/gi,":").replace(/%24/g,"$").replace(/%2C/gi,",").replace(/%20/g,"+").replace(/%5B/gi,"[").replace(/%5D/gi,"]")}function Ut(t,e,i){if(!e)return t;const o=i&&i.encode||vo,n=i&&i.serialize;let s;if(n?s=n(e,i):s=l.isURLSearchParams(e)?e.toString():new qe(e,i).toString(o),s){const r=t.indexOf("#");r!==-1&&(t=t.slice(0,r)),t+=(t.indexOf("?")===-1?"?":"&")+s}return t}class Ft{constructor(){this.handlers=[]}use(e,i,o){return this.handlers.push({fulfilled:e,rejected:i,synchronous:o?o.synchronous:!1,runWhen:o?o.runWhen:null}),this.handlers.length-1}eject(e){this.handlers[e]&&(this.handlers[e]=null)}clear(){this.handlers&&(this.handlers=[])}forEach(e){l.forEach(this.handlers,function(o){o!==null&&e(o)})}}const Bt={silentJSONParsing:!0,forcedJSONParsing:!0,clarifyTimeoutError:!1},xo={isBrowser:!0,classes:{URLSearchParams:typeof URLSearchParams<"u"?URLSearchParams:qe,FormData:typeof FormData<"u"?FormData:null,Blob:typeof Blob<"u"?Blob:null},protocols:["http","https","file","blob","url","data"]},We=typeof window<"u"&&typeof document<"u",Je=typeof navigator=="object"&&navigator||void 0,wo=We&&(!Je||["ReactNative","NativeScript","NS"].indexOf(Je.product)<0),$o=typeof WorkerGlobalScope<"u"&&self instanceof WorkerGlobalScope&&typeof self.importScripts=="function",So=We&&window.location.href||"http://localhost",C={...Object.freeze(Object.defineProperty({__proto__:null,hasBrowserEnv:We,hasStandardBrowserEnv:wo,hasStandardBrowserWebWorkerEnv:$o,navigator:Je,origin:So},Symbol.toStringTag,{value:"Module"})),...xo};function Eo(t,e){return Ee(t,new C.classes.URLSearchParams,Object.assign({visitor:function(i,o,n,s){return C.isNode&&l.isBuffer(i)?(this.append(o,i.toString("base64")),!1):s.defaultVisitor.apply(this,arguments)}},e))}function Do(t){return l.matchAll(/\w+|\[(\w*)]/g,t).map(e=>e[0]==="[]"?"":e[1]||e[0])}function Po(t){const e={},i=Object.keys(t);let o;const n=i.length;let s;for(o=0;o<n;o++)s=i[o],e[s]=t[s];return e}function Mt(t){function e(i,o,n,s){let r=i[s++];if(r==="__proto__")return!0;const a=Number.isFinite(+r),c=s>=i.length;return r=!r&&l.isArray(n)?n.length:r,c?(l.hasOwnProp(n,r)?n[r]=[n[r],o]:n[r]=o,!a):((!n[r]||!l.isObject(n[r]))&&(n[r]=[]),e(i,o,n[r],s)&&l.isArray(n[r])&&(n[r]=Po(n[r])),!a)}if(l.isFormData(t)&&l.isFunction(t.entries)){const i={};return l.forEachEntry(t,(o,n)=>{e(Do(o),n,i,0)}),i}return null}function Ao(t,e,i){if(l.isString(t))try{return(e||JSON.parse)(t),l.trim(t)}catch(o){if(o.name!=="SyntaxError")throw o}return(0,JSON.stringify)(t)}const me={transitional:Bt,adapter:["xhr","http","fetch"],transformRequest:[function(e,i){const o=i.getContentType()||"",n=o.indexOf("application/json")>-1,s=l.isObject(e);if(s&&l.isHTMLForm(e)&&(e=new FormData(e)),l.isFormData(e))return n?JSON.stringify(Mt(e)):e;if(l.isArrayBuffer(e)||l.isBuffer(e)||l.isStream(e)||l.isFile(e)||l.isBlob(e)||l.isReadableStream(e))return e;if(l.isArrayBufferView(e))return e.buffer;if(l.isURLSearchParams(e))return i.setContentType("application/x-www-form-urlencoded;charset=utf-8",!1),e.toString();let a;if(s){if(o.indexOf("application/x-www-form-urlencoded")>-1)return Eo(e,this.formSerializer).toString();if((a=l.isFileList(e))||o.indexOf("multipart/form-data")>-1){const c=this.env&&this.env.FormData;return Ee(a?{"files[]":e}:e,c&&new c,this.formSerializer)}}return s||n?(i.setContentType("application/json",!1),Ao(e)):e}],transformResponse:[function(e){const i=this.transitional||me.transitional,o=i&&i.forcedJSONParsing,n=this.responseType==="json";if(l.isResponse(e)||l.isReadableStream(e))return e;if(e&&l.isString(e)&&(o&&!this.responseType||n)){const r=!(i&&i.silentJSONParsing)&&n;try{return JSON.parse(e)}catch(a){if(r)throw a.name==="SyntaxError"?g.from(a,g.ERR_BAD_RESPONSE,this,null,this.response):a}}return e}],timeout:0,xsrfCookieName:"XSRF-TOKEN",xsrfHeaderName:"X-XSRF-TOKEN",maxContentLength:-1,maxBodyLength:-1,env:{FormData:C.classes.FormData,Blob:C.classes.Blob},validateStatus:function(e){return e>=200&&e<300},headers:{common:{Accept:"application/json, text/plain, */*","Content-Type":void 0}}};l.forEach(["delete","get","head","post","put","patch"],t=>{me.headers[t]={}});const Co=l.toObjectSet(["age","authorization","content-length","content-type","etag","expires","from","host","if-modified-since","if-unmodified-since","last-modified","location","max-forwards","proxy-authorization","referer","retry-after","user-agent"]),To=t=>{const e={};let i,o,n;return t&&t.split(`
`).forEach(function(r){n=r.indexOf(":"),i=r.substring(0,n).trim().toLowerCase(),o=r.substring(n+1).trim(),!(!i||e[i]&&Co[i])&&(i==="set-cookie"?e[i]?e[i].push(o):e[i]=[o]:e[i]=e[i]?e[i]+", "+o:o)}),e},zt=Symbol("internals");function ge(t){return t&&String(t).trim().toLowerCase()}function De(t){return t===!1||t==null?t:l.isArray(t)?t.map(De):String(t)}function _o(t){const e=Object.create(null),i=/([^\s,;=]+)\s*(?:=\s*([^,;]+))?/g;let o;for(;o=i.exec(t);)e[o[1]]=o[2];return e}const Lo=t=>/^[-_a-zA-Z0-9^`|~,!#$%&'*+.]+$/.test(t.trim());function Qe(t,e,i,o,n){if(l.isFunction(o))return o.call(this,e,i);if(n&&(e=i),!!l.isString(e)){if(l.isString(o))return e.indexOf(o)!==-1;if(l.isRegExp(o))return o.test(e)}}function Oo(t){return t.trim().toLowerCase().replace(/([a-z\d])(\w*)/g,(e,i,o)=>i.toUpperCase()+o)}function Ro(t,e){const i=l.toCamelCase(" "+e);["get","set","has"].forEach(o=>{Object.defineProperty(t,o+i,{value:function(n,s,r){return this[o].call(this,e,n,s,r)},configurable:!0})})}class T{constructor(e){e&&this.set(e)}set(e,i,o){const n=this;function s(a,c,d){const u=ge(c);if(!u)throw new Error("header name must be a non-empty string");const h=l.findKey(n,u);(!h||n[h]===void 0||d===!0||d===void 0&&n[h]!==!1)&&(n[h||c]=De(a))}const r=(a,c)=>l.forEach(a,(d,u)=>s(d,u,c));if(l.isPlainObject(e)||e instanceof this.constructor)r(e,i);else if(l.isString(e)&&(e=e.trim())&&!Lo(e))r(To(e),i);else if(l.isHeaders(e))for(const[a,c]of e.entries())s(c,a,o);else e!=null&&s(i,e,o);return this}get(e,i){if(e=ge(e),e){const o=l.findKey(this,e);if(o){const n=this[o];if(!i)return n;if(i===!0)return _o(n);if(l.isFunction(i))return i.call(this,n,o);if(l.isRegExp(i))return i.exec(n);throw new TypeError("parser must be boolean|regexp|function")}}}has(e,i){if(e=ge(e),e){const o=l.findKey(this,e);return!!(o&&this[o]!==void 0&&(!i||Qe(this,this[o],o,i)))}return!1}delete(e,i){const o=this;let n=!1;function s(r){if(r=ge(r),r){const a=l.findKey(o,r);a&&(!i||Qe(o,o[a],a,i))&&(delete o[a],n=!0)}}return l.isArray(e)?e.forEach(s):s(e),n}clear(e){const i=Object.keys(this);let o=i.length,n=!1;for(;o--;){const s=i[o];(!e||Qe(this,this[s],s,e,!0))&&(delete this[s],n=!0)}return n}normalize(e){const i=this,o={};return l.forEach(this,(n,s)=>{const r=l.findKey(o,s);if(r){i[r]=De(n),delete i[s];return}const a=e?Oo(s):String(s).trim();a!==s&&delete i[s],i[a]=De(n),o[a]=!0}),this}concat(...e){return this.constructor.concat(this,...e)}toJSON(e){const i=Object.create(null);return l.forEach(this,(o,n)=>{o!=null&&o!==!1&&(i[n]=e&&l.isArray(o)?o.join(", "):o)}),i}[Symbol.iterator](){return Object.entries(this.toJSON())[Symbol.iterator]()}toString(){return Object.entries(this.toJSON()).map(([e,i])=>e+": "+i).join(`
`)}get[Symbol.toStringTag](){return"AxiosHeaders"}static from(e){return e instanceof this?e:new this(e)}static concat(e,...i){const o=new this(e);return i.forEach(n=>o.set(n)),o}static accessor(e){const o=(this[zt]=this[zt]={accessors:{}}).accessors,n=this.prototype;function s(r){const a=ge(r);o[a]||(Ro(n,r),o[a]=!0)}return l.isArray(e)?e.forEach(s):s(e),this}}T.accessor(["Content-Type","Content-Length","Accept","Accept-Encoding","User-Agent","Authorization"]),l.reduceDescriptors(T.prototype,({value:t},e)=>{let i=e[0].toUpperCase()+e.slice(1);return{get:()=>t,set(o){this[i]=o}}}),l.freezeMethods(T);function Ke(t,e){const i=this||me,o=e||i,n=T.from(o.headers);let s=o.data;return l.forEach(t,function(a){s=a.call(i,s,n.normalize(),e?e.status:void 0)}),n.normalize(),s}function jt(t){return!!(t&&t.__CANCEL__)}function oe(t,e,i){g.call(this,t??"canceled",g.ERR_CANCELED,e,i),this.name="CanceledError"}l.inherits(oe,g,{__CANCEL__:!0});function Ht(t,e,i){const o=i.config.validateStatus;!i.status||!o||o(i.status)?t(i):e(new g("Request failed with status code "+i.status,[g.ERR_BAD_REQUEST,g.ERR_BAD_RESPONSE][Math.floor(i.status/100)-4],i.config,i.request,i))}function No(t){const e=/^([-+\w]{1,25})(:?\/\/|:)/.exec(t);return e&&e[1]||""}function ko(t,e){t=t||10;const i=new Array(t),o=new Array(t);let n=0,s=0,r;return e=e!==void 0?e:1e3,function(c){const d=Date.now(),u=o[s];r||(r=d),i[n]=c,o[n]=d;let h=s,y=0;for(;h!==n;)y+=i[h++],h=h%t;if(n=(n+1)%t,n===s&&(s=(s+1)%t),d-r<e)return;const v=u&&d-u;return v?Math.round(y*1e3/v):void 0}}function Io(t,e){let i=0,o=1e3/e,n,s;const r=(d,u=Date.now())=>{i=u,n=null,s&&(clearTimeout(s),s=null),t.apply(null,d)};return[(...d)=>{const u=Date.now(),h=u-i;h>=o?r(d,u):(n=d,s||(s=setTimeout(()=>{s=null,r(n)},o-h)))},()=>n&&r(n)]}const Pe=(t,e,i=3)=>{let o=0;const n=ko(50,250);return Io(s=>{const r=s.loaded,a=s.lengthComputable?s.total:void 0,c=r-o,d=n(c),u=r<=a;o=r;const h={loaded:r,total:a,progress:a?r/a:void 0,bytes:c,rate:d||void 0,estimated:d&&a&&u?(a-r)/d:void 0,event:s,lengthComputable:a!=null,[e?"download":"upload"]:!0};t(h)},i)},Gt=(t,e)=>{const i=t!=null;return[o=>e[0]({lengthComputable:i,total:t,loaded:o}),e[1]]},qt=t=>(...e)=>l.asap(()=>t(...e)),Vo=C.hasStandardBrowserEnv?function(){const e=C.navigator&&/(msie|trident)/i.test(C.navigator.userAgent),i=document.createElement("a");let o;function n(s){let r=s;return e&&(i.setAttribute("href",r),r=i.href),i.setAttribute("href",r),{href:i.href,protocol:i.protocol?i.protocol.replace(/:$/,""):"",host:i.host,search:i.search?i.search.replace(/^\?/,""):"",hash:i.hash?i.hash.replace(/^#/,""):"",hostname:i.hostname,port:i.port,pathname:i.pathname.charAt(0)==="/"?i.pathname:"/"+i.pathname}}return o=n(window.location.href),function(r){const a=l.isString(r)?n(r):r;return a.protocol===o.protocol&&a.host===o.host}}():function(){return function(){return!0}}(),Uo=C.hasStandardBrowserEnv?{write(t,e,i,o,n,s){const r=[t+"="+encodeURIComponent(e)];l.isNumber(i)&&r.push("expires="+new Date(i).toGMTString()),l.isString(o)&&r.push("path="+o),l.isString(n)&&r.push("domain="+n),s===!0&&r.push("secure"),document.cookie=r.join("; ")},read(t){const e=document.cookie.match(new RegExp("(^|;\\s*)("+t+")=([^;]*)"));return e?decodeURIComponent(e[3]):null},remove(t){this.write(t,"",Date.now()-864e5)}}:{write(){},read(){return null},remove(){}};function Fo(t){return/^([a-z][a-z\d+\-.]*:)?\/\//i.test(t)}function Bo(t,e){return e?t.replace(/\/?\/$/,"")+"/"+e.replace(/^\/+/,""):t}function Wt(t,e){return t&&!Fo(e)?Bo(t,e):e}const Jt=t=>t instanceof T?{...t}:t;function Q(t,e){e=e||{};const i={};function o(d,u,h){return l.isPlainObject(d)&&l.isPlainObject(u)?l.merge.call({caseless:h},d,u):l.isPlainObject(u)?l.merge({},u):l.isArray(u)?u.slice():u}function n(d,u,h){if(l.isUndefined(u)){if(!l.isUndefined(d))return o(void 0,d,h)}else return o(d,u,h)}function s(d,u){if(!l.isUndefined(u))return o(void 0,u)}function r(d,u){if(l.isUndefined(u)){if(!l.isUndefined(d))return o(void 0,d)}else return o(void 0,u)}function a(d,u,h){if(h in e)return o(d,u);if(h in t)return o(void 0,d)}const c={url:s,method:s,data:s,baseURL:r,transformRequest:r,transformResponse:r,paramsSerializer:r,timeout:r,timeoutMessage:r,withCredentials:r,withXSRFToken:r,adapter:r,responseType:r,xsrfCookieName:r,xsrfHeaderName:r,onUploadProgress:r,onDownloadProgress:r,decompress:r,maxContentLength:r,maxBodyLength:r,beforeRedirect:r,transport:r,httpAgent:r,httpsAgent:r,cancelToken:r,socketPath:r,responseEncoding:r,validateStatus:a,headers:(d,u)=>n(Jt(d),Jt(u),!0)};return l.forEach(Object.keys(Object.assign({},t,e)),function(u){const h=c[u]||n,y=h(t[u],e[u],u);l.isUndefined(y)&&h!==a||(i[u]=y)}),i}const Qt=t=>{const e=Q({},t);let{data:i,withXSRFToken:o,xsrfHeaderName:n,xsrfCookieName:s,headers:r,auth:a}=e;e.headers=r=T.from(r),e.url=Ut(Wt(e.baseURL,e.url),t.params,t.paramsSerializer),a&&r.set("Authorization","Basic "+btoa((a.username||"")+":"+(a.password?unescape(encodeURIComponent(a.password)):"")));let c;if(l.isFormData(i)){if(C.hasStandardBrowserEnv||C.hasStandardBrowserWebWorkerEnv)r.setContentType(void 0);else if((c=r.getContentType())!==!1){const[d,...u]=c?c.split(";").map(h=>h.trim()).filter(Boolean):[];r.setContentType([d||"multipart/form-data",...u].join("; "))}}if(C.hasStandardBrowserEnv&&(o&&l.isFunction(o)&&(o=o(e)),o||o!==!1&&Vo(e.url))){const d=n&&s&&Uo.read(s);d&&r.set(n,d)}return e},Mo=typeof XMLHttpRequest<"u"&&function(t){return new Promise(function(i,o){const n=Qt(t);let s=n.data;const r=T.from(n.headers).normalize();let{responseType:a,onUploadProgress:c,onDownloadProgress:d}=n,u,h,y,v,p;function b(){v&&v(),p&&p(),n.cancelToken&&n.cancelToken.unsubscribe(u),n.signal&&n.signal.removeEventListener("abort",u)}let f=new XMLHttpRequest;f.open(n.method.toUpperCase(),n.url,!0),f.timeout=n.timeout;function S(){if(!f)return;const A=T.from("getAllResponseHeaders"in f&&f.getAllResponseHeaders()),_={data:!a||a==="text"||a==="json"?f.responseText:f.response,status:f.status,statusText:f.statusText,headers:A,config:t,request:f};Ht(function(Y){i(Y),b()},function(Y){o(Y),b()},_),f=null}"onloadend"in f?f.onloadend=S:f.onreadystatechange=function(){!f||f.readyState!==4||f.status===0&&!(f.responseURL&&f.responseURL.indexOf("file:")===0)||setTimeout(S)},f.onabort=function(){f&&(o(new g("Request aborted",g.ECONNABORTED,t,f)),f=null)},f.onerror=function(){o(new g("Network Error",g.ERR_NETWORK,t,f)),f=null},f.ontimeout=function(){let V=n.timeout?"timeout of "+n.timeout+"ms exceeded":"timeout exceeded";const _=n.transitional||Bt;n.timeoutErrorMessage&&(V=n.timeoutErrorMessage),o(new g(V,_.clarifyTimeoutError?g.ETIMEDOUT:g.ECONNABORTED,t,f)),f=null},s===void 0&&r.setContentType(null),"setRequestHeader"in f&&l.forEach(r.toJSON(),function(V,_){f.setRequestHeader(_,V)}),l.isUndefined(n.withCredentials)||(f.withCredentials=!!n.withCredentials),a&&a!=="json"&&(f.responseType=n.responseType),d&&([y,p]=Pe(d,!0),f.addEventListener("progress",y)),c&&f.upload&&([h,v]=Pe(c),f.upload.addEventListener("progress",h),f.upload.addEventListener("loadend",v)),(n.cancelToken||n.signal)&&(u=A=>{f&&(o(!A||A.type?new oe(null,t,f):A),f.abort(),f=null)},n.cancelToken&&n.cancelToken.subscribe(u),n.signal&&(n.signal.aborted?u():n.signal.addEventListener("abort",u)));const P=No(n.url);if(P&&C.protocols.indexOf(P)===-1){o(new g("Unsupported protocol "+P+":",g.ERR_BAD_REQUEST,t));return}f.send(s||null)})},zo=(t,e)=>{const{length:i}=t=t?t.filter(Boolean):[];if(e||i){let o=new AbortController,n;const s=function(d){if(!n){n=!0,a();const u=d instanceof Error?d:this.reason;o.abort(u instanceof g?u:new oe(u instanceof Error?u.message:u))}};let r=e&&setTimeout(()=>{r=null,s(new g(`timeout ${e} of ms exceeded`,g.ETIMEDOUT))},e);const a=()=>{t&&(r&&clearTimeout(r),r=null,t.forEach(d=>{d.unsubscribe?d.unsubscribe(s):d.removeEventListener("abort",s)}),t=null)};t.forEach(d=>d.addEventListener("abort",s));const{signal:c}=o;return c.unsubscribe=()=>l.asap(a),c}},jo=function*(t,e){let i=t.byteLength;if(i<e){yield t;return}let o=0,n;for(;o<i;)n=o+e,yield t.slice(o,n),o=n},Ho=async function*(t,e){for await(const i of Go(t))yield*jo(i,e)},Go=async function*(t){if(t[Symbol.asyncIterator]){yield*t;return}const e=t.getReader();try{for(;;){const{done:i,value:o}=await e.read();if(i)break;yield o}}finally{await e.cancel()}},Kt=(t,e,i,o)=>{const n=Ho(t,e);let s=0,r,a=c=>{r||(r=!0,o&&o(c))};return new ReadableStream({async pull(c){try{const{done:d,value:u}=await n.next();if(d){a(),c.close();return}let h=u.byteLength;if(i){let y=s+=h;i(y)}c.enqueue(new Uint8Array(u))}catch(d){throw a(d),d}},cancel(c){return a(c),n.return()}},{highWaterMark:2})},Ae=typeof fetch=="function"&&typeof Request=="function"&&typeof Response=="function",Zt=Ae&&typeof ReadableStream=="function",qo=Ae&&(typeof TextEncoder=="function"?(t=>e=>t.encode(e))(new TextEncoder):async t=>new Uint8Array(await new Response(t).arrayBuffer())),Xt=(t,...e)=>{try{return!!t(...e)}catch{return!1}},Wo=Zt&&Xt(()=>{let t=!1;const e=new Request(C.origin,{body:new ReadableStream,method:"POST",get duplex(){return t=!0,"half"}}).headers.has("Content-Type");return t&&!e}),Yt=64*1024,Ze=Zt&&Xt(()=>l.isReadableStream(new Response("").body)),Ce={stream:Ze&&(t=>t.body)};Ae&&(t=>{["text","arrayBuffer","blob","formData","stream"].forEach(e=>{!Ce[e]&&(Ce[e]=l.isFunction(t[e])?i=>i[e]():(i,o)=>{throw new g(`Response type '${e}' is not supported`,g.ERR_NOT_SUPPORT,o)})})})(new Response);const Jo=async t=>{if(t==null)return 0;if(l.isBlob(t))return t.size;if(l.isSpecCompliantForm(t))return(await new Request(C.origin,{method:"POST",body:t}).arrayBuffer()).byteLength;if(l.isArrayBufferView(t)||l.isArrayBuffer(t))return t.byteLength;if(l.isURLSearchParams(t)&&(t=t+""),l.isString(t))return(await qo(t)).byteLength},Qo=async(t,e)=>{const i=l.toFiniteNumber(t.getContentLength());return i??Jo(e)},Xe={http:go,xhr:Mo,fetch:Ae&&(async t=>{let{url:e,method:i,data:o,signal:n,cancelToken:s,timeout:r,onDownloadProgress:a,onUploadProgress:c,responseType:d,headers:u,withCredentials:h="same-origin",fetchOptions:y}=Qt(t);d=d?(d+"").toLowerCase():"text";let v=zo([n,s&&s.toAbortSignal()],r),p;const b=v&&v.unsubscribe&&(()=>{v.unsubscribe()});let f;try{if(c&&Wo&&i!=="get"&&i!=="head"&&(f=await Qo(u,o))!==0){let _=new Request(e,{method:"POST",body:o,duplex:"half"}),M;if(l.isFormData(o)&&(M=_.headers.get("content-type"))&&u.setContentType(M),_.body){const[Y,Oe]=Gt(f,Pe(qt(c)));o=Kt(_.body,Yt,Y,Oe)}}l.isString(h)||(h=h?"include":"omit");const S="credentials"in Request.prototype;p=new Request(e,{...y,signal:v,method:i.toUpperCase(),headers:u.normalize().toJSON(),body:o,duplex:"half",credentials:S?h:void 0});let P=await fetch(p);const A=Ze&&(d==="stream"||d==="response");if(Ze&&(a||A&&b)){const _={};["status","statusText","headers"].forEach(ci=>{_[ci]=P[ci]});const M=l.toFiniteNumber(P.headers.get("content-length")),[Y,Oe]=a&&Gt(M,Pe(qt(a),!0))||[];P=new Response(Kt(P.body,Yt,Y,()=>{Oe&&Oe(),b&&b()}),_)}d=d||"text";let V=await Ce[l.findKey(Ce,d)||"text"](P,t);return!A&&b&&b(),await new Promise((_,M)=>{Ht(_,M,{data:V,headers:T.from(P.headers),status:P.status,statusText:P.statusText,config:t,request:p})})}catch(S){throw b&&b(),S&&S.name==="TypeError"&&/fetch/i.test(S.message)?Object.assign(new g("Network Error",g.ERR_NETWORK,t,p),{cause:S.cause||S}):g.from(S,S&&S.code,t,p)}})};l.forEach(Xe,(t,e)=>{if(t){try{Object.defineProperty(t,"name",{value:e})}catch{}Object.defineProperty(t,"adapterName",{value:e})}});const ei=t=>`- ${t}`,Ko=t=>l.isFunction(t)||t===null||t===!1,ti={getAdapter:t=>{t=l.isArray(t)?t:[t];const{length:e}=t;let i,o;const n={};for(let s=0;s<e;s++){i=t[s];let r;if(o=i,!Ko(i)&&(o=Xe[(r=String(i)).toLowerCase()],o===void 0))throw new g(`Unknown adapter '${r}'`);if(o)break;n[r||"#"+s]=o}if(!o){const s=Object.entries(n).map(([a,c])=>`adapter ${a} `+(c===!1?"is not supported by the environment":"is not available in the build"));let r=e?s.length>1?`since :
`+s.map(ei).join(`
`):" "+ei(s[0]):"as no adapter specified";throw new g("There is no suitable adapter to dispatch the request "+r,"ERR_NOT_SUPPORT")}return o},adapters:Xe};function Ye(t){if(t.cancelToken&&t.cancelToken.throwIfRequested(),t.signal&&t.signal.aborted)throw new oe(null,t)}function ii(t){return Ye(t),t.headers=T.from(t.headers),t.data=Ke.call(t,t.transformRequest),["post","put","patch"].indexOf(t.method)!==-1&&t.headers.setContentType("application/x-www-form-urlencoded",!1),ti.getAdapter(t.adapter||me.adapter)(t).then(function(o){return Ye(t),o.data=Ke.call(t,t.transformResponse,o),o.headers=T.from(o.headers),o},function(o){return jt(o)||(Ye(t),o&&o.response&&(o.response.data=Ke.call(t,t.transformResponse,o.response),o.response.headers=T.from(o.response.headers))),Promise.reject(o)})}const oi="1.7.7",et={};["object","boolean","number","function","string","symbol"].forEach((t,e)=>{et[t]=function(o){return typeof o===t||"a"+(e<1?"n ":" ")+t}});const ni={};et.transitional=function(e,i,o){function n(s,r){return"[Axios v"+oi+"] Transitional option '"+s+"'"+r+(o?". "+o:"")}return(s,r,a)=>{if(e===!1)throw new g(n(r," has been removed"+(i?" in "+i:"")),g.ERR_DEPRECATED);return i&&!ni[r]&&(ni[r]=!0,console.warn(n(r," has been deprecated since v"+i+" and will be removed in the near future"))),e?e(s,r,a):!0}};function Zo(t,e,i){if(typeof t!="object")throw new g("options must be an object",g.ERR_BAD_OPTION_VALUE);const o=Object.keys(t);let n=o.length;for(;n-- >0;){const s=o[n],r=e[s];if(r){const a=t[s],c=a===void 0||r(a,s,t);if(c!==!0)throw new g("option "+s+" must be "+c,g.ERR_BAD_OPTION_VALUE);continue}if(i!==!0)throw new g("Unknown option "+s,g.ERR_BAD_OPTION)}}const tt={assertOptions:Zo,validators:et},B=tt.validators;class K{constructor(e){this.defaults=e,this.interceptors={request:new Ft,response:new Ft}}async request(e,i){try{return await this._request(e,i)}catch(o){if(o instanceof Error){let n;Error.captureStackTrace?Error.captureStackTrace(n={}):n=new Error;const s=n.stack?n.stack.replace(/^.+\n/,""):"";try{o.stack?s&&!String(o.stack).endsWith(s.replace(/^.+\n.+\n/,""))&&(o.stack+=`
`+s):o.stack=s}catch{}}throw o}}_request(e,i){typeof e=="string"?(i=i||{},i.url=e):i=e||{},i=Q(this.defaults,i);const{transitional:o,paramsSerializer:n,headers:s}=i;o!==void 0&&tt.assertOptions(o,{silentJSONParsing:B.transitional(B.boolean),forcedJSONParsing:B.transitional(B.boolean),clarifyTimeoutError:B.transitional(B.boolean)},!1),n!=null&&(l.isFunction(n)?i.paramsSerializer={serialize:n}:tt.assertOptions(n,{encode:B.function,serialize:B.function},!0)),i.method=(i.method||this.defaults.method||"get").toLowerCase();let r=s&&l.merge(s.common,s[i.method]);s&&l.forEach(["delete","get","head","post","put","patch","common"],p=>{delete s[p]}),i.headers=T.concat(r,s);const a=[];let c=!0;this.interceptors.request.forEach(function(b){typeof b.runWhen=="function"&&b.runWhen(i)===!1||(c=c&&b.synchronous,a.unshift(b.fulfilled,b.rejected))});const d=[];this.interceptors.response.forEach(function(b){d.push(b.fulfilled,b.rejected)});let u,h=0,y;if(!c){const p=[ii.bind(this),void 0];for(p.unshift.apply(p,a),p.push.apply(p,d),y=p.length,u=Promise.resolve(i);h<y;)u=u.then(p[h++],p[h++]);return u}y=a.length;let v=i;for(h=0;h<y;){const p=a[h++],b=a[h++];try{v=p(v)}catch(f){b.call(this,f);break}}try{u=ii.call(this,v)}catch(p){return Promise.reject(p)}for(h=0,y=d.length;h<y;)u=u.then(d[h++],d[h++]);return u}getUri(e){e=Q(this.defaults,e);const i=Wt(e.baseURL,e.url);return Ut(i,e.params,e.paramsSerializer)}}l.forEach(["delete","get","head","options"],function(e){K.prototype[e]=function(i,o){return this.request(Q(o||{},{method:e,url:i,data:(o||{}).data}))}}),l.forEach(["post","put","patch"],function(e){function i(o){return function(s,r,a){return this.request(Q(a||{},{method:e,headers:o?{"Content-Type":"multipart/form-data"}:{},url:s,data:r}))}}K.prototype[e]=i(),K.prototype[e+"Form"]=i(!0)});class it{constructor(e){if(typeof e!="function")throw new TypeError("executor must be a function.");let i;this.promise=new Promise(function(s){i=s});const o=this;this.promise.then(n=>{if(!o._listeners)return;let s=o._listeners.length;for(;s-- >0;)o._listeners[s](n);o._listeners=null}),this.promise.then=n=>{let s;const r=new Promise(a=>{o.subscribe(a),s=a}).then(n);return r.cancel=function(){o.unsubscribe(s)},r},e(function(s,r,a){o.reason||(o.reason=new oe(s,r,a),i(o.reason))})}throwIfRequested(){if(this.reason)throw this.reason}subscribe(e){if(this.reason){e(this.reason);return}this._listeners?this._listeners.push(e):this._listeners=[e]}unsubscribe(e){if(!this._listeners)return;const i=this._listeners.indexOf(e);i!==-1&&this._listeners.splice(i,1)}toAbortSignal(){const e=new AbortController,i=o=>{e.abort(o)};return this.subscribe(i),e.signal.unsubscribe=()=>this.unsubscribe(i),e.signal}static source(){let e;return{token:new it(function(n){e=n}),cancel:e}}}function Xo(t){return function(i){return t.apply(null,i)}}function Yo(t){return l.isObject(t)&&t.isAxiosError===!0}const ot={Continue:100,SwitchingProtocols:101,Processing:102,EarlyHints:103,Ok:200,Created:201,Accepted:202,NonAuthoritativeInformation:203,NoContent:204,ResetContent:205,PartialContent:206,MultiStatus:207,AlreadyReported:208,ImUsed:226,MultipleChoices:300,MovedPermanently:301,Found:302,SeeOther:303,NotModified:304,UseProxy:305,Unused:306,TemporaryRedirect:307,PermanentRedirect:308,BadRequest:400,Unauthorized:401,PaymentRequired:402,Forbidden:403,NotFound:404,MethodNotAllowed:405,NotAcceptable:406,ProxyAuthenticationRequired:407,RequestTimeout:408,Conflict:409,Gone:410,LengthRequired:411,PreconditionFailed:412,PayloadTooLarge:413,UriTooLong:414,UnsupportedMediaType:415,RangeNotSatisfiable:416,ExpectationFailed:417,ImATeapot:418,MisdirectedRequest:421,UnprocessableEntity:422,Locked:423,FailedDependency:424,TooEarly:425,UpgradeRequired:426,PreconditionRequired:428,TooManyRequests:429,RequestHeaderFieldsTooLarge:431,UnavailableForLegalReasons:451,InternalServerError:500,NotImplemented:501,BadGateway:502,ServiceUnavailable:503,GatewayTimeout:504,HttpVersionNotSupported:505,VariantAlsoNegotiates:506,InsufficientStorage:507,LoopDetected:508,NotExtended:510,NetworkAuthenticationRequired:511};Object.entries(ot).forEach(([t,e])=>{ot[e]=t});function si(t){const e=new K(t),i=$t(K.prototype.request,e);return l.extend(i,K.prototype,e,{allOwnKeys:!0}),l.extend(i,e,null,{allOwnKeys:!0}),i.create=function(n){return si(Q(t,n))},i}const D=si(me);D.Axios=K,D.CanceledError=oe,D.CancelToken=it,D.isCancel=jt,D.VERSION=oi,D.toFormData=Ee,D.AxiosError=g,D.Cancel=D.CanceledError,D.all=function(e){return Promise.all(e)},D.spread=Xo,D.isAxiosError=Yo,D.mergeConfig=Q,D.AxiosHeaders=T,D.formToJSON=t=>Mt(l.isHTMLForm(t)?new FormData(t):t),D.getAdapter=ti.getAdapter,D.HttpStatusCode=ot,D.default=D;async function O(t,e,i,o,n,s){try{const r=await D.request({method:e,baseURL:t+"G2OnlineServices/"+i,headers:{Authorization:`Bearer ${o}`},data:n,...s});return{data:r.data,status:r.status}}catch(r){const a=r;if(a.response)return{data:a.response.data,status:a.response.status};throw a.request?new Error("No response received"):new Error("Request configuration error")}}const en=[{id:"-",label:"-",isSort:!1},{id:"IDVeiculo",label:"Código",isSort:!0},{id:"DataVenda",label:"Data da Venda",isSort:!0},{id:"Descricao",label:"Descrição",isSort:!0},{id:"ValorTotal",label:"Valor Total",isSort:!0},{id:"LancamentosQuitados",label:"Status Pagamento",isSort:!0},{id:"TipoVenda",label:"Tipo de Venda",isSort:!0},{id:"Download",label:"Download Nota",isSort:!1}];function ri(t,e="pt-BR"){return new Intl.NumberFormat(e,{currency:"BRL",style:"currency"}).format(t)}const tn=se`
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
`,nt=se`
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
`,Te=t=>{dispatchEvent(new CustomEvent("colibri-common-g2-alert-content",{bubbles:!0,composed:!0,detail:{title:t.title,description:t.description,type:t.type,action:t.action,onCancel:t.onCancel}})),dispatchEvent(new CustomEvent("colibri-common-g2-alert-container-action",{bubbles:!0,composed:!0,detail:{intervalId:t.action?1:void 0}}))};function Z(t){const e=atob(t.content),i=new Uint8Array(e.length);for(let c=0;c<e.length;c++)i[c]=e.charCodeAt(c);const o=t.name.split(".").pop(),n=on(o),s=new Blob([i],{type:n}),r=URL.createObjectURL(s),a=document.createElement("a");a.href=r,a.download=t.name,document.body.appendChild(a),a.click(),document.body.removeChild(a),URL.revokeObjectURL(r)}function on(t){switch(t.toLowerCase()){case"txt":return"text/plain";case"pdf":return"application/pdf";default:return"application/octet-stream"}}const nn=m`
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
`,sn=m`
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
`,ai=m`
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
`,rn=m`
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
`,an=m`
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
`,ln=m`
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
`,cn=m`
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
`;/**
 * @license
 * Copyright 2017 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */const dn={ATTRIBUTE:1,CHILD:2,PROPERTY:3,BOOLEAN_ATTRIBUTE:4,EVENT:5,ELEMENT:6},un=t=>(...e)=>({_$litDirective$:t,values:e});class hn{constructor(e){}get _$AU(){return this._$AM._$AU}_$AT(e,i,o){this._$Ct=e,this._$AM=i,this._$Ci=o}_$AS(e,i){return this.update(e,i)}update(e,i){return this.render(...i)}}/**
 * @license
 * Copyright 2017 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */class st extends hn{constructor(e){if(super(e),this.it=E,e.type!==dn.CHILD)throw Error(this.constructor.directiveName+"() can only be used in child bindings")}render(e){if(e===E||e==null)return this._t=void 0,this.it=e;if(e===G)return e;if(typeof e!="string")throw Error(this.constructor.directiveName+"() called with a non-string value");if(e===this.it)return this._t;this.it=e;const i=[e];return i.raw=i,this._t={_$litType$:this.constructor.resultType,strings:i,values:[]}}}st.directiveName="unsafeHTML",st.resultType=1;const pn=un(st);var fn=Object.defineProperty,mn=Object.getOwnPropertyDescriptor,$=(t,e,i,o)=>{for(var n=o>1?void 0:o?mn(e,i):e,s=t.length-1,r;s>=0;s--)(r=t[s])&&(n=(o?r(e,i,n):r(n))||n);return o&&n&&fn(e,i,n),n};let w=class extends W{constructor(){super(...arguments),this.memberId="",this.servicesUrl="",this.token="",this.activeStep="documentos",this.loadDataList=!1,this.dataListLots=[],this.pagination={baseQuery:"",pageSize:20,pageNumber:1,sortField:"",sortOrder:"",totalPages:0,numFound:0},this.filterList="",this.filterVehile="",this.filterIsAuction="",this.selectedLots=[],this.modalLotDetail=!1,this.loadDetail=!1,this.dataLotDetail={member:{Erros:[],PendingDocuments:[],ErrosPassiveisDeRevisao:[],Detail:{Bairro:"",CEP:"",CPFCNPJ:"",CidadeEstado:"",Complemento:"",Endereco:"",IERG:"",Nome:"",TelefoneCelular:""}},vehicles:[]},this.formDocuments=[],this.loadDocuments=!1,this.loadGatePass=!1,this.loadDownloadNote=!1,this.loadRevisao=!1,this.modalFilter=!1}static get styles(){return[tn,nt]}async firstUpdated(){await this.getLotsWithPendingIssuanceOfSalesNote()}async getLotsWithPendingIssuanceOfSalesNote(){const t=this.filterList===""?null:this.filterList==="true"?!0:this.filterList==="false"?!1:null,e=this.filterIsAuction===""?null:this.filterIsAuction==="true"?!0:this.filterIsAuction==="false"?!1:null;try{this.loadDataList=!0;const i={memberId:this.memberId,pageSize:this.pagination.pageSize,pageNumber:this.pagination.pageNumber,sortField:this.pagination.sortField,sortOrder:this.pagination.sortOrder,lancamentosQuitados:t,isAuction:e,idVeiculo:this.filterVehile},{data:o}=await O(this.servicesUrl,"POST","GetLotsWithPendingIssuanceOfSalesNote",this.token,i);this.dataListLots=o.items,this.pagination={...this.pagination,numFound:o.pagination.numFound,pageSize:o.pagination.pageSize,pageNumber:Number(o.pagination.currentPage),totalPages:o.pagination.totalPages};const n=this.dataListLots.map(s=>({dataVenda:s.DataVenda,idVeiculo:s.IDVeiculo,descricao:s.Descricao,valorTotal:s.ValorTotal,lancamentosQuitados:s.LancamentosQuitados,tipoVenda:s.TipoVenda}));this.dispatchEvent(new CustomEvent("dataPrint",{detail:n})),this.modalFilter=!1,this.loadDataList=!1}catch(i){console.error("Error fetching data:",i)}}handleOnSelectedLots(t,e,i,o,n){const s={IDTipoVendaReferencia:t,IsAuction:e,NotaEmitida:i,LancamentosQuitados:o,TipoVenda:n};this.selectedLots.findIndex(a=>a.IDTipoVendaReferencia===t)>=0?(this.selectedLots=this.selectedLots.filter(a=>a.IDTipoVendaReferencia!==t),this.selectedLots.length===0&&this.getLotsWithPendingIssuanceOfSalesNote()):(this.selectedLots.every(c=>c.TipoVenda===n)||this.selectedLots.length===0)&&(this.selectedLots=[...this.selectedLots,s],this.selectedLots.length===1&&this.getLotsWithPendingIssuanceOfSalesNote()),this.requestUpdate()}formatDatalots(t){const e=this.selectedLots.length>0?this.selectedLots[0].TipoVenda:null;return t.map(o=>{const n=!!this.selectedLots.filter(a=>a.IDTipoVendaReferencia===o.IDTipoVendaReferencia).length,s=e&&o.TipoVenda!==e,r=!o.LancamentosQuitados;return{"-":m`<colibri-common-g2-checkbox
          title=${s?"Tipo é diferente do selecionado":r?"Aguardando Pagamento":""}
          .isChecked=${n}
          .isDisabled=${s||r||!!o.NotaEmitida}
          @on-input=${()=>this.handleOnSelectedLots(o.IDTipoVendaReferencia,o.IsAuction,o.NotaEmitida,o.LancamentosQuitados,o.TipoVenda)}
        ></colibri-common-g2-checkbox>`,IDVeiculo:o.IDVeiculo,DataVenda:o.DataVenda,Descricao:o.Descricao,ValorTotal:ri(o.ValorTotal),LancamentosQuitados:m`<colibri-common-g2-badge
          type=${o.LancamentosQuitados?"success":"warning"}
          size="sm"
          text=${o.LancamentosQuitados?"Pagamento concluido":"Aguardando pagamento"}
        ></colibri-common-g2-badge>`,TipoVenda:o.DescricaoTipoVenda,Download:o.NotaEmitida?m`<div
              style="display: grid; place-items: center; width: min-content; margin-left: 12px;"
            >
              <colibri-common-g2-button-icon
                variant="success"
                size="xs"
                .icon=${nn}
                .load=${this.loadDownloadNote}
                .isDisabled=${!o.NotaEmitida}
                @onClick=${()=>this.handleOnDownloadSalesNoteAndReceiptDocument(o.IDTipoVendaReferencia,o.IsAuction)}
              ></colibri-common-g2-button-icon>
            </div> `:null}})}async handleOnChangePagination(t,e){t==="pageSize"&&(this.pagination={...this.pagination,pageNumber:1}),this.pagination={...this.pagination,[t]:e},await this.getLotsWithPendingIssuanceOfSalesNote()}async handleOnVerifyAndGetSalesNoteIssuanceDetails(){try{this.loadDetail=!0;const t={memberId:this.memberId,vehicles:this.selectedLots},{data:e}=await O(this.servicesUrl,"POST","VerifyAndGetSalesNoteIssuanceDetails",this.token,t),i={member:{Erros:e.member.Erros,PendingDocuments:e.member.PendingDocuments,ErrosPassiveisDeRevisao:e.member.ErrosPassiveisDeRevisao,Detail:e.member.Detail},vehicles:e.vehicles};this.dataLotDetail=i}catch(t){console.error("Error fetching data:",t)}finally{this.loadDetail=!1}}handleOnChangeFile(t,e){const i={idTipoAnexo:e,base64Content:t.file.split("base64,")[1],fileExtension:t.data.type.split("/")[1]};if(this.formDocuments.findIndex(n=>n.idTipoAnexo)>=0){const n=this.formDocuments.filter(s=>s.idTipoAnexo!==e);this.formDocuments=[...n,i]}else this.formDocuments=[...this.formDocuments,i]}handleOnClearFile(t){this.formDocuments=this.formDocuments.filter(e=>e.idTipoAnexo!==t)}handleOnCloseModalDetail(){this.formDocuments=[],this.dataLotDetail={member:{Erros:[],PendingDocuments:[],ErrosPassiveisDeRevisao:[],Detail:{Bairro:"",CEP:"",CPFCNPJ:"",CidadeEstado:"",Complemento:"",Endereco:"",IERG:"",Nome:"",TelefoneCelular:""}},vehicles:[]},this.modalLotDetail=!1}async handleOnDownloadSalesNoteAndReceiptDocument(t,e){try{this.loadDownloadNote=!0;const i={IDTipoVendaReferencia:t,IsAuction:e},{data:o}=await O(this.servicesUrl,"POST","DownloadSalesNoteAndReceiptDocument",this.token,i),n={name:o.detail.fileName,content:o.detail.content};Z(n)}catch{this.loadDownloadNote=!1}finally{this.loadDownloadNote=!1}}async handleOnDownloadSalesNotesAndReceiptsDocuments(t){try{this.loadDownloadNote=!0;const{data:e}=await O(this.servicesUrl,"POST","DownloadSalesNotesAndReceiptsDocuments",this.token,t);e.files.map(i=>{const o={name:i.fileName,content:i.content};Z(o)})}catch{this.loadDownloadNote=!1}finally{this.loadDownloadNote=!1}}dataBoxMember(t){return[{name:"Comprador",value:this.memberId},{name:"Nome",value:t.Nome},{name:"CPF/CNPJ",value:t.CPFCNPJ},{name:"IERG",value:t.IERG},{name:"Telefone Celular",value:t.TelefoneCelular},{name:"Endereço",value:t.Endereco},{name:"CEP",value:t.CEP},{name:"Bairro",value:t.Bairro},{name:"Cidade - Estado",value:t.CidadeEstado},{name:"Complemento",value:t.Complemento}]}datavehicle(t){const e=this.selectedLots.every(o=>o.NotaEmitida===!0),i=[{name:"Veículo",value:String(t.IDVeiculo)},{name:"Nome",value:String(t.NomeComitente)},{name:"Descrição",value:String(t.Descricao)},...t.Erros.map(o=>({name:"Pendência",value:m`<colibri-common-g2-text
          color="warning-600"
          weight="weight-light"
          >${o}</colibri-common-g2-text
        >`})),{name:"Tipo de Venda",value:t.IsAuction===!0?"Leilão: "+t.DescricaoEvento:"Compre Agora: "+t.DescricaoEvento}];return e&&i.push({name:`Download ${t.IsAuction?"nota de venda":"recibo de venda"} `,value:m`
          <colibri-common-g2-button
            size="xs"
            variant="yellow"
            @onClick=${()=>this.handleOnDownloadSalesNoteAndReceiptDocument(t.IDTipoVendaReferencia,t.IsAuction)}
            .load=${this.loadDownloadNote}
          >
            Download
          </colibri-common-g2-button>
        `}),i}async handleOnUploadDocuments(){try{this.loadDocuments=!0;const t={memberId:this.memberId,documents:this.formDocuments},{data:e}=await O(this.servicesUrl,"POST","UploadPendingMemberDocuments",this.token,t);e.resultCode===0&&(alert("Documentos enviados com sucesso"),this.formDocuments=[],this.dataLotDetail={member:{Erros:[],PendingDocuments:[],ErrosPassiveisDeRevisao:[],Detail:{Bairro:"",CEP:"",CPFCNPJ:"",CidadeEstado:"",Complemento:"",Endereco:"",IERG:"",Nome:"",TelefoneCelular:""}},vehicles:[]},this.selectedLots=[],this.modalLotDetail=!1,this.formatDatalots(this.dataListLots))}catch(t){console.error("Error fetching data:",t)}finally{this.loadDocuments=!1}}async handleOnGeneratedGatePass(){try{this.loadGatePass=!0;const t={vehicles:this.selectedLots,memberId:this.memberId},{data:e}=await O(this.servicesUrl,"POST","GenerateSalesDocuments",this.token,t);if(e.resultCode===1)throw new Error(e.resultMessage);if(e.resultCode===0){Te({title:"Atenção",type:"success",description:"Documento(s) gerado(s) com sucesso"});const i=this.selectedLots.map(o=>({idTipoVendaReferencia:o.IDTipoVendaReferencia,isAuction:o.IsAuction}));setTimeout(()=>{this.handleOnDownloadSalesNotesAndReceiptsDocuments(i)},4e3),this.formDocuments=[],this.dataLotDetail={member:{Erros:[],PendingDocuments:[],ErrosPassiveisDeRevisao:[],Detail:{Bairro:"",CEP:"",CPFCNPJ:"",CidadeEstado:"",Complemento:"",Endereco:"",IERG:"",Nome:"",TelefoneCelular:""}},vehicles:[]},this.selectedLots=[],this.modalLotDetail=!1,this.getLotsWithPendingIssuanceOfSalesNote()}}catch(t){console.error("Error fetching data:",t);const e=t;console.error("error",e.message),Te({title:"Atencao",type:"warning",description:e.message})}finally{this.loadGatePass=!1}}async handleOnRequestsRegistrationDataReview(t){try{this.loadRevisao=!0;const e={memberId:this.memberId,errosPassiveisDeRevisao:t},{data:i}=await O(this.servicesUrl,"POST","RequestsRegistrationDataReview",this.token,e);if(i.resultCode===1)throw new Error(i.resultMessage);i.resultCode===0&&Te({title:"Sucesso",type:"success",description:i.resultMessage})}catch(e){const i=e;console.error("error",i.message),Te({title:"Atencao",type:"warning",description:i.message})}finally{this.loadRevisao=!1}}handleOnSortBy(t){const e=t.detail;e.sortBy==="LancamentosQuitados"&&(this.pagination={...this.pagination,sortOrder:e.sortAsc===!0?"desc":"asc",sortField:e.sortBy},this.getLotsWithPendingIssuanceOfSalesNote())}handleToggleModalFilter(){this.modalFilter=!this.modalFilter}render(){var o;const t=!!this.dataLotDetail.member.PendingDocuments.length||!!this.dataLotDetail.member.Erros.length||!!this.dataLotDetail.member.ErrosPassiveisDeRevisao.length,e=!!((o=this.dataLotDetail.vehicles[0])!=null&&o.Erros.length),i=this.selectedLots.every(n=>n.LancamentosQuitados===!0&&n.NotaEmitida===!1);return m`
      <div class="container-documentation">
        <div class="box">
          <div class="section-box-header">
            <div class="filter-header">
              <div class="field-group">
                <div class="field-filter">
                  <colibri-common-g2-select
                    isLabel="Tipo de Venda"
                    .value=${this.filterList}
                    @on-input=${n=>this.filterIsAuction=n.detail.value}
                    .isChildren=${[{id:0,name:"Selecione uma opção",value:""},{id:1,name:"Compre Agora",value:"false"},{id:2,name:"Leilão",value:"true"}]}
                  ></colibri-common-g2-select>

                  <colibri-common-g2-select
                    isLabel="Status Pagamento"
                    .value=${this.filterList}
                    @on-input=${n=>this.filterList=n.detail.value}
                    .isChildren=${[{id:0,name:"Selecione uma opção",value:""},{id:1,name:"Aguardando pagamento",value:"false"},{id:2,name:"Pagamento concluido",value:"true"}]}
                  ></colibri-common-g2-select>

                  <colibri-common-g2-input
                    isLabel="Código Veículo"
                    isPlaceholder="Busque pelo código"
                    value=""
                    name="codigo"
                    @on-input=${n=>this.filterVehile=n.detail.value}
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
                  .isDisabled=${!this.selectedLots.length}
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
                @row-per-page=${n=>this.handleOnChangePagination("pageSize",n.detail)}
                @my-page-changed=${n=>this.handleOnChangePagination("pageNumber",n.detail.current)}
              >
              </colibri-common-g2-pagination>
            </div>
          </div>

          <div class="section-box-table scroll-bar">
            ${this.loadDataList?m`
                  <colibri-common-g2-load-table></colibri-common-g2-load-table>
                `:m`
                  <colibri-common-g2-table-default
                    .load=${this.loadDataList}
                    .theadData=${en}
                    .tbodyData=${this.formatDatalots(this.dataListLots)}
                    isSort
                    .sortBy=${this.pagination.sortField}
                    @my-sortBy=${n=>this.handleOnSortBy(n)}
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
                @row-per-page=${n=>this.handleOnChangePagination("pageSize",n.detail)}
                @my-page-changed=${n=>this.handleOnChangePagination("pageNumber",n.detail.current)}
              >
              </colibri-common-g2-pagination>
            </div>
          </div>
        </div>

        ${this.modalLotDetail?m`
              <colibri-common-g2-modal
                @on-close=${this.handleOnCloseModalDetail}
                title="Detalhes do lote"
                size="size-lg"
              >
                <div class="dialog-container">
                  ${this.loadDetail?m` <g2-load-modal></g2-load-modal> `:m`
                        <div class="dialog-content bar">
                          <div class="dialog-section-left">
                            <colibri-common-g2-heading weight="weight-bold"
                              >Dados comprador</colibri-common-g2-heading
                            >

                            ${this.dataLotDetail.member.ErrosPassiveisDeRevisao.length?m`
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
                                        Divergência no cadastro do arrematante
                                      </h1>

                                      <div class="card-error-info">
                                        ${this.dataLotDetail.member.ErrosPassiveisDeRevisao.map(n=>m`<span>${pn(n)}</span>`)}
                                      </div>
                                    </div>
                                  </div>
                                `:null}
                            ${this.dataLotDetail.member.Erros.length?m`
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
                                        Divergência no cadastro do arrematante
                                      </h1>

                                      <div class="card-error-info">
                                        ${this.dataLotDetail.member.Erros.map(n=>m` <span>${n}</span> `)}
                                      </div>
                                    </div>
                                  </div>
                                `:null}
                            ${this.dataLotDetail.member.PendingDocuments.length?m`
                      <div class="upload-docs">
                        <colibri-common-g2-heading weight="weight-bold"
                          >Documentos pendentes de envio</colibri-common-g2-heading
                        >
                        <colibri-common-g2-text size="size-1" color="warning-400">
                        Para emissão da Nota/Recibo de Venda é necessário anexar os seguintes documentos abaixo.
                      </colibri-common-g2-text>
      
                        <div class="upload-docs-form">
                          ${this.dataLotDetail.member.PendingDocuments.map(n=>{var s,r;return m`
                              <div class="field-group">
                                <colibri-common-g2-input
                                  type="file"
                                  isLabel=${n.Item2}
                                  value=${(r=(s=this.formDocuments)==null?void 0:s.filter(a=>a.idTipoAnexo===n.Item1)[0])==null?void 0:r.base64Content}
                                  name="doc"
                                  @on-input=${a=>this.handleOnChangeFile(a.detail.file,n.Item1)}
                                >
                                </colibri-common-g2-input>
                                ${this.formDocuments.filter(a=>a.idTipoAnexo===n.Item1).length?m`
                                      <button
                                        class="button-clear-file"
                                        @click=${()=>this.handleOnClearFile(n.Item1)}
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
                            ${!this.dataLotDetail.member.Erros.length&&!this.dataLotDetail.member.PendingDocuments.length&&this.loadDetail===!1?m`
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
                              ${this.dataLotDetail.vehicles.map(n=>m`
                                  <colibri-common-g2-box
                                    .data=${this.datavehicle({...n})}
                                  >
                                  </colibri-common-g2-box>
                                `)}
                            </div>
                          </div>
                        </div>

                        <div class="dialog-footer" style="justify-content: space-between;">
                          <div class="message-warning">
                            ${!e&&!t&&i?m`
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

                            ${this.dataLotDetail.member.PendingDocuments.length?m`
                                  <colibri-common-g2-button
                                    variant="yellow"
                                    .load=${this.loadDocuments}
                                    size="sm"
                                    .isDisabled=${!this.formDocuments.length}
                                    @onClick=${()=>this.handleOnUploadDocuments()}
                                    >Enviar documentos</colibri-common-g2-button
                                  >
                                `:null}
                            ${!e&&!t&&i?m`
                                  <colibri-common-g2-button
                                    variant="yellow"
                                    .load=${this.loadGatePass}
                                    size="sm"
                                    .isDisabled=${!!this.formDocuments.length}
                                    @onClick=${()=>this.handleOnGeneratedGatePass()}
                                    >Emitir documento</colibri-common-g2-button
                                  >
                                `:m``}
                            ${this.dataLotDetail.member.ErrosPassiveisDeRevisao.length?m`
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
        ${this.modalFilter?m`
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
                          @on-input=${n=>this.filterIsAuction=n.detail.value}
                          .isChildren=${[{id:0,name:"Selecione uma opção",value:""},{id:1,name:"Compre Agora",value:"false"},{id:2,name:"Leilão",value:"true"}]}
                        ></colibri-common-g2-select>

                        <colibri-common-g2-select
                          isLabel="Status Pagamento"
                          .value=${this.filterList}
                          @on-input=${n=>this.filterList=n.detail.value}
                          .isChildren=${[{id:0,name:"Selecione uma opção",value:""},{id:1,name:"Aguardando pagamento",value:"false"},{id:2,name:"Pagamento concluido",value:"true"}]}
                        ></colibri-common-g2-select>

                        <colibri-common-g2-input
                          isLabel="Código Veículo"
                          isPlaceholder="Busque pelo código"
                          value=""
                          name="codigo"
                          @on-input=${n=>this.filterVehile=n.detail.value}
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
      </div>
    `}};$([I()],w.prototype,"memberId",2),$([I()],w.prototype,"servicesUrl",2),$([I()],w.prototype,"token",2),$([x()],w.prototype,"activeStep",2),$([x()],w.prototype,"loadDataList",2),$([x()],w.prototype,"dataListLots",2),$([x()],w.prototype,"pagination",2),$([x()],w.prototype,"filterList",2),$([x()],w.prototype,"filterVehile",2),$([x()],w.prototype,"filterIsAuction",2),$([x()],w.prototype,"selectedLots",2),$([x()],w.prototype,"modalLotDetail",2),$([x()],w.prototype,"loadDetail",2),$([x()],w.prototype,"dataLotDetail",2),$([x()],w.prototype,"formDocuments",2),$([x()],w.prototype,"loadDocuments",2),$([x()],w.prototype,"loadGatePass",2),$([x()],w.prototype,"loadDownloadNote",2),$([x()],w.prototype,"loadRevisao",2),$([x()],w.prototype,"modalFilter",2),w=$([Me("page-documents")],w);const gn=se`
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
`,bn=[{id:"-",label:"-",isSort:!1},{id:"IDVeiculo",label:"Código",isSort:!0},{id:"DataVenda",label:"Data da Venda",isSort:!0},{id:"LancamentosQuitados",label:"Estadia Pendente",isSort:!0},{id:"Descricao",label:"Descrição",isSort:!0},{id:"ValorTotal",label:"Valor Total",isSort:!0},{id:"DataValidadeGatePass",label:"Vencimento",isSort:!0},{id:"TipoDocumento",label:"Documento",isSort:!0},{id:"TipoMonta",label:"Monta",isSort:!0},{id:"TipoVenda",label:"Tipo de Venda",isSort:!0}];function _e(t){const e=new Date(t),i={day:"2-digit",month:"2-digit",year:"numeric"};return new Intl.DateTimeFormat("pt-BR",i).format(e)}var yn=Object.defineProperty,vn=Object.getOwnPropertyDescriptor,N=(t,e,i,o)=>{for(var n=o>1?void 0:o?vn(e,i):e,s=t.length-1,r;s>=0;s--)(r=t[s])&&(n=(o?r(e,i,n):r(n))||n);return o&&n&&yn(e,i,n),n};let R=class extends W{constructor(){super(...arguments),this.memberId="",this.servicesUrl="",this.token="",this.loadDataList=!1,this.dataList=[],this.pagination={baseQuery:"",pageSize:20,pageNumber:1,sortField:"",sortOrder:"",totalPages:0,numFound:0},this.modalGatePass=!1,this.loadGenerateGatePass=!1,this.errorGenerateGatePass="",this.detailGatePass=[],this.selectedLots=[]}static get styles(){return[gn,nt]}async firstUpdated(){await this.GetLotsWithPendingIssuanceOfGatePass()}async GetLotsWithPendingIssuanceOfGatePass(){try{this.loadDataList=!0;const t={memberId:this.memberId,pageSize:this.pagination.pageSize,pageNumber:this.pagination.pageNumber,sortField:this.pagination.sortField,sortOrder:this.pagination.sortOrder},{data:e}=await O(this.servicesUrl,"POST","GetLotsWithPendingIssuanceOfGatePass",this.token,t);this.dataList=e.items,this.pagination={...this.pagination,numFound:e.pagination.numFound,pageSize:e.pagination.pageSize,pageNumber:Number(e.pagination.currentPage),totalPages:e.pagination.totalPages};const i=this.dataList.map(o=>({dataVenda:o.DataVenda,idVeiculo:o.IDVeiculo,descricao:o.Descricao,valorTotal:o.ValorTotal,lancamentosQuitados:o.LancamentosQuitados,tipoVenda:o.TipoVenda,dataValidadeGatePass:o.DataValidadeGatePass,tipoDocumento:o.TipoDocumento,tipoMonta:o.TipoMonta,descricaoEvento:o.DescricaoEvento}));this.dispatchEvent(new CustomEvent("dataPrint",{detail:i})),this.loadDataList=!1}catch(t){console.error("Error fetching data:",t)}}async handleOnChangePagination(t,e){t==="pageSize"&&(this.pagination={...this.pagination,pageNumber:1}),this.pagination={...this.pagination,[t]:e},await this.GetLotsWithPendingIssuanceOfGatePass()}handleOnShowDetail(t){this.detailGatePass=t,this.modalGatePass=!this.modalGatePass}handleOnCloseDetail(){this.detailGatePass=[],this.modalGatePass=!this.modalGatePass}async handleOnGenerateGatePass(){try{this.loadGenerateGatePass=!0;const t={vehicles:this.detailGatePass.map(o=>({IDTipoVendaReferencia:o.IDTipoVendaReferencia,IsAuction:o.IsAuction}))},{data:e}=await O(this.servicesUrl,"POST","GenerateGatePass",this.token,t);if(e.resultCode===1)throw this.errorGenerateGatePass=e.resultCode,e.resultMessage;const i={name:e.items[0].FileName,content:e.items[0].Content};Z(i),this.handleOnCloseDetail(),this.GetLotsWithPendingIssuanceOfGatePass()}catch(t){console.error("Error fetching data:",t)}finally{this.loadGenerateGatePass=!1}}handleOnSelectedLots(t,e){const i={...e,IDTipoVendaReferencia:t};if(this.selectedLots.findIndex(n=>n.IDTipoVendaReferencia===t)>=0){const n=this.selectedLots.filter(s=>s.IDTipoVendaReferencia!==t);this.selectedLots=n}else this.selectedLots=[...this.selectedLots,i]}formatDatalots(t){return t.map(i=>({"-":m`<colibri-common-g2-checkbox
      title=${i.LancamentosQuitados?"":"Aguardando Pagamento"}
        .isDisabled=${!i.LancamentosQuitados}
        .isChecked=${!!this.selectedLots.filter(o=>o.IDTipoVendaReferencia===i.IDTipoVendaReferencia).length}
        @on-input=${()=>this.handleOnSelectedLots(i.IDTipoVendaReferencia,i)}
      ></colibri-common-g2-checkbox>`,IDVeiculo:i.IDVeiculo,DataVenda:_e(i.DataVenda),LancamentosQuitados:m`<colibri-common-g2-badge
        size="sm"
        text=${i.LancamentosQuitados?"Não":"Sim"}
        type=${i.LancamentosQuitados?"success":"orange"}
      ></colibri-common-g2-badge>`,Descricao:i.Descricao,ValorTotal:ri(i.ValorTotal),DataValidadeGatePass:_e(i.DataValidadeGatePass),TipoDocumento:i.TipoDocumento,TipoMonta:i.TipoMonta,TipoVenda:i.TipoVenda+": "+i.DescricaoEvento,Doc:m`
        <div style="margin-left: 32px;">
          <colibri-common-g2-button-icon
            variant="gray"
            size="xs"
            .icon=${sn}
          >
          </colibri-common-g2-button-icon>
        </div>
      `}))}dataBoxGatePass(t,e){return[{name:"Dados Gatepass",value:`${e+1}`},{name:"Veículo",value:t.IDVeiculo},{name:"Data Venda",value:_e(t.DataVenda?t.DataVenda:Date())},{name:"Vencimento",value:_e(t.DataValidadeGatePass?t.DataValidadeGatePass:Date())},{name:"Tipo de Venda",value:t.IsAuction===!0?"Leilão: "+t.DescricaoEvento:"Compre Agora: "+t.DescricaoEvento},{name:"Descrição",value:t.DescricaoResumida}]}render(){return m`
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
            ${this.loadDataList?m`
                  <colibri-common-g2-load-table></colibri-common-g2-load-table>
                `:m`
                  <colibri-common-g2-table-default
                    .load=${this.loadDataList}
                    .theadData=${bn}
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

        ${this.modalGatePass?m`
          <colibri-common-g2-modal
            title="Detalhe Gatepass"
            @on-close=${this.handleOnCloseDetail}
          >
            <div class="dialog-container">
              <div class="dialog-content bar">
                ${this.errorGenerateGatePass?m`
                      <card-message
                        .messages=${[{title:"Atenção",message:this.errorGenerateGatePass}]}
                        type="warning"
                      ></card-message>
                    `:null}
  
                <div class="dialog-box-group">
                  ${this.detailGatePass.map((t,e)=>m`
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
    `}};N([I()],R.prototype,"memberId",2),N([I()],R.prototype,"servicesUrl",2),N([I()],R.prototype,"token",2),N([x()],R.prototype,"loadDataList",2),N([x()],R.prototype,"dataList",2),N([x()],R.prototype,"pagination",2),N([x()],R.prototype,"modalGatePass",2),N([x()],R.prototype,"loadGenerateGatePass",2),N([x()],R.prototype,"errorGenerateGatePass",2),N([x()],R.prototype,"detailGatePass",2),N([x()],R.prototype,"selectedLots",2),R=N([Me("page-gate-pass")],R);const xn=se`
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
`,wn={info:ln,success:rn,error:an,warning:ai,ghost:ai};function $n({title:t,type:e,action:i,description:o,closeToast:n}){const s={info:"blue",success:"green",error:"red",warning:"warning"};return m`
    <article
      style=${`background-color: var(--${s[e]}-50)`}
      popover="manual"
      id="toast-container"
      class=${`toast newest ${e}`}
    >
      ${wn[e]||"info"}

      <div class="toast-message">
        <colibri-common-ui-text
          style="line-height: 16px"
          color=${`${s[e]}-600`}
          size="size-2"
          weight="weight-medium"
          >${t}</colibri-common-ui-text
        >

        ${o?m`
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
        ${cn}
      </button>

      ${i?m`
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
  `}se`
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
`;function Le({title:t="",description:e="",type:i="info",action:o}){const n=$n({title:t,type:i,action:o,description:e,closeToast:a}),s=document.createElement("div");wt(n,s);const r=s.firstElementChild;document.body.appendChild(r),r.showPopover(),setTimeout(()=>{r.hidePopover(),r.remove()},5e5),r.addEventListener("toggle",c=>{c.newState==="open"&&Sn()});function a(){r.hidePopover(),r.remove()}}function Sn(){document.querySelectorAll(".toast").forEach(e=>{if(e.classList.contains("newest"))e.style.top="16px",e.classList.remove("newest");else{const i=e.style.top.replace("px",""),o=parseInt(i)+88;e.style.top=`${o}px`}})}var En=Object.defineProperty,Dn=Object.getOwnPropertyDescriptor,ne=(t,e,i,o)=>{for(var n=o>1?void 0:o?Dn(e,i):e,s=t.length-1,r;s>=0;s--)(r=t[s])&&(n=(o?r(e,i,n):r(n))||n);return o&&n&&En(e,i,n),n};let X=class extends W{constructor(){super(...arguments),this.memberId="",this.servicesUrl="",this.token="",this.activeStep="Nota/Recibo de Venda",this.dataprint=[]}static get styles(){return[xn,nt]}handleStepChange(t){this.activeStep=t}async exportLotsWithPendingIssuanceOfSalesNoteToExcel(){try{const t={itens:this.dataprint},{data:e}=await O(this.servicesUrl,"POST","exportLotsWithPendingIssuanceOfSalesNoteToExcel",this.token,t);if(e.resultCode===0){const i={name:`activeStep_${this.activeStep}.xlsx`,content:e.content};Z(i)}}catch{Le({title:"Atencao",type:"warning",description:"Não foi possivel gerar excel da página."})}}async exportLotsWithPendingIssuanceOfGatePassToExcel(){try{const t={itens:this.dataprint},{data:e}=await O(this.servicesUrl,"POST","exportLotsWithPendingIssuanceOfGatePassToExcel",this.token,t);if(e.resultCode===0){const i={name:`activeStep_${this.activeStep}.xlsx`,content:e.content};Z(i)}}catch{Le({title:"Atencao",type:"warning",description:"Não foi possivel gerar excel da página."})}}async printLotsWithPendingIssuanceOfSalesNoteToPdf(){try{const t={itens:this.dataprint},{data:e}=await O(this.servicesUrl,"POST","printLotsWithPendingIssuanceOfSalesNoteToPdf",this.token,t);if(e.resultCode===0){const i={name:`activeStep_${this.activeStep}.pdf`,content:e.content};Z(i)}}catch{Le({title:"Atencao",type:"warning",description:"Não foi possivel gerar excel da página."})}}async printLotsWithPendingIssuanceOfGatePassToPdf(){try{const t={itens:this.dataprint},{data:e}=await O(this.servicesUrl,"POST","printLotsWithPendingIssuanceOfGatePassToPdf",this.token,t);if(e.resultCode===0){const i={name:`activeStep_${this.activeStep}.pdf`,content:e.content};Z(i)}}catch{Le({title:"Atencao",type:"warning",description:"Não foi possivel gerar excel da página."})}}render(){const t=[{item:m`<page-documents
          memberId=${this.memberId}
          servicesUrl=${this.servicesUrl}
          token=${this.token}
          @dataPrint=${e=>this.dataprint=e.detail}
        ></page-documents>`,name:"Nota/Recibo de Venda"},{item:m`<page-gate-pass
          memberId=${this.memberId}
          servicesUrl=${this.servicesUrl}
          token=${this.token}
          @dataPrint=${e=>this.dataprint=e.detail}
        ></page-gate-pass>`,name:"Gatepass"}];return m`
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
    `}};ne([I()],X.prototype,"memberId",2),ne([I()],X.prototype,"servicesUrl",2),ne([I()],X.prototype,"token",2),ne([x()],X.prototype,"activeStep",2),ne([x()],X.prototype,"dataprint",2),X=ne([Me("page-documentation")],X)});
