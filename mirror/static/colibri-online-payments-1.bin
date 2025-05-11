(function(ie){typeof define=="function"&&define.amd?define(ie):ie()})(function(){"use strict";/*! colibri-online-payments - v1.0.0 *//**
 * @license
 * Copyright 2019 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */var fi;const ie=globalThis,Be=ie.ShadowRoot&&(ie.ShadyCSS===void 0||ie.ShadyCSS.nativeShadow)&&"adoptedStyleSheets"in Document.prototype&&"replace"in CSSStyleSheet.prototype,je=Symbol(),ft=new WeakMap;let gt=class{constructor(e,i,o){if(this._$cssResult$=!0,o!==je)throw Error("CSSResult is not constructable. Use `unsafeCSS` or `css` instead.");this.cssText=e,this.t=i}get styleSheet(){let e=this.o;const i=this.t;if(Be&&e===void 0){const o=i!==void 0&&i.length===1;o&&(e=ft.get(i)),e===void 0&&((this.o=e=new CSSStyleSheet).replaceSync(this.cssText),o&&ft.set(i,e))}return e}toString(){return this.cssText}};const gi=t=>new gt(typeof t=="string"?t:t+"",void 0,je),_=(t,...e)=>{const i=t.length===1?t[0]:e.reduce((o,s,r)=>o+(a=>{if(a._$cssResult$===!0)return a.cssText;if(typeof a=="number")return a;throw Error("Value passed to 'css' function must be a 'css' function result: "+a+". Use 'unsafeCSS' to pass non-literal values, but take care to ensure page security.")})(s)+t[r+1],t[0]);return new gt(i,t,je)},bi=(t,e)=>{if(Be)t.adoptedStyleSheets=e.map(i=>i instanceof CSSStyleSheet?i:i.styleSheet);else for(const i of e){const o=document.createElement("style"),s=ie.litNonce;s!==void 0&&o.setAttribute("nonce",s),o.textContent=i.cssText,t.appendChild(o)}},bt=Be?t=>t:t=>t instanceof CSSStyleSheet?(e=>{let i="";for(const o of e.cssRules)i+=o.cssText;return gi(i)})(t):t;/**
 * @license
 * Copyright 2017 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */const{is:yi,defineProperty:xi,getOwnPropertyDescriptor:vi,getOwnPropertyNames:wi,getOwnPropertySymbols:$i,getPrototypeOf:Ci}=Object,Z=globalThis,yt=Z.trustedTypes,Si=yt?yt.emptyScript:"",Ve=Z.reactiveElementPolyfillSupport,ue=(t,e)=>t,Pe={toAttribute(t,e){switch(e){case Boolean:t=t?Si:null;break;case Object:case Array:t=t==null?t:JSON.stringify(t)}return t},fromAttribute(t,e){let i=t;switch(e){case Boolean:i=t!==null;break;case Number:i=t===null?null:Number(t);break;case Object:case Array:try{i=JSON.parse(t)}catch{i=null}}return i}},qe=(t,e)=>!yi(t,e),xt={attribute:!0,type:String,converter:Pe,reflect:!1,hasChanged:qe};Symbol.metadata??(Symbol.metadata=Symbol("metadata")),Z.litPropertyMetadata??(Z.litPropertyMetadata=new WeakMap);let re=class extends HTMLElement{static addInitializer(e){this._$Ei(),(this.l??(this.l=[])).push(e)}static get observedAttributes(){return this.finalize(),this._$Eh&&[...this._$Eh.keys()]}static createProperty(e,i=xt){if(i.state&&(i.attribute=!1),this._$Ei(),this.elementProperties.set(e,i),!i.noAccessor){const o=Symbol(),s=this.getPropertyDescriptor(e,o,i);s!==void 0&&xi(this.prototype,e,s)}}static getPropertyDescriptor(e,i,o){const{get:s,set:r}=vi(this.prototype,e)??{get(){return this[i]},set(a){this[i]=a}};return{get(){return s==null?void 0:s.call(this)},set(a){const n=s==null?void 0:s.call(this);r.call(this,a),this.requestUpdate(e,n,o)},configurable:!0,enumerable:!0}}static getPropertyOptions(e){return this.elementProperties.get(e)??xt}static _$Ei(){if(this.hasOwnProperty(ue("elementProperties")))return;const e=Ci(this);e.finalize(),e.l!==void 0&&(this.l=[...e.l]),this.elementProperties=new Map(e.elementProperties)}static finalize(){if(this.hasOwnProperty(ue("finalized")))return;if(this.finalized=!0,this._$Ei(),this.hasOwnProperty(ue("properties"))){const i=this.properties,o=[...wi(i),...$i(i)];for(const s of o)this.createProperty(s,i[s])}const e=this[Symbol.metadata];if(e!==null){const i=litPropertyMetadata.get(e);if(i!==void 0)for(const[o,s]of i)this.elementProperties.set(o,s)}this._$Eh=new Map;for(const[i,o]of this.elementProperties){const s=this._$Eu(i,o);s!==void 0&&this._$Eh.set(s,i)}this.elementStyles=this.finalizeStyles(this.styles)}static finalizeStyles(e){const i=[];if(Array.isArray(e)){const o=new Set(e.flat(1/0).reverse());for(const s of o)i.unshift(bt(s))}else e!==void 0&&i.push(bt(e));return i}static _$Eu(e,i){const o=i.attribute;return o===!1?void 0:typeof o=="string"?o:typeof e=="string"?e.toLowerCase():void 0}constructor(){super(),this._$Ep=void 0,this.isUpdatePending=!1,this.hasUpdated=!1,this._$Em=null,this._$Ev()}_$Ev(){var e;this._$ES=new Promise(i=>this.enableUpdating=i),this._$AL=new Map,this._$E_(),this.requestUpdate(),(e=this.constructor.l)==null||e.forEach(i=>i(this))}addController(e){var i;(this._$EO??(this._$EO=new Set)).add(e),this.renderRoot!==void 0&&this.isConnected&&((i=e.hostConnected)==null||i.call(e))}removeController(e){var i;(i=this._$EO)==null||i.delete(e)}_$E_(){const e=new Map,i=this.constructor.elementProperties;for(const o of i.keys())this.hasOwnProperty(o)&&(e.set(o,this[o]),delete this[o]);e.size>0&&(this._$Ep=e)}createRenderRoot(){const e=this.shadowRoot??this.attachShadow(this.constructor.shadowRootOptions);return bi(e,this.constructor.elementStyles),e}connectedCallback(){var e;this.renderRoot??(this.renderRoot=this.createRenderRoot()),this.enableUpdating(!0),(e=this._$EO)==null||e.forEach(i=>{var o;return(o=i.hostConnected)==null?void 0:o.call(i)})}enableUpdating(e){}disconnectedCallback(){var e;(e=this._$EO)==null||e.forEach(i=>{var o;return(o=i.hostDisconnected)==null?void 0:o.call(i)})}attributeChangedCallback(e,i,o){this._$AK(e,o)}_$EC(e,i){var r;const o=this.constructor.elementProperties.get(e),s=this.constructor._$Eu(e,o);if(s!==void 0&&o.reflect===!0){const a=(((r=o.converter)==null?void 0:r.toAttribute)!==void 0?o.converter:Pe).toAttribute(i,o.type);this._$Em=e,a==null?this.removeAttribute(s):this.setAttribute(s,a),this._$Em=null}}_$AK(e,i){var r;const o=this.constructor,s=o._$Eh.get(e);if(s!==void 0&&this._$Em!==s){const a=o.getPropertyOptions(s),n=typeof a.converter=="function"?{fromAttribute:a.converter}:((r=a.converter)==null?void 0:r.fromAttribute)!==void 0?a.converter:Pe;this._$Em=s,this[s]=n.fromAttribute(i,a.type),this._$Em=null}}requestUpdate(e,i,o){if(e!==void 0){if(o??(o=this.constructor.getPropertyOptions(e)),!(o.hasChanged??qe)(this[e],i))return;this.P(e,i,o)}this.isUpdatePending===!1&&(this._$ES=this._$ET())}P(e,i,o){this._$AL.has(e)||this._$AL.set(e,i),o.reflect===!0&&this._$Em!==e&&(this._$Ej??(this._$Ej=new Set)).add(e)}async _$ET(){this.isUpdatePending=!0;try{await this._$ES}catch(i){Promise.reject(i)}const e=this.scheduleUpdate();return e!=null&&await e,!this.isUpdatePending}scheduleUpdate(){return this.performUpdate()}performUpdate(){var o;if(!this.isUpdatePending)return;if(!this.hasUpdated){if(this.renderRoot??(this.renderRoot=this.createRenderRoot()),this._$Ep){for(const[r,a]of this._$Ep)this[r]=a;this._$Ep=void 0}const s=this.constructor.elementProperties;if(s.size>0)for(const[r,a]of s)a.wrapped!==!0||this._$AL.has(r)||this[r]===void 0||this.P(r,this[r],a)}let e=!1;const i=this._$AL;try{e=this.shouldUpdate(i),e?(this.willUpdate(i),(o=this._$EO)==null||o.forEach(s=>{var r;return(r=s.hostUpdate)==null?void 0:r.call(s)}),this.update(i)):this._$EU()}catch(s){throw e=!1,this._$EU(),s}e&&this._$AE(i)}willUpdate(e){}_$AE(e){var i;(i=this._$EO)==null||i.forEach(o=>{var s;return(s=o.hostUpdated)==null?void 0:s.call(o)}),this.hasUpdated||(this.hasUpdated=!0,this.firstUpdated(e)),this.updated(e)}_$EU(){this._$AL=new Map,this.isUpdatePending=!1}get updateComplete(){return this.getUpdateComplete()}getUpdateComplete(){return this._$ES}shouldUpdate(e){return!0}update(e){this._$Ej&&(this._$Ej=this._$Ej.forEach(i=>this._$EC(i,this[i]))),this._$EU()}updated(e){}firstUpdated(e){}};re.elementStyles=[],re.shadowRootOptions={mode:"open"},re[ue("elementProperties")]=new Map,re[ue("finalized")]=new Map,Ve==null||Ve({ReactiveElement:re}),(Z.reactiveElementVersions??(Z.reactiveElementVersions=[])).push("2.0.4");/**
 * @license
 * Copyright 2017 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */const me=globalThis,ke=me.trustedTypes,vt=ke?ke.createPolicy("lit-html",{createHTML:t=>t}):void 0,wt="$lit$",Y=`lit$${(Math.random()+"").slice(9)}$`,$t="?"+Y,Pi=`<${$t}>`,oe=document,fe=()=>oe.createComment(""),ge=t=>t===null||typeof t!="object"&&typeof t!="function",Ct=Array.isArray,ki=t=>Ct(t)||typeof(t==null?void 0:t[Symbol.iterator])=="function",He=`[ 	
\f\r]`,be=/<(?:(!--|\/[^a-zA-Z])|(\/?[a-zA-Z][^>\s]*)|(\/?$))/g,St=/-->/g,Pt=/>/g,se=RegExp(`>|${He}(?:([^\\s"'>=/]+)(${He}*=${He}*(?:[^ 	
\f\r"'\`<>=]|("|')|))|$)`,"g"),kt=/'/g,At=/"/g,Dt=/^(?:script|style|textarea|title)$/i,Et=t=>(e,...i)=>({_$litType$:t,strings:e,values:i}),h=Et(1),Ae=Et(2),ne=Symbol.for("lit-noChange"),O=Symbol.for("lit-nothing"),Tt=new WeakMap,ae=oe.createTreeWalker(oe,129);function Ot(t,e){if(!Array.isArray(t)||!t.hasOwnProperty("raw"))throw Error("invalid template strings array");return vt!==void 0?vt.createHTML(e):e}const Ai=(t,e)=>{const i=t.length-1,o=[];let s,r=e===2?"<svg>":"",a=be;for(let n=0;n<i;n++){const c=t[n];let m,p,l=-1,v=0;for(;v<c.length&&(a.lastIndex=v,p=a.exec(c),p!==null);)v=a.lastIndex,a===be?p[1]==="!--"?a=St:p[1]!==void 0?a=Pt:p[2]!==void 0?(Dt.test(p[2])&&(s=RegExp("</"+p[2],"g")),a=se):p[3]!==void 0&&(a=se):a===se?p[0]===">"?(a=s??be,l=-1):p[1]===void 0?l=-2:(l=a.lastIndex-p[2].length,m=p[1],a=p[3]===void 0?se:p[3]==='"'?At:kt):a===At||a===kt?a=se:a===St||a===Pt?a=be:(a=se,s=void 0);const E=a===se&&t[n+1].startsWith("/>")?" ":"";r+=a===be?c+Pi:l>=0?(o.push(m),c.slice(0,l)+wt+c.slice(l)+Y+E):c+Y+(l===-2?n:E)}return[Ot(t,r+(t[i]||"<?>")+(e===2?"</svg>":"")),o]};class ye{constructor({strings:e,_$litType$:i},o){let s;this.parts=[];let r=0,a=0;const n=e.length-1,c=this.parts,[m,p]=Ai(e,i);if(this.el=ye.createElement(m,o),ae.currentNode=this.el.content,i===2){const l=this.el.content.firstChild;l.replaceWith(...l.childNodes)}for(;(s=ae.nextNode())!==null&&c.length<n;){if(s.nodeType===1){if(s.hasAttributes())for(const l of s.getAttributeNames())if(l.endsWith(wt)){const v=p[a++],E=s.getAttribute(l).split(Y),f=/([.?@])?(.*)/.exec(v);c.push({type:1,index:r,name:f[2],strings:E,ctor:f[1]==="."?Ei:f[1]==="?"?Ti:f[1]==="@"?Oi:De}),s.removeAttribute(l)}else l.startsWith(Y)&&(c.push({type:6,index:r}),s.removeAttribute(l));if(Dt.test(s.tagName)){const l=s.textContent.split(Y),v=l.length-1;if(v>0){s.textContent=ke?ke.emptyScript:"";for(let E=0;E<v;E++)s.append(l[E],fe()),ae.nextNode(),c.push({type:2,index:++r});s.append(l[v],fe())}}}else if(s.nodeType===8)if(s.data===$t)c.push({type:2,index:r});else{let l=-1;for(;(l=s.data.indexOf(Y,l+1))!==-1;)c.push({type:7,index:r}),l+=Y.length-1}r++}}static createElement(e,i){const o=oe.createElement("template");return o.innerHTML=e,o}}function le(t,e,i=t,o){var a,n;if(e===ne)return e;let s=o!==void 0?(a=i._$Co)==null?void 0:a[o]:i._$Cl;const r=ge(e)?void 0:e._$litDirective$;return(s==null?void 0:s.constructor)!==r&&((n=s==null?void 0:s._$AO)==null||n.call(s,!1),r===void 0?s=void 0:(s=new r(t),s._$AT(t,i,o)),o!==void 0?(i._$Co??(i._$Co=[]))[o]=s:i._$Cl=s),s!==void 0&&(e=le(t,s._$AS(t,e.values),s,o)),e}class Di{constructor(e,i){this._$AV=[],this._$AN=void 0,this._$AD=e,this._$AM=i}get parentNode(){return this._$AM.parentNode}get _$AU(){return this._$AM._$AU}u(e){const{el:{content:i},parts:o}=this._$AD,s=((e==null?void 0:e.creationScope)??oe).importNode(i,!0);ae.currentNode=s;let r=ae.nextNode(),a=0,n=0,c=o[0];for(;c!==void 0;){if(a===c.index){let m;c.type===2?m=new xe(r,r.nextSibling,this,e):c.type===1?m=new c.ctor(r,c.name,c.strings,this,e):c.type===6&&(m=new Ii(r,this,e)),this._$AV.push(m),c=o[++n]}a!==(c==null?void 0:c.index)&&(r=ae.nextNode(),a++)}return ae.currentNode=oe,s}p(e){let i=0;for(const o of this._$AV)o!==void 0&&(o.strings!==void 0?(o._$AI(e,o,i),i+=o.strings.length-2):o._$AI(e[i])),i++}}class xe{get _$AU(){var e;return((e=this._$AM)==null?void 0:e._$AU)??this._$Cv}constructor(e,i,o,s){this.type=2,this._$AH=O,this._$AN=void 0,this._$AA=e,this._$AB=i,this._$AM=o,this.options=s,this._$Cv=(s==null?void 0:s.isConnected)??!0}get parentNode(){let e=this._$AA.parentNode;const i=this._$AM;return i!==void 0&&(e==null?void 0:e.nodeType)===11&&(e=i.parentNode),e}get startNode(){return this._$AA}get endNode(){return this._$AB}_$AI(e,i=this){e=le(this,e,i),ge(e)?e===O||e==null||e===""?(this._$AH!==O&&this._$AR(),this._$AH=O):e!==this._$AH&&e!==ne&&this._(e):e._$litType$!==void 0?this.$(e):e.nodeType!==void 0?this.T(e):ki(e)?this.k(e):this._(e)}S(e){return this._$AA.parentNode.insertBefore(e,this._$AB)}T(e){this._$AH!==e&&(this._$AR(),this._$AH=this.S(e))}_(e){this._$AH!==O&&ge(this._$AH)?this._$AA.nextSibling.data=e:this.T(oe.createTextNode(e)),this._$AH=e}$(e){var r;const{values:i,_$litType$:o}=e,s=typeof o=="number"?this._$AC(e):(o.el===void 0&&(o.el=ye.createElement(Ot(o.h,o.h[0]),this.options)),o);if(((r=this._$AH)==null?void 0:r._$AD)===s)this._$AH.p(i);else{const a=new Di(s,this),n=a.u(this.options);a.p(i),this.T(n),this._$AH=a}}_$AC(e){let i=Tt.get(e.strings);return i===void 0&&Tt.set(e.strings,i=new ye(e)),i}k(e){Ct(this._$AH)||(this._$AH=[],this._$AR());const i=this._$AH;let o,s=0;for(const r of e)s===i.length?i.push(o=new xe(this.S(fe()),this.S(fe()),this,this.options)):o=i[s],o._$AI(r),s++;s<i.length&&(this._$AR(o&&o._$AB.nextSibling,s),i.length=s)}_$AR(e=this._$AA.nextSibling,i){var o;for((o=this._$AP)==null?void 0:o.call(this,!1,!0,i);e&&e!==this._$AB;){const s=e.nextSibling;e.remove(),e=s}}setConnected(e){var i;this._$AM===void 0&&(this._$Cv=e,(i=this._$AP)==null||i.call(this,e))}}class De{get tagName(){return this.element.tagName}get _$AU(){return this._$AM._$AU}constructor(e,i,o,s,r){this.type=1,this._$AH=O,this._$AN=void 0,this.element=e,this.name=i,this._$AM=s,this.options=r,o.length>2||o[0]!==""||o[1]!==""?(this._$AH=Array(o.length-1).fill(new String),this.strings=o):this._$AH=O}_$AI(e,i=this,o,s){const r=this.strings;let a=!1;if(r===void 0)e=le(this,e,i,0),a=!ge(e)||e!==this._$AH&&e!==ne,a&&(this._$AH=e);else{const n=e;let c,m;for(e=r[0],c=0;c<r.length-1;c++)m=le(this,n[o+c],i,c),m===ne&&(m=this._$AH[c]),a||(a=!ge(m)||m!==this._$AH[c]),m===O?e=O:e!==O&&(e+=(m??"")+r[c+1]),this._$AH[c]=m}a&&!s&&this.j(e)}j(e){e===O?this.element.removeAttribute(this.name):this.element.setAttribute(this.name,e??"")}}class Ei extends De{constructor(){super(...arguments),this.type=3}j(e){this.element[this.name]=e===O?void 0:e}}class Ti extends De{constructor(){super(...arguments),this.type=4}j(e){this.element.toggleAttribute(this.name,!!e&&e!==O)}}class Oi extends De{constructor(e,i,o,s,r){super(e,i,o,s,r),this.type=5}_$AI(e,i=this){if((e=le(this,e,i,0)??O)===ne)return;const o=this._$AH,s=e===O&&o!==O||e.capture!==o.capture||e.once!==o.once||e.passive!==o.passive,r=e!==O&&(o===O||s);s&&this.element.removeEventListener(this.name,this,o),r&&this.element.addEventListener(this.name,this,e),this._$AH=e}handleEvent(e){var i;typeof this._$AH=="function"?this._$AH.call(((i=this.options)==null?void 0:i.host)??this.element,e):this._$AH.handleEvent(e)}}class Ii{constructor(e,i,o){this.element=e,this.type=6,this._$AN=void 0,this._$AM=i,this.options=o}get _$AU(){return this._$AM._$AU}_$AI(e){le(this,e)}}const Ge=me.litHtmlPolyfillSupport;Ge==null||Ge(ye,xe),(me.litHtmlVersions??(me.litHtmlVersions=[])).push("3.1.2");const Fi=(t,e,i)=>{const o=(i==null?void 0:i.renderBefore)??e;let s=o._$litPart$;if(s===void 0){const r=(i==null?void 0:i.renderBefore)??null;o._$litPart$=s=new xe(e.insertBefore(fe(),r),r,void 0,i??{})}return s._$AI(t),s};/**
 * @license
 * Copyright 2017 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */class T extends re{constructor(){super(...arguments),this.renderOptions={host:this},this._$Do=void 0}createRenderRoot(){var i;const e=super.createRenderRoot();return(i=this.renderOptions).renderBefore??(i.renderBefore=e.firstChild),e}update(e){const i=this.render();this.hasUpdated||(this.renderOptions.isConnected=this.isConnected),super.update(e),this._$Do=Fi(i,this.renderRoot,this.renderOptions)}connectedCallback(){var e;super.connectedCallback(),(e=this._$Do)==null||e.setConnected(!0)}disconnectedCallback(){var e;super.disconnectedCallback(),(e=this._$Do)==null||e.setConnected(!1)}render(){return ne}}T._$litElement$=!0,T.finalized=!0,(fi=globalThis.litElementHydrateSupport)==null||fi.call(globalThis,{LitElement:T});const Qe=globalThis.litElementPolyfillSupport;Qe==null||Qe({LitElement:T}),(globalThis.litElementVersions??(globalThis.litElementVersions=[])).push("4.0.4");/**
 * @license
 * Copyright 2017 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */const R=t=>(e,i)=>{i!==void 0?i.addInitializer(()=>{customElements.define(t,e)}):customElements.define(t,e)};/**
 * @license
 * Copyright 2017 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */const _i={attribute:!0,type:String,converter:Pe,reflect:!1,hasChanged:qe},Ri=(t=_i,e,i)=>{const{kind:o,metadata:s}=i;let r=globalThis.litPropertyMetadata.get(s);if(r===void 0&&globalThis.litPropertyMetadata.set(s,r=new Map),r.set(i.name,t),o==="accessor"){const{name:a}=i;return{set(n){const c=e.get.call(this);e.set.call(this,n),this.requestUpdate(a,c,t)},init(n){return n!==void 0&&this.P(a,void 0,t),n}}}if(o==="setter"){const{name:a}=i;return function(n){const c=this[a];e.call(this,n),this.requestUpdate(a,c,t)}}throw Error("Unsupported decorator location: "+o)};function b(t){return(e,i)=>typeof i=="object"?Ri(t,e,i):((o,s,r)=>{const a=s.hasOwnProperty(r);return s.constructor.createProperty(r,a?{...o,wrapped:!0}:o),a?Object.getOwnPropertyDescriptor(s,r):void 0})(t,e,i)}/**
 * @license
 * Copyright 2017 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */function u(t){return b({...t,state:!0,attribute:!1})}/**
 * @license
 * Copyright 2017 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */const It=(t,e,i)=>(i.configurable=!0,i.enumerable=!0,Reflect.decorate&&typeof e!="object"&&Object.defineProperty(t,e,i),i);/**
 * @license
 * Copyright 2017 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */function Ee(t,e){return(i,o,s)=>{const r=a=>{var n;return((n=a.renderRoot)==null?void 0:n.querySelector(t))??null};if(e){const{get:a,set:n}=typeof o=="object"?i:s??(()=>{const c=Symbol();return{get(){return this[c]},set(m){this[c]=m}}})();return It(i,o,{get(){let c=a.call(this);return c===void 0&&(c=r(this),(c!==null||this.hasUpdated)&&n.call(this,c)),c}})}return It(i,o,{get(){return r(this)}})}}const Li=_`
  .container {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px;
    gap: 5px;

    p {
      font-weight: bold;
      margin: 0;
      font-size: 24px;
    }

    span {
      font-size: 20px;
      color: #6f6d6d;
    }
  }

  @media(max-width:768px) {
    .container {
      width: 300px;

    p {
      text-align: center;
    }
  }
  }
`;var Ni=Object.defineProperty,Mi=Object.getOwnPropertyDescriptor,zi=(t,e,i,o)=>{for(var s=o>1?void 0:o?Mi(e,i):e,r=t.length-1,a;r>=0;r--)(a=t[r])&&(s=(o?a(e,i,s):a(s))||s);return o&&s&&Ni(e,i,s),s};let Ft=class extends T{static get styles(){return[Li]}async connectedCallback(){super.connectedCallback(),await super.updateComplete}completeSvg(){return Ae`
    <svg width="40" height="40" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path fill-rule="evenodd" clip-rule="evenodd" d="M10 20C4.47667 20 0 15.5233 0 10C0 4.47667 4.47667 0 10 0C15.5233 0 20 4.47667 20 10C20 15.5233 15.5233 20 10 20Z" fill="#12B76A"/>
      <path d="M13.6108 8.33337L8.74967 13.1945L5.83301 10.2778" stroke="#F6FEF9" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
    `}render(){return h`
      <div class="container">
        ${this.completeSvg()}
        <p>Pagamento Cancelado</p>
      </div>
    `}};Ft=zi([R("message-callback")],Ft);const Ui=_`
  .clipBoard {
    position: relative;
    .trackingCode {
      max-width: 15ch;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      border: none;
      background-color: transparent;
      font-family: inherit;
      transition: background ease-in-out 70ms;
      cursor: pointer;
      &:hover {
        background-color: #c9c9c9;
        border-radius: 4px;
      }

      &::before {
        content: 'Copiado';
        position: absolute;
        top: 0px;
        right: 0;
        background-color: var(--primary-400);
        padding: 2px 10px;
        border-radius: 4px;
        font-size: 12px;
        display: none;
        color: white;
      }
    }
  }

  .clipBoard.active .trackingCode:before,
  .clipBoard.active .trackingCode:after {
    display: block;
  }
`;var Bi=Object.defineProperty,ji=Object.getOwnPropertyDescriptor,We=(t,e,i,o)=>{for(var s=o>1?void 0:o?ji(e,i):e,r=t.length-1,a;r>=0;r--)(a=t[r])&&(s=(o?a(e,i,s):a(s))||s);return o&&s&&Bi(e,i,s),s};let ve=class extends T{constructor(){super(...arguments),this.TrackingCode="",this.isActiveClipBoard=!1}copyText(){navigator.clipboard.writeText(this.TrackingCode),this.isActiveClipBoard=!0,setTimeout(()=>{this.isActiveClipBoard=!1},1e3)}render(){return h`
      <div
        @click=${this.TrackingCode!=null?this.copyText:null}
        title="Copiar"
        class="clipBoard ${this.isActiveClipBoard?"active":""}"
      >
        <button class="trackingCode">${this.TrackingCode}</button>
      </div>
    `}};ve.styles=[Ui],We([b({type:String})],ve.prototype,"TrackingCode",2),We([u()],ve.prototype,"isActiveClipBoard",2),ve=We([R("tracking-code-table")],ve);const Vi=_`
  @keyframes overlayShow {
    from {
      opacity: 0;
    }
    to {
      opacity: 1;
    }
  }

  @keyframes contentShow {
    from {
      opacity: 0;
      transform: translate(-50%, -48%) scale(0.96);
    }
    to {
      opacity: 1;
      transform: translate(-50%, -50%) scale(1);
    }
  }

  :host {
    display: flex;
  }

  .overlay {
    background: rgba(52, 64, 84, 0.7);
    backdrop-filter: blur(4px);
    position: fixed;
    inset: 0;
    animation: overlayShow 150ms cubic-bezier(0.16, 1, 0.3, 1);
    z-index: 999;
  }

  .container {
    background-color: white;
    border-radius: 4px;
    box-shadow:
      hsl(206 22% 7% / 35%) 0px 10px 38px -10px,
      hsl(206 22% 7% / 20%) 0px 10px 20px -15px;
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    /* width: 50vw; */
    max-height: 95vh;
    animation: contentShow 150ms cubic-bezier(0.16, 1, 0.3, 1);

    .headerModal {
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;

      padding: 14px 16px;
      border-radius: 4px 4px 0 0;

      > h1 {
        font-size: 24px;
        font-weight: bold;
        color: black;
        margin: 0;
      }

      > button {
        font-family: inherit;
        border-radius: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #6c757d;
        border: none;
        background-color: transparent;
        cursor: pointer;
        border-radius: 4px;
        position: absolute;
        right: 20px;

        transition: all 0.35s ease;

        &:focus {
          outline: 1px solid #fff;
        }

        &:hover {
          box-shadow: 0 0 0 2px #fff;
        }
      }
    }
    .mainModal {
      display: flex;
      flex-direction: column;
      overflow: auto;
      max-height: 90vh;
      min-height: 100%;

      @media (min-height: 680px) {
        max-height: 84vh;
      }
    }
  }
`;var qi=Object.defineProperty,Hi=Object.getOwnPropertyDescriptor,Ze=(t,e,i,o)=>{for(var s=o>1?void 0:o?Hi(e,i):e,r=t.length-1,a;r>=0;r--)(a=t[r])&&(s=(o?a(e,i,s):a(s))||s);return o&&s&&qi(e,i,s),s};let Te=class extends T{constructor(){super(...arguments),this.isCloseButton=!0}static get styles(){return[Vi]}render(){const e=h`
      <svg
        width="29"
        height="29"
        viewBox="0 0 29 29"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          d="M19.4434 8.3623L14.4932 13.3113L9.5442 8.3623L7.89453 10.012L12.8435 14.961L7.89453 19.91L9.5442 21.5596L14.4932 16.6106L19.4434 21.5596L21.093 19.91L16.144 14.961L21.093 10.012L19.4434 8.3623Z"
          fill="black"
        />
      </svg>
    `;return h`
      <div class="overlay" id="over">
        <div class=${"container lg"}>
          <div class="headerModal">
            <h1>${this.title}</h1>
            ${this.isCloseButton?h`<button @click=${this.handleOnModalCard}>
                  ${e}
                </button>`:null}
          </div>
          <div class="mainModal">
            <slot></slot>
          </div>
        </div>
      </div>
    `}handleOnModalCard(){const e=new CustomEvent("my-close-modal");this.dispatchEvent(e)}};Ze([b()],Te.prototype,"title",2),Ze([b()],Te.prototype,"isCloseButton",2),Te=Ze([R("payment-online-modal")],Te);const Gi=_`
  .completionPayment {
    display: grid;
    grid-template-columns: auto 330px;
    justify-content: space-around;
    gap: 25px;
    align-items: center;
    padding-inline: 50px;
    padding-block: 20px;
    height: 490px;

    .card {
      width: 400px;
      display: flex;
      flex-direction: column;
      border-radius: 4px;
      border: 1px solid #dfdfdf;
      max-height: 300px;
      align-items: center;

      p:nth-of-type(even) {
        text-align: right;
      }

      .header {
        background-color: #101f46;
        text-align: center;
        width: 100%;
        color: white;
      }

      .cardInfos {
        display: grid;
        grid-template-columns: repeat(1, 1fr);
        width: 100%;
        overflow-x: hidden;

        &::-webkit-scrollbar {
          width: 6px;
          height: 8px;
        }

        &::-webkit-scrollbar-track {
          background: #f1f1f1;
          border-radius: 6px;
        }

        &::-webkit-scrollbar-thumb {
          background: var(--gray-700);
          border-radius: 6px;
        }

        &::-webkit-scrollbar-thumb:hover {
          background: #555;
        }

        .padding {
          padding: 15px;

          .itemDetails {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 15px;
            margin-block: 15px;

            p {
              margin: 0;
            }
          }

          .childItems {
            .items {
              display: grid;
              margin-left: 10px;
              padding-right: 5px;
              max-height: 130px;
              grid-template-columns: repeat(2, 1fr);

              p {
                margin-block: 5px;
              }
            }
          }
        }
      }
    }

    .confirmCancel {
      padding: 20px;
      display: flex;
      flex-direction: column;
      align-items: center;

      p {
        font-size: 18px;
        text-align: center;
        margin-block: 10px;
      }

      .buttons {
        display: flex;
        gap: 20px;
        justify-content: space-around;

        button {
          background-color: #e73300;
          border-radius: 4px;
          padding: 8px 16px;
          color: white;
          font-weight: 600;
          border: none;
          cursor: pointer;
          font-family: 'Red Hat Display';
          width: 100px;
          margin-top: 5px;
          font-size: 16px;

          &:nth-of-type(1) {
            background-color: var(--success-500);
            color: white;
          }
        }
      }
    }
  }

  .badgeContent {
    position: absolute;
    bottom: 5%;
    left: 50%;
    margin-right: -50%;
    transform: translate(-50%, -50%);
    border-radius: 16px;
    background-color: var(--warning-50);
    color: var(--warning-500);
    padding: 4px 12px;
    display: flex;
    align-items: center;

    p {
      max-width: 440px;
      font-size: 14px;
      text-align: center;
      margin: 0;
    }
  }

  .contentLoading {
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 20px 50px;
  }

  .cancelButtonDiv {
    margin-top: 35px;
    display: flex;
    justify-content: center;

  }
  .button {
    width: 200px;
  }

  .qrCodeImage {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 10px;
    margin-bottom: 20px;

    textarea {
      width: 320px;
      resize: none;
      border-radius: 4px;
      border: 1px solid #dfdfdf;
      font-family: 'Red Hat Display', sans-serif !important;
      cursor: pointer;
    }

    img {
      height: 300px;
      width: 302px;
      border: 1px solid #dfdfdf;
      border-radius: 4px;
    }

    .imgPix {
      position: relative;

      .svgCanceled {
        border-radius: 30px;
        background-color: #ffebe6;
        position: absolute;
        top: 50%;
        left: 50%;
        margin-right: -50%;
        transform: translate(-50%, -50%);
        padding: 5px;
        display: flex;
        align-items: center;
      }

      .svgCheck {
        position: absolute;
        top: 50%;
        left: 50%;
        margin-right: -50%;
        transform: translate(-50%, -50%);
        display: flex;
        padding: 10px;
        align-items: center;
        border-radius: 30px;
        background-color: #d9ffed;
      }
    }
  }

  .pix {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 10px;
  }

  .copied-message {
    position: fixed;
    top: 20px;
    left: 50%;
    transform: translateX(-50%);
    background-color: #4caf50;
    color: white;
    padding: 15px;
    border-radius: 5px;
    font-size: 16px;
    z-index: 9999;
    display: none;
  }

  .skeletons {
    display: flex;
    gap: 60px;
    width: 100%;
    margin-bottom: 10px;
  }

  .skeleton {
    animation: skeleton-loading 1s linear infinite alternate;
  }

  .skeletonChildWidth {
    padding: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 800px;
  }

  .skeletonSize {
    width: 40%;
    height: 400px;
  }

  .spinner {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 400px;
    height: 400px;
  }

  @keyframes skeleton-loading {
    0% {
      background-color: hsl(200, 20%, 80%);
    }
    100% {
      background-color: hsl(200, 20%, 95%);
    }
  }

  @media (max-width: 768px) {
    .completionPayment {
      display: flex;
      flex-direction: column;
      height: max-content;
      gap: 0;
      padding-inline: 10px;
      height: max-content;

      .card {
        width: 330px;
      }
    }

    .badgeContent {
      display: none;
    }

    .skeletons {
      gap: 30px;
      flex-direction: column;
    }

    .pix {
      margin-top: 10px;
  }

    .cancelButtonDiv {
    margin-top: 15px;
  }

    .skeletonChildWidth {
      padding: 5px;
      display: flex;
      align-items: center;
      justify-content: center;
      width: 95vw;
    }

    .skeletonSize {
      width: 70%;
      height: 260px;
    }
  }
`;function _t(t,e){return function(){return t.apply(e,arguments)}}const{toString:Qi}=Object.prototype,{getPrototypeOf:Ye}=Object,Oe=(t=>e=>{const i=Qi.call(e);return t[i]||(t[i]=i.slice(8,-1).toLowerCase())})(Object.create(null)),B=t=>(t=t.toLowerCase(),e=>Oe(e)===t),Ie=t=>e=>typeof e===t,{isArray:de}=Array,we=Ie("undefined");function Wi(t){return t!==null&&!we(t)&&t.constructor!==null&&!we(t.constructor)&&M(t.constructor.isBuffer)&&t.constructor.isBuffer(t)}const Rt=B("ArrayBuffer");function Zi(t){let e;return typeof ArrayBuffer<"u"&&ArrayBuffer.isView?e=ArrayBuffer.isView(t):e=t&&t.buffer&&Rt(t.buffer),e}const Yi=Ie("string"),M=Ie("function"),Lt=Ie("number"),Fe=t=>t!==null&&typeof t=="object",Ji=t=>t===!0||t===!1,_e=t=>{if(Oe(t)!=="object")return!1;const e=Ye(t);return(e===null||e===Object.prototype||Object.getPrototypeOf(e)===null)&&!(Symbol.toStringTag in t)&&!(Symbol.iterator in t)},Ki=B("Date"),Xi=B("File"),eo=B("Blob"),to=B("FileList"),io=t=>Fe(t)&&M(t.pipe),oo=t=>{let e;return t&&(typeof FormData=="function"&&t instanceof FormData||M(t.append)&&((e=Oe(t))==="formdata"||e==="object"&&M(t.toString)&&t.toString()==="[object FormData]"))},so=B("URLSearchParams"),ao=t=>t.trim?t.trim():t.replace(/^[\s\uFEFF\xA0]+|[\s\uFEFF\xA0]+$/g,"");function $e(t,e,{allOwnKeys:i=!1}={}){if(t===null||typeof t>"u")return;let o,s;if(typeof t!="object"&&(t=[t]),de(t))for(o=0,s=t.length;o<s;o++)e.call(null,t[o],o,t);else{const r=i?Object.getOwnPropertyNames(t):Object.keys(t),a=r.length;let n;for(o=0;o<a;o++)n=r[o],e.call(null,t[n],n,t)}}function Nt(t,e){e=e.toLowerCase();const i=Object.keys(t);let o=i.length,s;for(;o-- >0;)if(s=i[o],e===s.toLowerCase())return s;return null}const Mt=typeof globalThis<"u"?globalThis:typeof self<"u"?self:typeof window<"u"?window:global,zt=t=>!we(t)&&t!==Mt;function Je(){const{caseless:t}=zt(this)&&this||{},e={},i=(o,s)=>{const r=t&&Nt(e,s)||s;_e(e[r])&&_e(o)?e[r]=Je(e[r],o):_e(o)?e[r]=Je({},o):de(o)?e[r]=o.slice():e[r]=o};for(let o=0,s=arguments.length;o<s;o++)arguments[o]&&$e(arguments[o],i);return e}const ro=(t,e,i,{allOwnKeys:o}={})=>($e(e,(s,r)=>{i&&M(s)?t[r]=_t(s,i):t[r]=s},{allOwnKeys:o}),t),no=t=>(t.charCodeAt(0)===65279&&(t=t.slice(1)),t),lo=(t,e,i,o)=>{t.prototype=Object.create(e.prototype,o),t.prototype.constructor=t,Object.defineProperty(t,"super",{value:e.prototype}),i&&Object.assign(t.prototype,i)},co=(t,e,i,o)=>{let s,r,a;const n={};if(e=e||{},t==null)return e;do{for(s=Object.getOwnPropertyNames(t),r=s.length;r-- >0;)a=s[r],(!o||o(a,t,e))&&!n[a]&&(e[a]=t[a],n[a]=!0);t=i!==!1&&Ye(t)}while(t&&(!i||i(t,e))&&t!==Object.prototype);return e},po=(t,e,i)=>{t=String(t),(i===void 0||i>t.length)&&(i=t.length),i-=e.length;const o=t.indexOf(e,i);return o!==-1&&o===i},ho=t=>{if(!t)return null;if(de(t))return t;let e=t.length;if(!Lt(e))return null;const i=new Array(e);for(;e-- >0;)i[e]=t[e];return i},uo=(t=>e=>t&&e instanceof t)(typeof Uint8Array<"u"&&Ye(Uint8Array)),mo=(t,e)=>{const o=(t&&t[Symbol.iterator]).call(t);let s;for(;(s=o.next())&&!s.done;){const r=s.value;e.call(t,r[0],r[1])}},fo=(t,e)=>{let i;const o=[];for(;(i=t.exec(e))!==null;)o.push(i);return o},go=B("HTMLFormElement"),bo=t=>t.toLowerCase().replace(/[-_\s]([a-z\d])(\w*)/g,function(i,o,s){return o.toUpperCase()+s}),Ut=(({hasOwnProperty:t})=>(e,i)=>t.call(e,i))(Object.prototype),yo=B("RegExp"),Bt=(t,e)=>{const i=Object.getOwnPropertyDescriptors(t),o={};$e(i,(s,r)=>{let a;(a=e(s,r,t))!==!1&&(o[r]=a||s)}),Object.defineProperties(t,o)},xo=t=>{Bt(t,(e,i)=>{if(M(t)&&["arguments","caller","callee"].indexOf(i)!==-1)return!1;const o=t[i];if(M(o)){if(e.enumerable=!1,"writable"in e){e.writable=!1;return}e.set||(e.set=()=>{throw Error("Can not rewrite read-only method '"+i+"'")})}})},vo=(t,e)=>{const i={},o=s=>{s.forEach(r=>{i[r]=!0})};return de(t)?o(t):o(String(t).split(e)),i},wo=()=>{},$o=(t,e)=>(t=+t,Number.isFinite(t)?t:e),Ke="abcdefghijklmnopqrstuvwxyz",jt="0123456789",Vt={DIGIT:jt,ALPHA:Ke,ALPHA_DIGIT:Ke+Ke.toUpperCase()+jt},Co=(t=16,e=Vt.ALPHA_DIGIT)=>{let i="";const{length:o}=e;for(;t--;)i+=e[Math.random()*o|0];return i};function So(t){return!!(t&&M(t.append)&&t[Symbol.toStringTag]==="FormData"&&t[Symbol.iterator])}const Po=t=>{const e=new Array(10),i=(o,s)=>{if(Fe(o)){if(e.indexOf(o)>=0)return;if(!("toJSON"in o)){e[s]=o;const r=de(o)?[]:{};return $e(o,(a,n)=>{const c=i(a,s+1);!we(c)&&(r[n]=c)}),e[s]=void 0,r}}return o};return i(t,0)},ko=B("AsyncFunction"),d={isArray:de,isArrayBuffer:Rt,isBuffer:Wi,isFormData:oo,isArrayBufferView:Zi,isString:Yi,isNumber:Lt,isBoolean:Ji,isObject:Fe,isPlainObject:_e,isUndefined:we,isDate:Ki,isFile:Xi,isBlob:eo,isRegExp:yo,isFunction:M,isStream:io,isURLSearchParams:so,isTypedArray:uo,isFileList:to,forEach:$e,merge:Je,extend:ro,trim:ao,stripBOM:no,inherits:lo,toFlatObject:co,kindOf:Oe,kindOfTest:B,endsWith:po,toArray:ho,forEachEntry:mo,matchAll:fo,isHTMLForm:go,hasOwnProperty:Ut,hasOwnProp:Ut,reduceDescriptors:Bt,freezeMethods:xo,toObjectSet:vo,toCamelCase:bo,noop:wo,toFiniteNumber:$o,findKey:Nt,global:Mt,isContextDefined:zt,ALPHABET:Vt,generateString:Co,isSpecCompliantForm:So,toJSONObject:Po,isAsyncFn:ko,isThenable:t=>t&&(Fe(t)||M(t))&&M(t.then)&&M(t.catch)};function y(t,e,i,o,s){Error.call(this),Error.captureStackTrace?Error.captureStackTrace(this,this.constructor):this.stack=new Error().stack,this.message=t,this.name="AxiosError",e&&(this.code=e),i&&(this.config=i),o&&(this.request=o),s&&(this.response=s)}d.inherits(y,Error,{toJSON:function(){return{message:this.message,name:this.name,description:this.description,number:this.number,fileName:this.fileName,lineNumber:this.lineNumber,columnNumber:this.columnNumber,stack:this.stack,config:d.toJSONObject(this.config),code:this.code,status:this.response&&this.response.status?this.response.status:null}}});const qt=y.prototype,Ht={};["ERR_BAD_OPTION_VALUE","ERR_BAD_OPTION","ECONNABORTED","ETIMEDOUT","ERR_NETWORK","ERR_FR_TOO_MANY_REDIRECTS","ERR_DEPRECATED","ERR_BAD_RESPONSE","ERR_BAD_REQUEST","ERR_CANCELED","ERR_NOT_SUPPORT","ERR_INVALID_URL"].forEach(t=>{Ht[t]={value:t}}),Object.defineProperties(y,Ht),Object.defineProperty(qt,"isAxiosError",{value:!0}),y.from=(t,e,i,o,s,r)=>{const a=Object.create(qt);return d.toFlatObject(t,a,function(c){return c!==Error.prototype},n=>n!=="isAxiosError"),y.call(a,t.message,e,i,o,s),a.cause=t,a.name=t.name,r&&Object.assign(a,r),a};const Ao=null;function Xe(t){return d.isPlainObject(t)||d.isArray(t)}function Gt(t){return d.endsWith(t,"[]")?t.slice(0,-2):t}function Qt(t,e,i){return t?t.concat(e).map(function(s,r){return s=Gt(s),!i&&r?"["+s+"]":s}).join(i?".":""):e}function Do(t){return d.isArray(t)&&!t.some(Xe)}const Eo=d.toFlatObject(d,{},null,function(e){return/^is[A-Z]/.test(e)});function Re(t,e,i){if(!d.isObject(t))throw new TypeError("target must be an object");e=e||new FormData,i=d.toFlatObject(i,{metaTokens:!0,dots:!1,indexes:!1},!1,function(g,F){return!d.isUndefined(F[g])});const o=i.metaTokens,s=i.visitor||p,r=i.dots,a=i.indexes,c=(i.Blob||typeof Blob<"u"&&Blob)&&d.isSpecCompliantForm(e);if(!d.isFunction(s))throw new TypeError("visitor must be a function");function m(f){if(f===null)return"";if(d.isDate(f))return f.toISOString();if(!c&&d.isBlob(f))throw new y("Blob is not supported. Use a Buffer instead.");return d.isArrayBuffer(f)||d.isTypedArray(f)?c&&typeof Blob=="function"?new Blob([f]):Buffer.from(f):f}function p(f,g,F){let N=f;if(f&&!F&&typeof f=="object"){if(d.endsWith(g,"{}"))g=o?g:g.slice(0,-2),f=JSON.stringify(f);else if(d.isArray(f)&&Do(f)||(d.isFileList(f)||d.endsWith(g,"[]"))&&(N=d.toArray(f)))return g=Gt(g),N.forEach(function(te,Bs){!(d.isUndefined(te)||te===null)&&e.append(a===!0?Qt([g],Bs,r):a===null?g:g+"[]",m(te))}),!1}return Xe(f)?!0:(e.append(Qt(F,g,r),m(f)),!1)}const l=[],v=Object.assign(Eo,{defaultVisitor:p,convertValue:m,isVisitable:Xe});function E(f,g){if(!d.isUndefined(f)){if(l.indexOf(f)!==-1)throw Error("Circular reference detected in "+g.join("."));l.push(f),d.forEach(f,function(N,ee){(!(d.isUndefined(N)||N===null)&&s.call(e,N,d.isString(ee)?ee.trim():ee,g,v))===!0&&E(N,g?g.concat(ee):[ee])}),l.pop()}}if(!d.isObject(t))throw new TypeError("data must be an object");return E(t),e}function Wt(t){const e={"!":"%21","'":"%27","(":"%28",")":"%29","~":"%7E","%20":"+","%00":"\0"};return encodeURIComponent(t).replace(/[!'()~]|%20|%00/g,function(o){return e[o]})}function et(t,e){this._pairs=[],t&&Re(t,this,e)}const Zt=et.prototype;Zt.append=function(e,i){this._pairs.push([e,i])},Zt.toString=function(e){const i=e?function(o){return e.call(this,o,Wt)}:Wt;return this._pairs.map(function(s){return i(s[0])+"="+i(s[1])},"").join("&")};function To(t){return encodeURIComponent(t).replace(/%3A/gi,":").replace(/%24/g,"$").replace(/%2C/gi,",").replace(/%20/g,"+").replace(/%5B/gi,"[").replace(/%5D/gi,"]")}function Yt(t,e,i){if(!e)return t;const o=i&&i.encode||To,s=i&&i.serialize;let r;if(s?r=s(e,i):r=d.isURLSearchParams(e)?e.toString():new et(e,i).toString(o),r){const a=t.indexOf("#");a!==-1&&(t=t.slice(0,a)),t+=(t.indexOf("?")===-1?"?":"&")+r}return t}class Jt{constructor(){this.handlers=[]}use(e,i,o){return this.handlers.push({fulfilled:e,rejected:i,synchronous:o?o.synchronous:!1,runWhen:o?o.runWhen:null}),this.handlers.length-1}eject(e){this.handlers[e]&&(this.handlers[e]=null)}clear(){this.handlers&&(this.handlers=[])}forEach(e){d.forEach(this.handlers,function(o){o!==null&&e(o)})}}const Kt={silentJSONParsing:!0,forcedJSONParsing:!0,clarifyTimeoutError:!1},Oo={isBrowser:!0,classes:{URLSearchParams:typeof URLSearchParams<"u"?URLSearchParams:et,FormData:typeof FormData<"u"?FormData:null,Blob:typeof Blob<"u"?Blob:null},protocols:["http","https","file","blob","url","data"]},Xt=typeof window<"u"&&typeof document<"u",Io=(t=>Xt&&["ReactNative","NativeScript","NS"].indexOf(t)<0)(typeof navigator<"u"&&navigator.product),Fo=typeof WorkerGlobalScope<"u"&&self instanceof WorkerGlobalScope&&typeof self.importScripts=="function",j={...Object.freeze(Object.defineProperty({__proto__:null,hasBrowserEnv:Xt,hasStandardBrowserEnv:Io,hasStandardBrowserWebWorkerEnv:Fo},Symbol.toStringTag,{value:"Module"})),...Oo};function _o(t,e){return Re(t,new j.classes.URLSearchParams,Object.assign({visitor:function(i,o,s,r){return j.isNode&&d.isBuffer(i)?(this.append(o,i.toString("base64")),!1):r.defaultVisitor.apply(this,arguments)}},e))}function Ro(t){return d.matchAll(/\w+|\[(\w*)]/g,t).map(e=>e[0]==="[]"?"":e[1]||e[0])}function Lo(t){const e={},i=Object.keys(t);let o;const s=i.length;let r;for(o=0;o<s;o++)r=i[o],e[r]=t[r];return e}function ei(t){function e(i,o,s,r){let a=i[r++];if(a==="__proto__")return!0;const n=Number.isFinite(+a),c=r>=i.length;return a=!a&&d.isArray(s)?s.length:a,c?(d.hasOwnProp(s,a)?s[a]=[s[a],o]:s[a]=o,!n):((!s[a]||!d.isObject(s[a]))&&(s[a]=[]),e(i,o,s[a],r)&&d.isArray(s[a])&&(s[a]=Lo(s[a])),!n)}if(d.isFormData(t)&&d.isFunction(t.entries)){const i={};return d.forEachEntry(t,(o,s)=>{e(Ro(o),s,i,0)}),i}return null}function No(t,e,i){if(d.isString(t))try{return(e||JSON.parse)(t),d.trim(t)}catch(o){if(o.name!=="SyntaxError")throw o}return(i||JSON.stringify)(t)}const tt={transitional:Kt,adapter:["xhr","http"],transformRequest:[function(e,i){const o=i.getContentType()||"",s=o.indexOf("application/json")>-1,r=d.isObject(e);if(r&&d.isHTMLForm(e)&&(e=new FormData(e)),d.isFormData(e))return s?JSON.stringify(ei(e)):e;if(d.isArrayBuffer(e)||d.isBuffer(e)||d.isStream(e)||d.isFile(e)||d.isBlob(e))return e;if(d.isArrayBufferView(e))return e.buffer;if(d.isURLSearchParams(e))return i.setContentType("application/x-www-form-urlencoded;charset=utf-8",!1),e.toString();let n;if(r){if(o.indexOf("application/x-www-form-urlencoded")>-1)return _o(e,this.formSerializer).toString();if((n=d.isFileList(e))||o.indexOf("multipart/form-data")>-1){const c=this.env&&this.env.FormData;return Re(n?{"files[]":e}:e,c&&new c,this.formSerializer)}}return r||s?(i.setContentType("application/json",!1),No(e)):e}],transformResponse:[function(e){const i=this.transitional||tt.transitional,o=i&&i.forcedJSONParsing,s=this.responseType==="json";if(e&&d.isString(e)&&(o&&!this.responseType||s)){const a=!(i&&i.silentJSONParsing)&&s;try{return JSON.parse(e)}catch(n){if(a)throw n.name==="SyntaxError"?y.from(n,y.ERR_BAD_RESPONSE,this,null,this.response):n}}return e}],timeout:0,xsrfCookieName:"XSRF-TOKEN",xsrfHeaderName:"X-XSRF-TOKEN",maxContentLength:-1,maxBodyLength:-1,env:{FormData:j.classes.FormData,Blob:j.classes.Blob},validateStatus:function(e){return e>=200&&e<300},headers:{common:{Accept:"application/json, text/plain, */*","Content-Type":void 0}}};d.forEach(["delete","get","head","post","put","patch"],t=>{tt.headers[t]={}});const it=tt,Mo=d.toObjectSet(["age","authorization","content-length","content-type","etag","expires","from","host","if-modified-since","if-unmodified-since","last-modified","location","max-forwards","proxy-authorization","referer","retry-after","user-agent"]),zo=t=>{const e={};let i,o,s;return t&&t.split(`
`).forEach(function(a){s=a.indexOf(":"),i=a.substring(0,s).trim().toLowerCase(),o=a.substring(s+1).trim(),!(!i||e[i]&&Mo[i])&&(i==="set-cookie"?e[i]?e[i].push(o):e[i]=[o]:e[i]=e[i]?e[i]+", "+o:o)}),e},ti=Symbol("internals");function Ce(t){return t&&String(t).trim().toLowerCase()}function Le(t){return t===!1||t==null?t:d.isArray(t)?t.map(Le):String(t)}function Uo(t){const e=Object.create(null),i=/([^\s,;=]+)\s*(?:=\s*([^,;]+))?/g;let o;for(;o=i.exec(t);)e[o[1]]=o[2];return e}const Bo=t=>/^[-_a-zA-Z0-9^`|~,!#$%&'*+.]+$/.test(t.trim());function ot(t,e,i,o,s){if(d.isFunction(o))return o.call(this,e,i);if(s&&(e=i),!!d.isString(e)){if(d.isString(o))return e.indexOf(o)!==-1;if(d.isRegExp(o))return o.test(e)}}function jo(t){return t.trim().toLowerCase().replace(/([a-z\d])(\w*)/g,(e,i,o)=>i.toUpperCase()+o)}function Vo(t,e){const i=d.toCamelCase(" "+e);["get","set","has"].forEach(o=>{Object.defineProperty(t,o+i,{value:function(s,r,a){return this[o].call(this,e,s,r,a)},configurable:!0})})}class Ne{constructor(e){e&&this.set(e)}set(e,i,o){const s=this;function r(n,c,m){const p=Ce(c);if(!p)throw new Error("header name must be a non-empty string");const l=d.findKey(s,p);(!l||s[l]===void 0||m===!0||m===void 0&&s[l]!==!1)&&(s[l||c]=Le(n))}const a=(n,c)=>d.forEach(n,(m,p)=>r(m,p,c));return d.isPlainObject(e)||e instanceof this.constructor?a(e,i):d.isString(e)&&(e=e.trim())&&!Bo(e)?a(zo(e),i):e!=null&&r(i,e,o),this}get(e,i){if(e=Ce(e),e){const o=d.findKey(this,e);if(o){const s=this[o];if(!i)return s;if(i===!0)return Uo(s);if(d.isFunction(i))return i.call(this,s,o);if(d.isRegExp(i))return i.exec(s);throw new TypeError("parser must be boolean|regexp|function")}}}has(e,i){if(e=Ce(e),e){const o=d.findKey(this,e);return!!(o&&this[o]!==void 0&&(!i||ot(this,this[o],o,i)))}return!1}delete(e,i){const o=this;let s=!1;function r(a){if(a=Ce(a),a){const n=d.findKey(o,a);n&&(!i||ot(o,o[n],n,i))&&(delete o[n],s=!0)}}return d.isArray(e)?e.forEach(r):r(e),s}clear(e){const i=Object.keys(this);let o=i.length,s=!1;for(;o--;){const r=i[o];(!e||ot(this,this[r],r,e,!0))&&(delete this[r],s=!0)}return s}normalize(e){const i=this,o={};return d.forEach(this,(s,r)=>{const a=d.findKey(o,r);if(a){i[a]=Le(s),delete i[r];return}const n=e?jo(r):String(r).trim();n!==r&&delete i[r],i[n]=Le(s),o[n]=!0}),this}concat(...e){return this.constructor.concat(this,...e)}toJSON(e){const i=Object.create(null);return d.forEach(this,(o,s)=>{o!=null&&o!==!1&&(i[s]=e&&d.isArray(o)?o.join(", "):o)}),i}[Symbol.iterator](){return Object.entries(this.toJSON())[Symbol.iterator]()}toString(){return Object.entries(this.toJSON()).map(([e,i])=>e+": "+i).join(`
`)}get[Symbol.toStringTag](){return"AxiosHeaders"}static from(e){return e instanceof this?e:new this(e)}static concat(e,...i){const o=new this(e);return i.forEach(s=>o.set(s)),o}static accessor(e){const o=(this[ti]=this[ti]={accessors:{}}).accessors,s=this.prototype;function r(a){const n=Ce(a);o[n]||(Vo(s,a),o[n]=!0)}return d.isArray(e)?e.forEach(r):r(e),this}}Ne.accessor(["Content-Type","Content-Length","Accept","Accept-Encoding","User-Agent","Authorization"]),d.reduceDescriptors(Ne.prototype,({value:t},e)=>{let i=e[0].toUpperCase()+e.slice(1);return{get:()=>t,set(o){this[i]=o}}}),d.freezeMethods(Ne);const G=Ne;function st(t,e){const i=this||it,o=e||i,s=G.from(o.headers);let r=o.data;return d.forEach(t,function(n){r=n.call(i,r,s.normalize(),e?e.status:void 0)}),s.normalize(),r}function ii(t){return!!(t&&t.__CANCEL__)}function Se(t,e,i){y.call(this,t??"canceled",y.ERR_CANCELED,e,i),this.name="CanceledError"}d.inherits(Se,y,{__CANCEL__:!0});function qo(t,e,i){const o=i.config.validateStatus;!i.status||!o||o(i.status)?t(i):e(new y("Request failed with status code "+i.status,[y.ERR_BAD_REQUEST,y.ERR_BAD_RESPONSE][Math.floor(i.status/100)-4],i.config,i.request,i))}const Ho=j.hasStandardBrowserEnv?{write(t,e,i,o,s,r){const a=[t+"="+encodeURIComponent(e)];d.isNumber(i)&&a.push("expires="+new Date(i).toGMTString()),d.isString(o)&&a.push("path="+o),d.isString(s)&&a.push("domain="+s),r===!0&&a.push("secure"),document.cookie=a.join("; ")},read(t){const e=document.cookie.match(new RegExp("(^|;\\s*)("+t+")=([^;]*)"));return e?decodeURIComponent(e[3]):null},remove(t){this.write(t,"",Date.now()-864e5)}}:{write(){},read(){return null},remove(){}};function Go(t){return/^([a-z][a-z\d+\-.]*:)?\/\//i.test(t)}function Qo(t,e){return e?t.replace(/\/?\/$/,"")+"/"+e.replace(/^\/+/,""):t}function oi(t,e){return t&&!Go(e)?Qo(t,e):e}const Wo=j.hasStandardBrowserEnv?function(){const e=/(msie|trident)/i.test(navigator.userAgent),i=document.createElement("a");let o;function s(r){let a=r;return e&&(i.setAttribute("href",a),a=i.href),i.setAttribute("href",a),{href:i.href,protocol:i.protocol?i.protocol.replace(/:$/,""):"",host:i.host,search:i.search?i.search.replace(/^\?/,""):"",hash:i.hash?i.hash.replace(/^#/,""):"",hostname:i.hostname,port:i.port,pathname:i.pathname.charAt(0)==="/"?i.pathname:"/"+i.pathname}}return o=s(window.location.href),function(a){const n=d.isString(a)?s(a):a;return n.protocol===o.protocol&&n.host===o.host}}():function(){return function(){return!0}}();function Zo(t){const e=/^([-+\w]{1,25})(:?\/\/|:)/.exec(t);return e&&e[1]||""}function Yo(t,e){t=t||10;const i=new Array(t),o=new Array(t);let s=0,r=0,a;return e=e!==void 0?e:1e3,function(c){const m=Date.now(),p=o[r];a||(a=m),i[s]=c,o[s]=m;let l=r,v=0;for(;l!==s;)v+=i[l++],l=l%t;if(s=(s+1)%t,s===r&&(r=(r+1)%t),m-a<e)return;const E=p&&m-p;return E?Math.round(v*1e3/E):void 0}}function si(t,e){let i=0;const o=Yo(50,250);return s=>{const r=s.loaded,a=s.lengthComputable?s.total:void 0,n=r-i,c=o(n),m=r<=a;i=r;const p={loaded:r,total:a,progress:a?r/a:void 0,bytes:n,rate:c||void 0,estimated:c&&a&&m?(a-r)/c:void 0,event:s};p[e?"download":"upload"]=!0,t(p)}}const at={http:Ao,xhr:typeof XMLHttpRequest<"u"&&function(t){return new Promise(function(i,o){let s=t.data;const r=G.from(t.headers).normalize();let{responseType:a,withXSRFToken:n}=t,c;function m(){t.cancelToken&&t.cancelToken.unsubscribe(c),t.signal&&t.signal.removeEventListener("abort",c)}let p;if(d.isFormData(s)){if(j.hasStandardBrowserEnv||j.hasStandardBrowserWebWorkerEnv)r.setContentType(!1);else if((p=r.getContentType())!==!1){const[g,...F]=p?p.split(";").map(N=>N.trim()).filter(Boolean):[];r.setContentType([g||"multipart/form-data",...F].join("; "))}}let l=new XMLHttpRequest;if(t.auth){const g=t.auth.username||"",F=t.auth.password?unescape(encodeURIComponent(t.auth.password)):"";r.set("Authorization","Basic "+btoa(g+":"+F))}const v=oi(t.baseURL,t.url);l.open(t.method.toUpperCase(),Yt(v,t.params,t.paramsSerializer),!0),l.timeout=t.timeout;function E(){if(!l)return;const g=G.from("getAllResponseHeaders"in l&&l.getAllResponseHeaders()),N={data:!a||a==="text"||a==="json"?l.responseText:l.response,status:l.status,statusText:l.statusText,headers:g,config:t,request:l};qo(function(te){i(te),m()},function(te){o(te),m()},N),l=null}if("onloadend"in l?l.onloadend=E:l.onreadystatechange=function(){!l||l.readyState!==4||l.status===0&&!(l.responseURL&&l.responseURL.indexOf("file:")===0)||setTimeout(E)},l.onabort=function(){l&&(o(new y("Request aborted",y.ECONNABORTED,t,l)),l=null)},l.onerror=function(){o(new y("Network Error",y.ERR_NETWORK,t,l)),l=null},l.ontimeout=function(){let F=t.timeout?"timeout of "+t.timeout+"ms exceeded":"timeout exceeded";const N=t.transitional||Kt;t.timeoutErrorMessage&&(F=t.timeoutErrorMessage),o(new y(F,N.clarifyTimeoutError?y.ETIMEDOUT:y.ECONNABORTED,t,l)),l=null},j.hasStandardBrowserEnv&&(n&&d.isFunction(n)&&(n=n(t)),n||n!==!1&&Wo(v))){const g=t.xsrfHeaderName&&t.xsrfCookieName&&Ho.read(t.xsrfCookieName);g&&r.set(t.xsrfHeaderName,g)}s===void 0&&r.setContentType(null),"setRequestHeader"in l&&d.forEach(r.toJSON(),function(F,N){l.setRequestHeader(N,F)}),d.isUndefined(t.withCredentials)||(l.withCredentials=!!t.withCredentials),a&&a!=="json"&&(l.responseType=t.responseType),typeof t.onDownloadProgress=="function"&&l.addEventListener("progress",si(t.onDownloadProgress,!0)),typeof t.onUploadProgress=="function"&&l.upload&&l.upload.addEventListener("progress",si(t.onUploadProgress)),(t.cancelToken||t.signal)&&(c=g=>{l&&(o(!g||g.type?new Se(null,t,l):g),l.abort(),l=null)},t.cancelToken&&t.cancelToken.subscribe(c),t.signal&&(t.signal.aborted?c():t.signal.addEventListener("abort",c)));const f=Zo(v);if(f&&j.protocols.indexOf(f)===-1){o(new y("Unsupported protocol "+f+":",y.ERR_BAD_REQUEST,t));return}l.send(s||null)})}};d.forEach(at,(t,e)=>{if(t){try{Object.defineProperty(t,"name",{value:e})}catch{}Object.defineProperty(t,"adapterName",{value:e})}});const ai=t=>`- ${t}`,Jo=t=>d.isFunction(t)||t===null||t===!1,ri={getAdapter:t=>{t=d.isArray(t)?t:[t];const{length:e}=t;let i,o;const s={};for(let r=0;r<e;r++){i=t[r];let a;if(o=i,!Jo(i)&&(o=at[(a=String(i)).toLowerCase()],o===void 0))throw new y(`Unknown adapter '${a}'`);if(o)break;s[a||"#"+r]=o}if(!o){const r=Object.entries(s).map(([n,c])=>`adapter ${n} `+(c===!1?"is not supported by the environment":"is not available in the build"));let a=e?r.length>1?`since :
`+r.map(ai).join(`
`):" "+ai(r[0]):"as no adapter specified";throw new y("There is no suitable adapter to dispatch the request "+a,"ERR_NOT_SUPPORT")}return o},adapters:at};function rt(t){if(t.cancelToken&&t.cancelToken.throwIfRequested(),t.signal&&t.signal.aborted)throw new Se(null,t)}function ni(t){return rt(t),t.headers=G.from(t.headers),t.data=st.call(t,t.transformRequest),["post","put","patch"].indexOf(t.method)!==-1&&t.headers.setContentType("application/x-www-form-urlencoded",!1),ri.getAdapter(t.adapter||it.adapter)(t).then(function(o){return rt(t),o.data=st.call(t,t.transformResponse,o),o.headers=G.from(o.headers),o},function(o){return ii(o)||(rt(t),o&&o.response&&(o.response.data=st.call(t,t.transformResponse,o.response),o.response.headers=G.from(o.response.headers))),Promise.reject(o)})}const li=t=>t instanceof G?{...t}:t;function ce(t,e){e=e||{};const i={};function o(m,p,l){return d.isPlainObject(m)&&d.isPlainObject(p)?d.merge.call({caseless:l},m,p):d.isPlainObject(p)?d.merge({},p):d.isArray(p)?p.slice():p}function s(m,p,l){if(d.isUndefined(p)){if(!d.isUndefined(m))return o(void 0,m,l)}else return o(m,p,l)}function r(m,p){if(!d.isUndefined(p))return o(void 0,p)}function a(m,p){if(d.isUndefined(p)){if(!d.isUndefined(m))return o(void 0,m)}else return o(void 0,p)}function n(m,p,l){if(l in e)return o(m,p);if(l in t)return o(void 0,m)}const c={url:r,method:r,data:r,baseURL:a,transformRequest:a,transformResponse:a,paramsSerializer:a,timeout:a,timeoutMessage:a,withCredentials:a,withXSRFToken:a,adapter:a,responseType:a,xsrfCookieName:a,xsrfHeaderName:a,onUploadProgress:a,onDownloadProgress:a,decompress:a,maxContentLength:a,maxBodyLength:a,beforeRedirect:a,transport:a,httpAgent:a,httpsAgent:a,cancelToken:a,socketPath:a,responseEncoding:a,validateStatus:n,headers:(m,p)=>s(li(m),li(p),!0)};return d.forEach(Object.keys(Object.assign({},t,e)),function(p){const l=c[p]||s,v=l(t[p],e[p],p);d.isUndefined(v)&&l!==n||(i[p]=v)}),i}const di="1.6.8",nt={};["object","boolean","number","function","string","symbol"].forEach((t,e)=>{nt[t]=function(o){return typeof o===t||"a"+(e<1?"n ":" ")+t}});const ci={};nt.transitional=function(e,i,o){function s(r,a){return"[Axios v"+di+"] Transitional option '"+r+"'"+a+(o?". "+o:"")}return(r,a,n)=>{if(e===!1)throw new y(s(a," has been removed"+(i?" in "+i:"")),y.ERR_DEPRECATED);return i&&!ci[a]&&(ci[a]=!0,console.warn(s(a," has been deprecated since v"+i+" and will be removed in the near future"))),e?e(r,a,n):!0}};function Ko(t,e,i){if(typeof t!="object")throw new y("options must be an object",y.ERR_BAD_OPTION_VALUE);const o=Object.keys(t);let s=o.length;for(;s-- >0;){const r=o[s],a=e[r];if(a){const n=t[r],c=n===void 0||a(n,r,t);if(c!==!0)throw new y("option "+r+" must be "+c,y.ERR_BAD_OPTION_VALUE);continue}if(i!==!0)throw new y("Unknown option "+r,y.ERR_BAD_OPTION)}}const lt={assertOptions:Ko,validators:nt},J=lt.validators;class Me{constructor(e){this.defaults=e,this.interceptors={request:new Jt,response:new Jt}}async request(e,i){try{return await this._request(e,i)}catch(o){if(o instanceof Error){let s;Error.captureStackTrace?Error.captureStackTrace(s={}):s=new Error;const r=s.stack?s.stack.replace(/^.+\n/,""):"";o.stack?r&&!String(o.stack).endsWith(r.replace(/^.+\n.+\n/,""))&&(o.stack+=`
`+r):o.stack=r}throw o}}_request(e,i){typeof e=="string"?(i=i||{},i.url=e):i=e||{},i=ce(this.defaults,i);const{transitional:o,paramsSerializer:s,headers:r}=i;o!==void 0&&lt.assertOptions(o,{silentJSONParsing:J.transitional(J.boolean),forcedJSONParsing:J.transitional(J.boolean),clarifyTimeoutError:J.transitional(J.boolean)},!1),s!=null&&(d.isFunction(s)?i.paramsSerializer={serialize:s}:lt.assertOptions(s,{encode:J.function,serialize:J.function},!0)),i.method=(i.method||this.defaults.method||"get").toLowerCase();let a=r&&d.merge(r.common,r[i.method]);r&&d.forEach(["delete","get","head","post","put","patch","common"],f=>{delete r[f]}),i.headers=G.concat(a,r);const n=[];let c=!0;this.interceptors.request.forEach(function(g){typeof g.runWhen=="function"&&g.runWhen(i)===!1||(c=c&&g.synchronous,n.unshift(g.fulfilled,g.rejected))});const m=[];this.interceptors.response.forEach(function(g){m.push(g.fulfilled,g.rejected)});let p,l=0,v;if(!c){const f=[ni.bind(this),void 0];for(f.unshift.apply(f,n),f.push.apply(f,m),v=f.length,p=Promise.resolve(i);l<v;)p=p.then(f[l++],f[l++]);return p}v=n.length;let E=i;for(l=0;l<v;){const f=n[l++],g=n[l++];try{E=f(E)}catch(F){g.call(this,F);break}}try{p=ni.call(this,E)}catch(f){return Promise.reject(f)}for(l=0,v=m.length;l<v;)p=p.then(m[l++],m[l++]);return p}getUri(e){e=ce(this.defaults,e);const i=oi(e.baseURL,e.url);return Yt(i,e.params,e.paramsSerializer)}}d.forEach(["delete","get","head","options"],function(e){Me.prototype[e]=function(i,o){return this.request(ce(o||{},{method:e,url:i,data:(o||{}).data}))}}),d.forEach(["post","put","patch"],function(e){function i(o){return function(r,a,n){return this.request(ce(n||{},{method:e,headers:o?{"Content-Type":"multipart/form-data"}:{},url:r,data:a}))}}Me.prototype[e]=i(),Me.prototype[e+"Form"]=i(!0)});const ze=Me;class dt{constructor(e){if(typeof e!="function")throw new TypeError("executor must be a function.");let i;this.promise=new Promise(function(r){i=r});const o=this;this.promise.then(s=>{if(!o._listeners)return;let r=o._listeners.length;for(;r-- >0;)o._listeners[r](s);o._listeners=null}),this.promise.then=s=>{let r;const a=new Promise(n=>{o.subscribe(n),r=n}).then(s);return a.cancel=function(){o.unsubscribe(r)},a},e(function(r,a,n){o.reason||(o.reason=new Se(r,a,n),i(o.reason))})}throwIfRequested(){if(this.reason)throw this.reason}subscribe(e){if(this.reason){e(this.reason);return}this._listeners?this._listeners.push(e):this._listeners=[e]}unsubscribe(e){if(!this._listeners)return;const i=this._listeners.indexOf(e);i!==-1&&this._listeners.splice(i,1)}static source(){let e;return{token:new dt(function(s){e=s}),cancel:e}}}const Xo=dt;function es(t){return function(i){return t.apply(null,i)}}function ts(t){return d.isObject(t)&&t.isAxiosError===!0}const ct={Continue:100,SwitchingProtocols:101,Processing:102,EarlyHints:103,Ok:200,Created:201,Accepted:202,NonAuthoritativeInformation:203,NoContent:204,ResetContent:205,PartialContent:206,MultiStatus:207,AlreadyReported:208,ImUsed:226,MultipleChoices:300,MovedPermanently:301,Found:302,SeeOther:303,NotModified:304,UseProxy:305,Unused:306,TemporaryRedirect:307,PermanentRedirect:308,BadRequest:400,Unauthorized:401,PaymentRequired:402,Forbidden:403,NotFound:404,MethodNotAllowed:405,NotAcceptable:406,ProxyAuthenticationRequired:407,RequestTimeout:408,Conflict:409,Gone:410,LengthRequired:411,PreconditionFailed:412,PayloadTooLarge:413,UriTooLong:414,UnsupportedMediaType:415,RangeNotSatisfiable:416,ExpectationFailed:417,ImATeapot:418,MisdirectedRequest:421,UnprocessableEntity:422,Locked:423,FailedDependency:424,TooEarly:425,UpgradeRequired:426,PreconditionRequired:428,TooManyRequests:429,RequestHeaderFieldsTooLarge:431,UnavailableForLegalReasons:451,InternalServerError:500,NotImplemented:501,BadGateway:502,ServiceUnavailable:503,GatewayTimeout:504,HttpVersionNotSupported:505,VariantAlsoNegotiates:506,InsufficientStorage:507,LoopDetected:508,NotExtended:510,NetworkAuthenticationRequired:511};Object.entries(ct).forEach(([t,e])=>{ct[e]=t});const is=ct;function pi(t){const e=new ze(t),i=_t(ze.prototype.request,e);return d.extend(i,ze.prototype,e,{allOwnKeys:!0}),d.extend(i,e,null,{allOwnKeys:!0}),i.create=function(s){return pi(ce(t,s))},i}const A=pi(it);A.Axios=ze,A.CanceledError=Se,A.CancelToken=Xo,A.isCancel=ii,A.VERSION=di,A.toFormData=Re,A.AxiosError=y,A.Cancel=A.CanceledError,A.all=function(e){return Promise.all(e)},A.spread=es,A.isAxiosError=ts,A.mergeConfig=ce,A.AxiosHeaders=G,A.formToJSON=t=>ei(d.isHTMLForm(t)?new FormData(t):t),A.getAdapter=ri.getAdapter,A.HttpStatusCode=is,A.default=A;const I=(t,e,i,o,s)=>{A.post(`${t}`,i,{headers:{Accept:"*/*","Content-Type":"application/json-patch+json",Authorization:`Bearer ${e}`}}).then(r=>{o(r.data)}).catch(r=>{s("Erro na solicitação:",r)})},pe=(t,e,i,o)=>{A.get(`${t}`,{headers:{Accept:"*/*","Content-Type":"application/json-patch+json",Authorization:`Bearer ${e}`}}).then(s=>{i(s.data)}).catch(s=>{o("Erro na solicitação:",s)})};function pt(t){const e=new Date(t),i=String(e.getDate()).padStart(2,"0"),o=String(e.getMonth()+1).padStart(2,"0"),s=e.getFullYear();return`${i}/${o}/${s}`}function L(t){return new Intl.NumberFormat("pt-BR",{style:"currency",currency:"BRL"}).format(t)}var os=Object.defineProperty,ss=Object.getOwnPropertyDescriptor,U=(t,e,i,o)=>{for(var s=o>1?void 0:o?ss(e,i):e,r=t.length-1,a;r>=0;r--)(a=t[r])&&(s=(o?a(e,i,s):a(s))||s);return o&&s&&os(e,i,s),s};let z=class extends T{constructor(){super(...arguments),this.memberId=0,this.cancelRequest=!1,this.requestId=0,this.confirmCancel=!1,this.messageCallback=!1,this.isLoading=!1,this.intervalId=0,this.token="",this.servicesUrl="",this.headerTableDetailPayment=[{label:"Veículo",id:"VehicleId"},{label:"Descrição",id:"FeeName"},{label:"Valor",id:"FeeAmount"}]}static get styles(){return[Gi]}checkPaymentStatus(t){pe(`${this.servicesUrl}/G2OnlineServices/CheckPaymentStatus?requestId=${t}`,this.token,e=>{this.IsPaid=e.IsPaid,this.IsPaid&&this.clearTime(),this.requestUpdate()},()=>{})}CancelPayment(){this.isLoading=!0,I(`${this.servicesUrl}/G2OnlineServices/CancelPayment`,this.token,{memberId:this.memberId,requestID:this.requestId},()=>{this.messageCallback=!0,this.dispatchEvent(new CustomEvent("message-callback",{composed:!0,bubbles:!0,detail:this.messageCallback})),this.isLoading=!1,this.clearTime()},t=>{console.log(t)})}checkoutCompleteSvg(){return Ae`
    <svg width="100" height="100" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path fill-rule="evenodd" clip-rule="evenodd" d="M10 20C4.47667 20 0 15.5233 0 10C0 4.47667 4.47667 0 10 0C15.5233 0 20 4.47667 20 10C20 15.5233 15.5233 20 10 20Z" fill="#12B76A"/>
      <path d="M13.6108 8.33337L8.74967 13.1945L5.83301 10.2778" stroke="#F6FEF9" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
    `}checkoutCanceledSvg(){return Ae`
    <svg width="120" height="120" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M12 2C6.486 2 2 6.486 2 12C2 17.514 6.486 22 12 22C17.514 22 22 17.514 22 12C22 6.486 17.514 2 12 2ZM16.207 14.793L14.793 16.207L12 13.414L9.207 16.207L7.793 14.793L10.586 12L7.793 9.207L9.207 7.793L12 10.586L14.793 7.793L16.207 9.207L13.414 12L16.207 14.793Z" fill="#F04438"/>
    </svg>

    `}copyPaste(t){navigator.clipboard.writeText(t);const e=this.shadowRoot.getElementById("copiedMessage");e.style.display="block",setTimeout(()=>{e.style.display="none"},3e3)}updated(t){super.updated(t),t.has("dataQrCode")&&(this.requestId=this.dataQrCode.requestId,this.IsPaid||this.dataQrCode.PaymentStatusID==1&&(this.intervalId=setInterval(()=>this.checkPaymentStatus(this.dataQrCode.requestId),3e3)))}clearTime(){clearInterval(this.intervalId)}async connectedCallback(){super.connectedCallback(),await super.updateComplete}render(){return h`
      <div id="copiedMessage" class="copied-message">
        Texto copiado com sucesso!
      </div>
      ${this.isLoading?h`<div class="spinner"><loading-spinner></loading-spinner></div>`:this.messageCallback?h`<div class="">
              <message-callback></message-callback>
            </div>`:h` ${this.showCofirmModal()} `}
    `}alertOctagon(){return Ae`
    <svg width="110" height="110" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M12 8V12M12 16H12.01M7.86 2H16.14L22 7.86V16.14L16.14 22H7.86L2 16.14V7.86L7.86 2Z" stroke="#e73300" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
    `}formatDataDetailPayment(){return this.dataQrCode.Items.map(e=>({VehicleId:e.VehicleId,FeeName:e.FeeName,FeeAmount:L(e==null?void 0:e.FeeAmount)}))}showCofirmModal(){var t,e,i,o,s,r;return this.dataQrCode?h`
      <div class="completionPayment">

      <div>
        <div class="card">
          <div class="header">
            <p>Detalhe - ${(t=this.dataQrCode)==null?void 0:t.requestId}</p>
          </div>

            <div class="cardInfos">
              <div class="padding">
                <div class="itemDetails">
                  <p>Data Emissão:</p>
                  <p>${pt((e=this.dataQrCode)==null?void 0:e.creationDate)}</p>
                </div>

                <div class="itemDetails">
                  <p>Data Vencimento PIX:</p>
                  <p>${pt((i=this.dataQrCode)==null?void 0:i.dueDate)}</p>
                </div>

                <div class="itemDetails">
                  <p>Valor Total:</p>
                  <p>${L((o=this.dataQrCode)==null?void 0:o.requestAmount)}</p>
                </div>
              

                <div class="childItems">
                  <p>Itens:</p>
                  <colibri-common-g2-table-default .theadData=${this.headerTableDetailPayment} .tbodyData=${this.formatDataDetailPayment()}></colibri-common-g2-table-default>                   
                </div>
              </div>
            </div>

          </div>
          ${window.innerWidth<880?h`
                  <div class="pix">
                    ${this.dataQrCode.PaymentStatusID!=1||this.IsPaid?null:h` <colibri-common-g2-button
                          @onClick=${()=>{var a;return this.copyPaste((a=this.dataQrCode)==null?void 0:a.copyPaste)}}
                          class="button"
                        >
                          <ph-pix-logo size="20"></ph-pix-logo> Copiar Pix
                        </colibri-common-g2-button>`}
                  </div>
                `:null}
          
          ${this.confirmCancel?null:h`<div class="cancelButtonDiv">
                  ${this.renderCancelButton()}
                </div>`}
      </div>

          ${this.confirmCancel?h`
                  <div class="confirmCancel">
                    ${this.alertOctagon()}

                    <p>Deseja realmente seguir com o cancelamento</p>

                    <div class="buttons">
                      <button @click=${()=>this.CancelPayment()}>Sim</button>
                      <button @click=${()=>this.confirmCancel=!1}>
                        Não
                      </button>
                    </div>
                  </div>
                `:window.innerWidth<880?this.renderBadgeMessage():h`<div class="qrCodeImage">
                    ${this.dataQrCode.PaymentStatusID==1?h`<p style="margin:0;">Escaneie o QR Code</p>`:null}

                    <div class="imgPix">
                      <img src=${(s=this.dataQrCode)==null?void 0:s.qrcode} />
                      ${this.IsPaid||((r=this.dataQrCode)==null?void 0:r.PaymentStatusID)==2?h`<div class="svgCheck">
                            ${this.checkoutCompleteSvg()}
                          </div>`:null}
                      ${this.statusPayment()}
                    </div>
                    <div class="pix">
                      ${this.dataQrCode.PaymentStatusID!=1||this.IsPaid?null:h`<colibri-common-g2-button
                            @onClick=${()=>{var a;return this.copyPaste((a=this.dataQrCode)==null?void 0:a.copyPaste)}}
                            class="button"
                          >
                            <ph-pix-logo size="20"></ph-pix-logo> Copiar Pix
                          </colibri-common-g2-button>`}
                    </div>
                  </div>`}
        </div>
        ${this.confirmCancel?h`
                <div class="badgeContent">
                  <ph-warning
                    color="var(--warning-600)"
                    weight="bold"
                    size="22"
                  ></ph-warning>

                  <p>
                    Pagamentos relacionados a envio de documentos, quando
                    cancelado, automaticamente cancela a solicitação de envio do
                    documento
                  </p>
                </div>
              `:null}
        </div>
          `:h`
        <div class="skeletons skeletonChildWidth">
          <div class="skeleton skeletonSize"></div>
          <div class="skeleton skeletonSize"></div>
        </div>
      `}shouldShowCancelButton(){var t;return!this.IsPaid&&this.cancelRequest&&((t=this.dataQrCode)==null?void 0:t.PaymentStatusID)===1}toggleConfirmCancel(){this.confirmCancel=!this.confirmCancel}renderCancelButton(){return this.shouldShowCancelButton()?h`
        <colibri-common-g2-button
          variant="error"
          class="button"
          @click=${this.toggleConfirmCancel}
        >
          Cancelar
        </colibri-common-g2-button>
      `:null}renderBadgeMessage(){var t,e,i;if(((t=this.dataQrCode)==null?void 0:t.PaymentStatusID)==2)return h`<colibri-common-g2-badge
        type="success"
        text="Pagamento Concluído"
      ></colibri-common-g2-badge>`;if(((e=this.dataQrCode)==null?void 0:e.PaymentStatusID)==3)return h`<colibri-common-g2-badge
        type="yellow"
        text="Pagamento Cancelado"
      ></colibri-common-g2-badge>`;if(((i=this.dataQrCode)==null?void 0:i.PaymentStatusID)==4)return h`<colibri-common-g2-badge
        type="yellow"
        text="Pagamento Expirado"
      ></colibri-common-g2-badge>`}statusPayment(){var t,e;if(((t=this.dataQrCode)==null?void 0:t.PaymentStatusID)==3||((e=this.dataQrCode)==null?void 0:e.PaymentStatusID)==4)return h`<div class="svgCanceled">${this.checkoutCanceledSvg()}</div>`}handleOnModalCard(){const t=new CustomEvent("my-close-modal");this.dispatchEvent(t)}};U([b()],z.prototype,"dataQrCode",2),U([b()],z.prototype,"memberId",2),U([b()],z.prototype,"cancelRequest",2),U([u()],z.prototype,"requestId",2),U([u()],z.prototype,"confirmCancel",2),U([u()],z.prototype,"messageCallback",2),U([u()],z.prototype,"isLoading",2),U([u()],z.prototype,"intervalId",2),U([b({type:String})],z.prototype,"token",2),U([b()],z.prototype,"servicesUrl",2),z=U([R("qrcode-visualizer")],z);const as=_`
  .content {
    padding: 20px;
    .form {
      display: grid;
      gap: 20px;
      grid-template-columns: repeat(2, 1fr);

      .input {
        display: flex;
        flex-direction: column;
        gap: 5px;

        input {
          padding: 5px;
          border: 2px solid gray;
          border-radius: 4px;
          font-family: 'Red Hat Display', sans-serif !important;
          width: 250px;
          font-size: 14px;
        }
        .error {
          border: 2px solid #d82020;
        }
        .error-message {
          color: #d82020;
        }
      }
    }
    .buttons {
      display: flex;
      width: 100%;
      gap: 15px;
      justify-content: flex-end;
      margin-top: 20px;

      button {
        background-color: #ffb838;
        border-radius: 4px;
        padding: 8px 16px;
        color: black;
        font-weight: 600;
        border: none;
        cursor: pointer;
        font-family: 'Red Hat Display';

        &:disabled {
          background-color: #eba930;
          cursor: not-allowed;
        }
      }
    }
  }
`;var rs=Object.defineProperty,ns=Object.getOwnPropertyDescriptor,he=(t,e,i,o)=>{for(var s=o>1?void 0:o?ns(e,i):e,r=t.length-1,a;r>=0;r--)(a=t[r])&&(s=(o?a(e,i,s):a(s))||s);return o&&s&&rs(e,i,s),s};let K=class extends T{constructor(){super(...arguments),this.zipCode="",this.dataAddress=null,this.servicesUrl="https://g2services-qa4.copart.com.br/",this.token=""}async connectedCallback(){super.connectedCallback(),await super.updateComplete}fetchData(){I(`${this.servicesUrl}/G2Member/SearchZipCode`,this.token,{zipCode:this.zipCode},e=>{this.zipCodeDetails=e.zipCodeDetails,this.requestUpdate()},()=>{})}handleSaveChanges(){const e=this.shadowRoot.querySelectorAll(".inputClass");let i=!0;e.forEach(o=>{const s=this.shadowRoot.getElementById(`${o.id}Error`);o.value.trim()?o.id==="cep"&&!this.isValidCEP(o.value.trim())?(i=!1,o.classList.add("error"),s.textContent="CEP inválido."):(o.classList.remove("error"),s.textContent=""):(i=!1,o.classList.add("error"),s.textContent="Este campo é obrigatório.")}),i?this.saveData():console.log("Por favor, corrija os erros antes de salvar.")}saveData(){console.log("Dados salvos com sucesso!")}handleCloseModal(){this.dispatchEvent(new CustomEvent("colibri-handle-show-shipping-address",{composed:!0,bubbles:!0,detail:{}}))}render(){var e,i,o,s,r,a,n;return h`
      <div class="content">
        <div class="form">
          <div class="input">
            <label for="">CEP</label>
            <input
              @input=${this.handleInput}
              class="inputClass"
              id="cep"
              type="text"
              @blur=${()=>this.fetchData()}
              .value=${((e=this.dataAddress)==null?void 0:e.ZipCode)||null}
            />
            <span id="cepError" class="error-message"></span>
          </div>
          <div class="input">
            <label for="">Logradouro</label>
            <input
              id="street"
              class="inputClass"
              type="text"
              .value=${((i=this.dataAddress)==null?void 0:i.AddressName)||null}
            />
            <span id="streetError" class="error-message"></span>
          </div>
          <div class="input">
            <label for="">Número</label>
            <input
              id="number"
              class="inputClass"
              .value=${((o=this.dataAddress)==null?void 0:o.AddressNumber)||null}
              type="text"
            />
            <span id="numberError" class="error-message"></span>
          </div>
          <div class="input">
            <label for="">Complemento</label>
            <input
              id="complement"
              .value=${((s=this.dataAddress)==null?void 0:s.Complement)||null}
              type="text"
            />
          </div>
          <div class="input">
            <label for="">Bairro</label>
            <input
              id="neighborhood"
              value=${(r=this.dataAddress)==null?void 0:r.Neighborhood}
              class="inputClass"
              type="text"
            />
            <span id="neighborhoodError" class="error-message"></span>
          </div>
          <div class="input">
            <label for="">Cidade</label>
            <input
              value=${(a=this.dataAddress)==null?void 0:a.City}
              id="city"
              class="inputClass"
              type="text"
            />
            <span id="cityError" class="error-message"></span>
          </div>
          <div class="input">
            <label for="">Estado</label>
            <input
              value=${(n=this.dataAddress)==null?void 0:n.State}
              id="state"
              class="inputClass"
              type="text"
            />
            <span id="stateError" class="error-message"></span>
          </div>
        </div>

        <div class="buttons">
          <button @click=${this.handleCloseModal}>Voltar</button>
          <button @click=${this.handleSaveChanges}>Salvar Alterações</button>
        </div>
      </div>
    `}isValidCEP(e){return/^\d{5}-\d{3}$/.test(e)}handleInput(e){const i=e.target,o=i.value.replace(/\D/g,""),s=this.formatCEP(o);this.zipCode=i.value,i.value=s}formatCEP(e){const i=/^(\d{0,5})(\d{0,3})$/,o=e.match(i);return o?`${o[1]}${o[2]?"-"+o[2]:""}`:e}};K.styles=[as],he([u()],K.prototype,"zipCode",2),he([u()],K.prototype,"zipCodeDetails",2),he([b()],K.prototype,"dataAddress",2),he([b()],K.prototype,"servicesUrl",2),he([b({type:String})],K.prototype,"token",2),K=he([R("shipping-address")],K);const ls=_`
  label {
    font-size: var(--text-small-sm);
    font-weight: var(--weight-medium);
    color: var(--gray-600);
    margin-bottom: 4px;
  }

  .skeleton-container {
    display: flex;
    flex-direction: column;
    border: 1px solid var(--gray-200);
    border-radius: 8px;
    height: 100%;

    .row {
      display: flex;
      align-items: center;

      .column {
        display: flex;
        flex-direction: column;
        width: 100%;

        .row-skeleton {
          height: 31px;
        }
      }
    }
  }
`,ds=_`
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
`,cs=_`
  @keyframes shimmer {
    0% {
      background-position: 0% 0%;
    }
    100% {
      background-position: -135% 0%;
    }
  }

  .skeleton {
    background-image: linear-gradient(
      -90deg,
      #e7edf1 0%,
      #f8f8f8 50%,
      #e7edf1 100%
    );
    background-size: 400% 400%;
    animation: shimmer 1.2s ease-in-out infinite;

    &.white {
      background-image: linear-gradient(
        -90deg,
        #fff 0%,
        #e7edf1 50%,
        #fff 100%
      );
    }
  }
`;var ps=Object.defineProperty,hs=Object.getOwnPropertyDescriptor,hi=(t,e,i,o)=>{for(var s=o>1?void 0:o?hs(e,i):e,r=t.length-1,a;r>=0;r--)(a=t[r])&&(s=(o?a(e,i,s):a(s))||s);return o&&s&&ps(e,i,s),s};let ht=class extends T{constructor(){super(...arguments),this.isLabel=""}static get styles(){return[ds,cs,ls]}shimmerTable(){return h`
      <div class="row">
        <div class="column">
          <div class="skeleton">
            <div class="row-skeleton white"></div>
          </div>
        </div>
      </div>
    `}skeleton(){return h` <div>
      ${this.isLabel&&h`<label for=${this.isLabel}>${this.isLabel}</label>`}

      <div class="skeleton-container">${this.shimmerTable()}</div>
    </div>`}render(){return h` ${this.skeleton()} `}};hi([b({type:String})],ht.prototype,"isLabel",2),ht=hi([R("ui-load-input")],ht);var us=Object.defineProperty,ms=Object.getOwnPropertyDescriptor,fs=(t,e,i,o)=>{for(var s=o>1?void 0:o?ms(e,i):e,r=t.length-1,a;r>=0;r--)(a=t[r])&&(s=(o?a(e,i,s):a(s))||s);return o&&s&&us(e,i,s),s};let ut=class extends T{render(){return h`
      <div class="spinner"></div>
    `}};ut.styles=_`
    :host {
      display: block;
      text-align: center;
    }
    .spinner {
      border: 4px solid rgba(0, 0, 0, 0.1);
      border-left-color: #7983ff;
      border-radius: 50%;
      width: 40px;
      height: 40px;
      animation: spin 1s linear infinite;
    }
    @keyframes spin {
      to {
        transform: rotate(360deg);
      }
    }
  `,ut=fs([R("loading-spinner")],ut);const gs=_`
  .content {
    gap: 20px;
    padding: 10px;
    width: 55vw;

    .button {
      background-color: #ffb838;
      border-radius: 4px;
      padding: 8px 16px;
      color: black;
      font-weight: 600;
      border: none;
      cursor: pointer;
      font-family: 'Red Hat Display';

      &:disabled {
        background-color: #eba930;
        cursor: not-allowed;
      }

      &.minHeight {
        margin-top: auto;
        height: 50px;
      }
    }

    .cardsSelect {
      width: 100%;

      .card {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: row;
        gap: 20px;
        width: 100%;

        button {
          height: 100px;
          padding: 30px;
          width: 100%;
          font-family: 'Red Hat Display';
          cursor: pointer;
          border: none;
          border-radius: 8px;
          font-weight: 600;
          font-size: 14px;
          background-color: #ffb938;
          border: 2px solid #ffb838;
          transition: all ease-in-out 100ms;

          &:hover {
            background-color: white;
          }
        }
      }
    }

    .addressActual {
      margin-top: 20px;
      border: 2px solid #ffb938;
      border-radius: 8px;
      padding: 10px;
      display: flex;
      justify-content: space-between;

      .address {
        width: 400px;
        display: flex;
        flex-direction: column;
        gap: 10px;
        p {
          margin: 0;
          &:nth-of-type(2) {
            margin-top: 10px;
          }
        }
      }
    }

    @media (max-width: 768px) {
      overflow: auto;
      flex-direction: column;
      width: 100vw;
      height: 80vh;
    }
  }

  .displayRow {
    display: grid;
    grid-template-columns: 65% auto;
  }

  .modal-tbody {
    display: flex;
    flex-direction: column;
    width: 100%;

    .tr {
      display: grid;
      grid-template-columns: repeat(4, 1fr);

      .td {
        font-size: 12px;
        padding: 4px 10px;
        color: black;
      }
    }

    .firstLine {
      background-color: #fff;
    }

    .secondLine {
      background-color: #eee;
    }
  }

  .thead-td {
    background-color: #dfdfdf;
    padding: 10px;
    font-weight: bold;
    font-size: 12px;
  }

  .table thead .th-table {
    padding: 8px;
    font-size: 12px;
    color: #151317;
    background-clip: padding-box !important;
    text-align: left;
    border-right: 1px solid white;
  }

  .sideBar {
    display: flex;
    flex-direction: column;
    gap: 20px;

    .box {
      padding: 10px;
      border: 1px solid #c9c9c9;
      border-radius: 4px;

      h2 {
        margin: 0;
      }
    }

    button {
      background-color: #ffb838;
      border-radius: 4px;
      padding: 8px 16px;
      color: black;
      font-weight: 600;
      border: none;
      cursor: pointer;
      font-family: 'Red Hat Display';

      &:disabled {
        background-color: #eba930;
        cursor: not-allowed;
      }
    }
  }

  .blue {
    background-color: #1254ff !important;
    color: white !important;
  }
`;var bs=Object.defineProperty,ys=Object.getOwnPropertyDescriptor,X=(t,e,i,o)=>{for(var s=o>1?void 0:o?ys(e,i):e,r=t.length-1,a;r>=0;r--)(a=t[r])&&(s=(o?a(e,i,s):a(s))||s);return o&&s&&bs(e,i,s),s};let V=class extends T{constructor(){super(...arguments),this.isLoadTable=!1,this.shippingType=0,this.servicesUrl="",this.memberId=0,this.token="",this.theadData=[{label:"Código",id:"VehicleId"},{label:"Leilão",id:"SaleInfo"},{label:"Lote",id:"ProcessId"},{label:"Status",id:"Status"}]}async connectedCallback(){super.connectedCallback(),await super.updateComplete,this.fetchData()}fetchData(){pe(`${this.servicesUrl}/G2OnlineServices/GetMemberAddress?id=${this.memberId}`,this.token,e=>{this.addressData=e.Address,this.requestUpdate()},()=>{})}handleHideShippingAddress(){this.shippingType=0,this.requestUpdate()}changeStep(e){e==0?(this.shippingType=0,this.requestUpdate()):e==1?(this.shippingType=1,this.requestUpdate()):e==2?(this.shippingType=2,this.requestUpdate()):e==3?(this.shippingType=3,this.requestUpdate()):e==4&&(this.shippingType=4,this.requestUpdate())}renderStep0(){var e,i,o,s,r,a;return h`<div class="content">
      <div class="cardsSelect">
        <div class="card">
          <button @click=${()=>this.changeStep(1)}>
            ENVIO PARA ENDEREÇO ATUAL
          </button>
          <button @click=${()=>this.changeStep(4)}>
            ENVIO PARA ENDEREÇO TERCEIRO
          </button>
          <button @click=${()=>this.changeStep(3)}>ENVIO PARA PÁTIO</button>
        </div>
      </div>

      <div class="addressActual">
        <div class="address">
          <p>Endereço atual:</p>
          <p>
            ${(e=this.addressData)==null?void 0:e.AddressName},
            ${(i=this.addressData)==null?void 0:i.AddressNumber}, ${(o=this.addressData)==null?void 0:o.ZipCode}
          </p>
          <p>${(s=this.addressData)==null?void 0:s.Neighborhood}</p>
          <p>${(r=this.addressData)==null?void 0:r.City} - ${(a=this.addressData)==null?void 0:a.State}</p>
        </div>
        <button @click=${()=>this.changeStep(2)} class="button minHeight">
          ALTERAR ENDEREÇO
        </button>
      </div>
    </div>`}renderStep1(){var e,i,o,s,r,a;return h`${h`<div class="content displayRow">
      <div class="modal-tbody">
        <div class="tr">
          ${this.theadData.map(n=>h` <div class="thead-td">${n.label}</div> `)}
        </div>

        ${this.isLoadTable?h`
              <div class="Skeletons-tbody">
                <div class="skeleton skeletonItem"></div>
                <div class="skeleton2 skeletonItem"></div>
                <div class="skeleton skeletonItem"></div>
                <div class="skeleton2 skeletonItem"></div>
              </div>
            `:(e=this.dataList)==null?void 0:e.map((n,c)=>h`
                <div
                  class=${c%2===0?"tr firstLine":"tr secondLine"}
                >
                  ${this.theadData.map(m=>h` <div class="td">${n[m.id]}</div> `)}
                </div>
              `)}
      </div>
      <div class="sideBar">
        <div class="box">
          <h2>Endereço de Envio</h2>
          <p>
            ${(i=this.addressData)==null?void 0:i.AddressName}, ${(o=this.addressData)==null?void 0:o.AddressNumber}
          </p>
          <p>${(s=this.addressData)==null?void 0:s.Neighborhood} - ${(r=this.addressData)==null?void 0:r.City}</p>
          <p>CEP: ${(a=this.addressData)==null?void 0:a.ZipCode}</p>
        </div>
        <div class="box">
          <h2>Observação</h2>
          <p>Ressaltamos que será por conta e risco do arrametante</p>
        </div>
        <div class="">
          <h2>Total Envio: R$ 85,00</h2>
          <div>
            <button @click=${()=>this.changeStep(0)} class="button">
              Voltar
            </button>
            <button class="button blue">Confirmar</button>
          </div>
        </div>
      </div>
    </div>`}`}renderStep2(){return h`<shipping-address
      @colibri-handle-show-shipping-address=${this.handleHideShippingAddress}
      .dataAddress=${this.addressData}
    ></shipping-address>`}renderStep3(){return h`<p>OPa</p>`}renderStep4(){return h` <shipping-address
      @colibri-handle-show-shipping-address=${this.handleHideShippingAddress}
    ></shipping-address>`}steps(){switch(this.shippingType){case 1:return this.renderStep1();case 2:return this.renderStep2();case 3:return this.renderStep3();case 4:return this.renderStep4();default:return this.renderStep0()}}render(){return this.steps()}};V.styles=[gs],X([u()],V.prototype,"isLoadTable",2),X([u()],V.prototype,"shippingType",2),X([u()],V.prototype,"addressData",2),X([b()],V.prototype,"dataList",2),X([b()],V.prototype,"servicesUrl",2),X([b()],V.prototype,"memberId",2),X([b({type:String})],V.prototype,"token",2),V=X([R("document-shipping")],V);const xs=_`
  .container {
    width: calc(100vw - 10rem);
    padding: 1rem;
    display: grid;
    grid-template-columns: 50% auto;
    gap: 20px;

    section {
      display: flex;
      flex-direction: column;
      gap: 20px;

      .address {
        border: 1px solid #ccc;
        padding: 10px;
        border-radius: 6px;

        .steps {
          height: 300px;
        }
      }

      .observation {
        border: 1px solid #ccc;
        padding: 10px;
        border-radius: 6px;

        p {
          color: var(--warning-500);
        }
      }

      h2 {
        margin: 0;
        span {
          color: var(--success-600);
        }
      }

      .contentButton {
        display: flex;
        justify-content: space-between;
        button {
          border-radius: 4px;
          padding: 8px 16px;
          color: white;
          font-weight: 600;
          border: none;
          cursor: pointer;
          font-family: 'Red Hat Display';
          width: 100px;

          background-color: #ffb838;
          color: black;
        }
      }
    }
  }

  .contentSelect {
    margin-top: 10px;
  }

  @media (max-width: 880px) {
    .container {
      width: 100%;
      grid-template-columns: 1fr;

      .sectionStep {
        width: 370px;
      }

      section {
        .address {
          .steps {
            height: auto;
          }
        }
      }
    }
  }
`,vs=(t,e,i)=>{let o="";return e===!1?!0:t[e]&&i.length===0?(o=t[e].errorNull,{[e]:o}):t[e]&&!t[e].regex.test(i)?(o=t[e].message,{[e]:o}):(o=null,{[e]:o})};function Ue(t,e){const s=Object.entries(e).map(a=>vs(t,a[0],a[1])).reduce((a,n)=>{const c=Object.keys(n)[0],m=n[c];return m!==null&&(a[c]=m),a},{});return Object.keys(t).filter(a=>!e[a]).forEach(a=>{s[a]||(s[a]=t[a].errorNull)}),s}const mt={AddressNumber:{regex:/^\d+$/,message:"Valor inválido",errorNull:"Preencha o campo Número"},ZipCode:{regex:/^\d{8}$/,message:"CEP inválido",errorNull:"Preencha o campo CEP"}},ws={Yard:{regex:/^\d+$/,message:"Valor inválido",errorNull:"Selecione uma opção"}};var $s=Object.defineProperty,Cs=Object.getOwnPropertyDescriptor,k=(t,e,i,o)=>{for(var s=o>1?void 0:o?Cs(e,i):e,r=t.length-1,a;r>=0;r--)(a=t[r])&&(s=(o?a(e,i,s):a(s))||s);return o&&s&&$s(e,i,s),s};let C=class extends T{constructor(){super(...arguments),this.isLoadTable=!1,this.shippingType=0,this.activeStep="Meu Endereço",this.isEditActualForm=!1,this.yardSelected={Yard:""},this.showPixModal=!1,this.actualForm={AddressName:"",AddressNumber:"",ZipCode:"",Neighborhood:"",City:"",State:"",Complement:"",CityId:""},this.thirdForm={AddressName:"",AddressNumber:"",ZipCode:"",Neighborhood:"",City:"",State:"",Complement:"",CityId:""},this.errorsActualForm={AddressNumber:"",ZipCode:""},this.errorYardSelect={Yard:""},this.errorsThirdForm={AddressNumber:"",ZipCode:""},this.servicesUrl="",this.memberId=0,this.token="",this.theadData=[{label:"Código",id:"VehicleId"},{label:"Marca",id:"Make"},{label:"Modelo",id:"Model"},{label:"Tipo de Venda",id:"SaleType"},{label:"Status",id:"Status"}]}async connectedCallback(){super.connectedCallback(),await super.updateComplete,this.fetchData()}fetchData(){pe(`${this.servicesUrl}/G2OnlineServices/GetShippingOptions?id=${this.memberId}&qt=${this.dataList.length}`,this.token,e=>{this.actualForm=e.MemberAddress,this.addressData=e,this.yardsChildren=e.Yards.map(i=>({id:String(i.Amount),value:String(i.YardId),name:i.YardName})),this.yardsChildren.unshift({id:"0",value:"0",name:"Selecione uma opção"}),this.feeCost=e.MemberAddress.Amount,this.requestUpdate()},()=>{})}save(){this.errorsActualForm=Ue(mt,this.actualForm),!Object.entries(this.errorsActualForm).length&&I(`${this.servicesUrl}/G2OnlineServices/ChangeMemberAddress`,this.token,{memberId:this.memberId,addressName:this.actualForm.AddressName,number:this.actualForm.AddressNumber,zipCode:this.actualForm.ZipCode,neighborhood:this.actualForm.Neighborhood,cityId:this.actualForm.CityId,complement:this.actualForm.Complement},()=>{this.GetFeeCostByStateOrYard(this.actualForm.State),this.requestUpdate()},()=>{})}handleStepChange(e){this.activeStep=e,this.isEditActualForm=!1,this.activeStep=="Meu Endereço"?this.feeCost=this.addressData.MemberAddress.Amount:this.feeCost=0}wichFormProp(e){return this.activeStep=="Meu Endereço"?this.actualForm[e]:this.thirdForm[e]}titleModalChange(e){let i;return e.PaymentStatusID==2?i="Pagamento Realizado":e.PaymentStatusID==3?i="Pagamento Cancelado":(i="Aguardando Pagamento",this.messageCallback&&(i="Aviso")),i}updated(e){super.updated(e),e.has("messageModal")&&this.titleModalChange(this.dataQrCode)}requestDispatchDocuments(){this.errorsActualForm=Ue(mt,this.actualForm),this.errorsThirdForm=Ue(mt,this.thirdForm),this.errorYardSelect=Ue(ws,this.yardSelected);const e=this.dataList.map(s=>s.ProcessId);let i;if(this.activeStep=="Meu Endereço"?i=this.errorsActualForm:this.activeStep=="Outro Endereço"?i=this.errorsThirdForm:i=this.errorYardSelect,Object.entries(i).length)return;this.showPixModal=!this.showPixModal;const o={memberId:this.memberId,requestsIds:e,requestType:this.activeStep=="Pátio Copart"?2:this.activeStep=="Meu Endereço"?1:3,yardIdSelect:Number(this.yardSelected.Yard),address:this.wichFormProp("AddressName"),addressNumber:this.wichFormProp("AddressNumber"),neighborhood:this.wichFormProp("Neighborhood"),complement:this.wichFormProp("Complement"),zipCode:this.wichFormProp("ZipCode"),cityId:Number(this.wichFormProp("CityId"))};I(`${this.servicesUrl}/G2OnlineServices/RequestDispatchDocuments`,this.token,o,s=>{this.dataQrCode={...s.invoice,Items:s.Items},this.dispatchEvent(new CustomEvent("data-QrCode",{composed:!0,detail:this.titleModalChange(this.dataQrCode)})),this.requestUpdate()},()=>{})}GetFeeCostByStateOrYard(e){I(`${this.servicesUrl}/G2OnlineServices/GetFeeCostByStateOrYard`,this.token,{memberId:this.memberId,documentsQuantity:this.dataList.length,address:{state:e}},i=>{this.feeCost=i.FeeCost,this.requestUpdate()},()=>{})}dataListFormatted(){return this.dataList.map(e=>({...e,SaleType:`${e.SaleType}: ${e.SaleInfo}`}))}clearInterval(){this.qrcodeVisualizer.clearTime()}render(){var i;const e=[{name:"Meu Endereço",item:h`<actual-form
          @zipcode-searched-sucessfully=${o=>{this.actualForm=o.detail}}
          @on-Change=${o=>this.onChangeActualForm(o.detail.name,o.detail.value)}
          @is-edit=${o=>this.isEditActualForm=!o.detail}
          .data=${this.actualForm}
          .errors=${this.errorsActualForm}
          @save-new-address=${this.save}
          .servicesUrl=${this.servicesUrl}
        ></actual-form>`},{name:"Pátio Copart",item:h`<div class="contentSelect">
          <colibri-common-g2-select
            isLabel="Pátios"
            isPlaceholder="Selecione uma opção"
            .isChildren=${this.yardsChildren}
            @on-input=${o=>this.onChangeYardSelect(o)}
            .error=${this.errorYardSelect.Yard}
          ></colibri-common-g2-select>
        </div>`},{name:"Outro Endereço",item:h`<third-form
          @zipcode-searched-sucessfully=${o=>{this.thirdForm=o.detail,this.GetFeeCostByStateOrYard(o.detail.State)}}
          @on-Change=${o=>this.onChangeThirdForm(o.detail.name,o.detail.value)}
          .errors=${this.errorsThirdForm}
          .data=${this.thirdForm}
          .servicesUrl=${this.servicesUrl}
        ></third-form>`}];return h`
      ${this.showPixModal?h`<qrcode-visualizer
            id="qrcodeVisualizer"
            .dataQrCode=${this.dataQrCode}
            .requestId=${(i=this.dataQrCode)==null?void 0:i.requestId}
            .cancelRequest=${!0}
            .memberId=${this.memberId}
            .servicesUrl=${this.servicesUrl}
            .token=${this.token}
            @message-callback=${o=>this.messageCallback=o.detail}
          ></qrcode-visualizer>`:h` <div class="container">
          ${window.innerWidth<880?null:h`<div class="sectionStep">
                  <h2>Lista de itens</h2>

                  <colibri-common-g2-table-default
                    .theadData=${this.theadData}
                    .tbodyData=${this.dataListFormatted()}
                  ></colibri-common-g2-table-default>
                </div>`}
                

                <section class="sectionStep">
                  <div class="address">
                    <h2>Endereço para envio</h2>

                    <div>
                      <colibri-common-g2-step
                        .data=${e}
                        active=${this.activeStep}
                        @onClick=${o=>this.handleStepChange(o.detail.name)}
                      ></colibri-common-g2-step>
                    </div>
                    <div class="steps">
                      ${e.filter(o=>o.name==this.activeStep)[0].item}
                    </div>
                  </div>

                  ${window.innerWidth<880?null:h`<div class="observation">
                          <h2>Observação</h2>
                          <p>
                            Ressaltamos que será por conta e risco do
                            arrematante eventuais extravios que possam ocorrer
                            no trajeto e destino desse documento, conforme
                            condições de venda.
                          </p>
                        </div>`}
                  

                  <div class="contentButton">
                    <h2>
                      Total:
                      <span>${L(this.feeCost)}</span>
                    </h2>

                    <colibri-common-g2-button .isDisabled=${this.isEditActualForm||this.activeStep=="Outro Endereço"&&this.thirdForm.Neighborhood==""} @onClick=${this.requestDispatchDocuments}>
                      Confirmar
                    </colibri-common-g2-button>
                  </div>
                </section>
              </div>
              </div>
              `}
    `}onChangeActualForm(e,i){this.actualForm={...this.actualForm,[e]:i}}onChangeThirdForm(e,i){this.thirdForm={...this.thirdForm,[e]:i}}onChangeYardSelect(e){this.feeCost=e.detail.id,this.yardSelected.Yard=e.detail.value}};C.styles=[xs],k([Ee("#qrcodeVisualizer")],C.prototype,"qrcodeVisualizer",2),k([u()],C.prototype,"isLoadTable",2),k([u()],C.prototype,"shippingType",2),k([u()],C.prototype,"activeStep",2),k([u()],C.prototype,"addressData",2),k([u()],C.prototype,"feeCost",2),k([u()],C.prototype,"yardsChildren",2),k([u()],C.prototype,"isEditActualForm",2),k([u()],C.prototype,"yardSelected",2),k([u()],C.prototype,"showPixModal",2),k([u()],C.prototype,"dataQrCode",2),k([u()],C.prototype,"messageCallback",2),k([u()],C.prototype,"actualForm",2),k([u()],C.prototype,"thirdForm",2),k([u()],C.prototype,"errorsActualForm",2),k([u()],C.prototype,"errorYardSelect",2),k([u()],C.prototype,"errorsThirdForm",2),k([b()],C.prototype,"dataList",2),k([b()],C.prototype,"servicesUrl",2),k([b()],C.prototype,"memberId",2),k([b({type:String})],C.prototype,"token",2),C=k([R("documents-send")],C);const Ss=_`
  :root {
    /* scroll */
    --scrollbar-size: 10px;

    /* Colors */
    --gray-25: #fcfcfd;
    --gray-50: #f9fafb;
    --gray-100: #f2f4f7;
    --gray-200: #eaecf0;
    --gray-300: #d0d5dd;
    --gray-400: #98a2b3;
    --gray-500: #667085;
    --gray-600: #475467;
    --gray-700: #344054;
    --gray-800: #1d2939;
    --gray-900: #101828;

    /* Primary-Color */
    --blue-50: #eaf2ff;
    --blue-100: #d5e5ff;
    --blue-200: #a6c8ff;
    --blue-300: #77abff;
    --blue-400: #489eff;
    --blue-500: #1254ff; /* Base */
    --blue-600: #0041cc;
    --blue-700: #003199;
    --blue-800: #002066;
    --blue-900: #001033;

    /* Error-Color */
    --error-50: #ffe8e0;
    --error-100: #ffd1c1;
    --error-200: #ffa392;
    --error-300: #ff7c63;
    --error-400: #ff5534;
    --error-500: #f76120;
    --error-600: #c23e18;
    --error-700: #911a0f;
    --error-800: #5f0e08;
    --error-900: #2e0704;

    /* Warning-Color */
    --yellow-50: #fff8e1;
    --yellow-100: #fff0c2;
    --yellow-200: #ffe999;
    --yellow-300: #ffdb70;
    --yellow-400: #ffce47;
    --yellow-500: #ffb838; /* Base */
    --yellow-600: #cc971f;
    --yellow-700: #996e15;
    --yellow-800: #66460c;
    --yellow-900: #332306;

    /*  Success-Color */
    --success-50: #e5f4e0;
    --success-100: #c9e9c1;
    --success-200: #9edf99;
    --success-300: #73d471;
    --success-400: #47c948;
    --success-500: #238202; /* Base */
    --success-600: #1a6300;
    --success-700: #113f00;
    --success-800: #092600;
    --success-900: #040d00;

    /* Warning-Color */
    --warning-25: #fffcf5;
    --warning-50: #fffaeb;
    --warning-100: #fef0c7;
    --warning-200: #fedf89;
    --warning-300: #fec84b;
    --warning-400: #fdb022;
    --warning-500: #f79009;
    --warning-600: #dc6803;
    --warning-700: #b54708;
    --warning-800: #93370d;
    --warning-900: #7a2e0e;

    /* Fonts */
    --body-font: 'Red Hat Display', sans-serif;
    --text-small-xs: 0.75rem; /* 12px */
    --text-small-sm: 0.875rem; /* 14px */
    --text-small-md: 1rem; /* 16px */
    --text-small-lg: 1.125rem; /* 18px */
    --text-small-xl: 1.25rem; /* 20px */
    --text-headline-sm: 1.5rem; /* 24px */
    --text-headline-md: 1.75rem; /* 28px */
    --text-headline-lg: 2.187rem; /* 35px */
    --text-display-sm: 3rem; /* 48px */
    --text-display-md: 3.75rem; /* 60px */
    --text-display-lg: 4.5rem; /* 72px */

    /* Font weight */
    --weight-light: 300;
    --weight-regular: 400;
    --weight-medium: 500;
    --weight-semibold: 600;
    --weight-bold: 700;
    --weight-extrabold: 800;
  }

  .content {
    .buttonsModal {
      display: flex;
      justify-content: flex-end;
      gap: 10px;
    }

    .header {
      display: flex;
      justify-content: space-between;
      align-items: center;

      .title {
        color: #1254ff;
        font-weight: bolder;
        font-family: 'Red Hat Display', sans-serif;
        font-size: 3rem;
        padding: 0px;
        margin: 0px;
      }

      .header-actions {
        display: flex;
        align-items: center;
        gap: 12px;

        .button-print {
          display: flex;
          align-items: center;
          gap: 6px;
          font-size: var(--text-small-sm);
          font-weight: var(--weight-semibold);
          color: var(--gray-700);
          background-color: transparent;
          border: none;
          font-family: inherit;
          cursor: pointer;

          &:hover {
            color: var(--blue-600);
            text-decoration: underline;
          }
        }
      }
    }

    .border {
      border: 1px solid #ddd;
      border-radius: 6px;
    }

    .responsiveButton {
      display: none;
    }

    .filters {
      display: flex;
      justify-content: flex-start;
      align-items: flex-end;
      gap: 20px;
      margin-top: 10px;
      margin-left: 5px;

      .input {
        width: 200px;
      }
    }

    @media (max-width: 880px) {
      .responsiveButton {
        display: block;
        margin-block: 10px;
      }

      .filters {
        display: none;
      }
    }
  }

  .padding {
    padding: 10px;
  }

  .expandChildTable::before {
    display: block;
    cursor: pointer;
  }

  .totalPayment {
    text-align: end;
  }

  .button {
    background-color: #ffb838;
    border-radius: 4px;
    padding: 8px 16px;
    color: black;
    font-weight: 600;
    border: none;
    cursor: pointer;
    font-family: 'Red Hat Display';

    &:disabled {
      background-color: #eba930;
      cursor: not-allowed;
    }
  }

  .completionPayment .card .header {
    background-color: #101f46;
    text-align: center;
    padding: 5px;
    color: white;
  }

  .modal-tbody {
    display: flex;
    flex-direction: column;
  }

  .Skeletons-tbody {
    display: flex;
    flex-direction: column;
  }

  .skeletonItem {
    width: 100%;
    height: 20px;
  }

  .modal-tr {
    display: grid;
    grid-template-columns: 100px 180px 1fr 1fr 100px;
  }

  .modal-td {
    font-size: 12px;
    padding: 4px 10px;
    color: black;
  }

  .checkbox {
    cursor: pointer;

    &:disabled {
      cursor: not-allowed;
    }
  }

  .theadFees {
    background-color: #ddd;
  }

  .contentTable {
    display: flex;
    flex-direction: column;
    /* gap: 10px; */

    .rowPayment {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-inline: 2px;

      .textIcons {
        display: flex;
        /* align-items: center; */
        gap: 12px;

        .align {
          display: flex;
          justify-content: center;
        }

        a {
          display: flex;
          align-items: flex-end;
          gap: 4px;
          font-weight: 700;
          font-size: 12px;
          cursor: pointer;
        }
      }

      p {
        font-size: 13px;
        font-weight: 700;
      }
    }
  }

  .pagination {
    margin-block: 10px;
    margin-inline: 5px;
  }

  .link {
    color: #1254ff;
    cursor: pointer;
  }

  .childTableRowTr {
    display: grid;
    grid-template-columns: 50px repeat(auto-fill, minmax(230px, 1fr));
    border: 1px solid #d0d0d0;
    width: 600px;
    background-color: white;

    .bold {
      font-weight: bold;
      text-align: center;
    }

    .amount {
      text-align: right;
    }
  }

  .contentChildrenTable {
    padding: 10px;
  }

  .childTableRowTrTable {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(230px, 1fr));
    border: 1px solid #d0d0d0;
    width: 600px;
    background-color: white;
  }

  .childTableRowTrModalHeader {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(230px, 1fr));
  }

  .contentTable .rowPayment .textIcons a:hover {
    color: #1254ff;
  }

  .table thead .th-table {
    padding: 8px;
    font-size: 12px;
    color: #151317;
    background-clip: padding-box !important;
    text-align: left;
    border-right: 1px solid white;
  }

  .firstLine {
    background-color: #fff;
  }

  .secondLine {
    background-color: #eee;
  }

  .totalBalance {
    border-top: 1px solid #ddd;
    background-color: #e1ffb9;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 5px;

    .buyButton {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    p {
      font-size: 17px;
      margin: 0;
      font-weight: 700;
    }
  }

  .methodPayment {
    margin-top: 40px;
    display: flex;
    flex-direction: column;
    border: 1px solid #ddd;
    border-top-left-radius: 4px;
    border-top-right-radius: 4px;
    overflow: hidden;

    .header {
      background-color: #1254ff;
      color: white;
      margin: 0;
      padding: 10px;

      p {
        margin: 0;
        font-weight: 700;
      }
    }

    .info {
      padding: 10px;

      p {
        margin: 0;
        font-size: 14px;

        a {
          color: blue;
          cursor: pointer;
        }
      }
    }
  }

  .methodPayment .info ul li {
    margin: 0;
    font-size: 14px;
  }

  .skeletons {
    display: flex;
    gap: 60px;
    width: 100%;
    margin-bottom: 10px;
  }

  .skeleton {
    animation: skeleton-loading 1s linear infinite alternate;
  }

  .skeleton2 {
    animation: skeleton-loading2 1s linear infinite alternate;
  }

  .skeletonWidth {
    width: 100%;
    height: 350px;
  }

  @keyframes skeleton-loading {
    0% {
      background-color: hsl(200, 20%, 80%);
    }
    100% {
      background-color: hsl(200, 20%, 95%);
    }
  }
  @keyframes skeleton-loading2 {
    0% {
      background-color: hsl(200, 20%, 95%);
    }
    100% {
      background-color: hsl(200, 20%, 80%);
    }
  }

  @media (max-width: 880px) {
    .largeModalResponsive {
      width: 95vw;
    }

    .content {
    .buttonsModal {
      display: flex;
      justify-content: flex-end;
      gap: 10px;
    }

    .header {
      flex-direction: column;

      .title {
        font-size: 2rem;
      }
    }
  }

    .totalBalance {
      flex-direction: column;
      align-items: end;
      gap: 10px;

      .buyButton {
        display: flex;
        align-items: center;
        gap: 10px;
      }

      p {
        font-size: 17px;
        margin: 0;
        font-weight: 700;
      }
    }

    .contentModalFeeList {
      width: 350px;
      padding: 10px;
    }

    .filtersResponsive {
      padding: 10px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      width: 300px;
    }
  }
`;var Ps=Object.defineProperty,ks=Object.getOwnPropertyDescriptor,w=(t,e,i,o)=>{for(var s=o>1?void 0:o?ks(e,i):e,r=t.length-1,a;r>=0;r--)(a=t[r])&&(s=(o?a(e,i,s):a(s))||s);return o&&s&&Ps(e,i,s),s};let x=class extends T{constructor(){super(...arguments),this.showModal=!1,this.showModalFilters=!1,this.completionPayment=!1,this.isLoadTable=!0,this.dataListNotFormatted=[],this.dataList=[],this.showHead=!1,this.IsPaid=!0,this.showHeadMap=new Map,this.requestId=0,this.FeeIds=[],this.subTotal=0,this.selectedOptions=[],this.memberId=1024863,this.pagination={memberId:this.memberId,baseQuery:"",pageSize:20,pageNumber:1,sortField:"",sortOrder:"",totalPages:0,NumFound:0},this.vehicleId=0,this.saleType=0,this.sortBy="",this.sortAsc=!0,this.token="",this.servicesUrl="",this.selectedRows=[],this.theadDataChildTable=[{id:"-",label:"-"},{id:"FeeName",label:"Descrição cobrança"},{id:"state",label:"Situação"},{id:"DueDate",label:"Data Vencimento"},{id:"FeeAmount",label:"Valor"}]}calcularSomaTotalFeeAmount(t){let e=0;return t.forEach(i=>{e+=i.TotalFeeAmount}),L(e)}fetchData(){this.isLoadTable=!0,this.showModalFilters&&(this.showModalFilters=!1),I(`${this.servicesUrl}/G2OnlineServices/GetPendingPayments`,this.token,{memberId:this.memberId,pageSize:this.pagination.pageSize,pageNumber:this.pagination.pageNumber,vehicleId:this.vehicleId==0?0:this.vehicleId,saleType:this.saleType,sortBy:this.sortBy,sortOrder:this.sortAsc},t=>{this.isLoadTable=!1,this.pagination=this.pagination={...this.pagination,NumFound:t.pagination.NumFound,pageSize:t.pagination.pageSize,pageNumber:t.pagination.pageNumber,totalPages:t.pagination.totalPages},this.dataListNotFormatted=t.items,this.totalFeeAmount=this.calcularSomaTotalFeeAmount(t.items),this.dataList=t.items.map(e=>({...e,SaleDate:pt(e.SaleDate),OthersFeeAmount:L(e.OthersFeeAmount),TotalFeeAmount:L(e.TotalFeeAmount),DSALFeeAmount:L(e.DSALFeeAmount),BidAmount:L(e.BidAmount),ComissionFeeAmount:L(e.ComissionFeeAmount),VehicleSaleAmount:L(e.VehicleSaleAmount),InvoiceLink:e.InvoiceLink?h`<a href=${e.InvoiceLink} style="text-decoration:none"
                >Visualizar Boleto</a
              >`:null,Info:`${e.SaleTypeDescription}: ${this.renderSaleInfo(e)}`}))},()=>{})}renderSaleInfo(t){return t.SaleType==1?`${t.AuctionNumber} / ${t.LotOrder}`:`${t.BuyItNowId}`}PrintPendingPaymentsToPdf(){I(`${this.servicesUrl}/G2OnlineServices/PrintPendingPaymentsToPdf`,this.token,{items:this.dataListNotFormatted},t=>{if(t.resultCode===0&&t.content){const e=atob(t.content),i=new Array(e.length);for(let l=0;l<e.length;l++)i[l]=e.charCodeAt(l);const o=new Uint8Array(i),s=new Blob([o],{type:"application/pdf"}),r=URL.createObjectURL(s),a=new Date,n=String(a.getDate()).padStart(2,"0"),c=String(a.getMonth()+1).padStart(2,"0"),m=a.getFullYear(),p=document.createElement("a");p.style.display="none",p.href=r,p.download=`pagamentosPendentes${n}/${c}/${m}.pdf`,document.body.appendChild(p),p.click(),URL.revokeObjectURL(r),document.body.removeChild(p)}},()=>{})}ExportPendingPaymentsToExcel(){I(`${this.servicesUrl}/G2OnlineServices/ExportPendingPaymentsToExcel`,this.token,{items:this.dataListNotFormatted},t=>{if(t.resultCode===0&&t.content){const e=atob(t.content),i=new Array(e.length);for(let l=0;l<e.length;l++)i[l]=e.charCodeAt(l);const o=new Uint8Array(i),s=new Blob([o],{type:"application/vnd.ms-excel"}),r=URL.createObjectURL(s),a=new Date,n=String(a.getDate()).padStart(2,"0"),c=String(a.getMonth()+1).padStart(2,"0"),m=a.getFullYear(),p=document.createElement("a");p.style.display="none",p.href=r,p.download=`pagamentosPendentes${n}/${c}/${m}.xls`,document.body.appendChild(p),p.click(),URL.revokeObjectURL(r),document.body.removeChild(p)}},()=>{})}handleCompletionPayment(){this.completionPayment=!this.completionPayment}generateQrCode(){const t=[];this.selectedRows.forEach(e=>{e.selectedFees.forEach(i=>{t.push(...i.FeeId)})}),I(`${this.servicesUrl}/G2OnlineServices/RequestInvoice`,this.token,{feesIds:t,memberId:this.memberId},e=>{this.dataQrCode={...e.invoice,Items:e.Items},this.requestId=e.invoice.requestId,this.pagination.pageNumber=1,this.fetchData(),this.selectedRows=[],this.subTotal=0},()=>{})}handleOpenModal(){this.showModal=!this.showModal,this.showModal==!1&&this.pix.clearTime(),this.completionPayment=!1}handleOpenModalFilters(){this.showModalFilters=!this.showModalFilters}tHeadFormatted(){return window.innerWidth<880?[{label:"Código",id:"VehicleId",isSort:!0},{label:"Data da Venda",id:"SaleDate",isSort:!0},{label:"Descrição",id:"VehicleDescription"},{label:"Lance/Bem",id:"BidAmount"},{label:"Comissão",id:"ComissionFeeAmount"},{label:"DSAL/DSAP",id:"DSALFeeAmount"},{label:"Outros",id:"OthersFeeAmount"},{label:"Valor Devido",id:"TotalFeeAmount"},{label:"Tipo de Venda",id:"Info",isSort:!0},{label:"Boleto",id:"InvoiceLink"},{label:"",id:"Itens"}]:[{label:"Código",id:"VehicleId",isSort:!0},{label:"Data da Venda",id:"SaleDate",isSort:!0},{label:"Descrição",id:"VehicleDescription"},{label:"Lance/Bem",id:"BidAmount"},{label:"Comissão",id:"ComissionFeeAmount"},{label:"DSAL/DSAP",id:"DSALFeeAmount"},{label:"Outros",id:"OthersFeeAmount"},{label:"Valor Devido",id:"TotalFeeAmount"},{label:"Tipo de Venda",id:"Info",isSort:!0},{label:"Boleto",id:"InvoiceLink"},{label:"",id:"View"}]}formatDate(t){if(t==null)return"-";const e=new Date(t),i=String(e.getDate()).padStart(2,"0"),o=String(e.getMonth()+1).padStart(2,"0"),s=e.getFullYear();return`${i}/${o}/${s}`}theadDataModal(){return window.innerWidth<880?[{label:"Código",id:"VehicleId"},{label:"Tipo de Venda",id:"SaleTypeDescription"},{label:"Descrição",id:"VehicleDescription"},{label:"Valor",id:"TotalFeeAmount"},{label:"",id:"Detail"}]:[{label:"Código",id:"VehicleId"},{label:"Tipo de Venda",id:"SaleTypeDescription"},{label:"Descrição",id:"VehicleDescription"},{label:"Valor",id:"TotalFeeAmount"},{label:"",id:"View"}]}isChecked(t,e){return t.some(i=>e.FeeId.includes(i))}dataFeesList(t){var o;const e=[];return this.selectedRows.forEach(s=>{s.selectedFees.forEach(r=>{e.push(...r.FeeId)})}),(o=t==null?void 0:t.Fees)==null?void 0:o.map(s=>({"-":h`<input
        type="checkbox"
        value=${s.FeeAmount}
        @input=${r=>this.toggleCheckbox(r.target,t,s)}
        ?disabled=${!s.IsSelectable}
        .title=${s.IsSelectable?"":"Aguardando pagamento"}
        .checked=${this.isChecked(e,s)}
        class="checkbox"
      />`,FeeName:s.FeeName,state:h`<colibri-common-g2-badge
        .type=${s.IsSelectable?"blue":"warning"}
        .text=${s.IsSelectable?"Pendente":"Aguardando Pagamento"}
      ></colibri-common-g2-badge>`,DueDate:this.formatDate(s.DueDate),FeeAmount:L(s.FeeAmount)}))}async connectedCallback(){super.connectedCallback(),await super.updateComplete,this.fetchData(),this.GetMemberVehicleDocumentosFilters()}handleClick(t){this.dataList[t].Child==null?this.dataList[t]={...this.dataList[t],Child:this.childTable(this.dataList[t])}:this.dataList[t]={...this.dataList[t],Child:null},this.requestUpdate()}handleClickCheckout(t){this.selectedRows[t].Child==null?this.selectedRows[t]={...this.selectedRows[t],Child:this.tableSelectedFees(this.selectedRows[t].selectedFees)}:this.selectedRows[t]={...this.selectedRows[t],Child:null},this.requestUpdate()}async handleOnChangePagination(t,e){t==="pageSize"&&(this.pagination={...this.pagination,pageNumber:1}),this.pagination={...this.pagination,[t]:e},this.fetchData()}GetMemberVehicleDocumentosFilters(){pe(`${this.servicesUrl}/G2OnlineServices/GetMemberVehicleDocumentosFilters`,this.token,t=>{this.GetMemberVehicleDocumentosOptionsSaleType=t.SaleType.map(e=>({id:String(e.id),value:String(e.id),name:e.descricao})),this.GetMemberVehicleDocumentosOptionsSaleType.unshift({id:"0",value:"0",name:"Selecione uma opção"}),this.requestUpdate()},()=>{})}handleSortTable(t){const e=t.detail;this.sortAsc=e.sortAsc,this.sortBy=e.sortBy,this.fetchData()}filterModalResponsive(){return h`
      <g2-dialog
        .isOpen=${this.showModalFilters}
        title="Filtros"
        @on-close=${this.handleOpenModalFilters}
      >
        <div class="filtersResponsive">
          <colibri-common-g2-input
            class="input"
            isLabel="Código"
            @on-input=${t=>this.vehicleId=t.detail.value}
          ></colibri-common-g2-input>

          <colibri-common-g2-select
            class="input"
            isLabel="Tipo de venda"
            .isChildren=${this.GetMemberVehicleDocumentosOptionsSaleType}
            @on-input=${t=>this.saleType=t.detail.value}
          ></colibri-common-g2-select>

          <colibri-common-g2-button
            @onClick=${this.fetchData}
            radius="radius-sm"
            variant="dark"
            size="xs"
          >
            <ph-funnel-simple
              color="var(--gray-50)"
              weight="bold"
              size="18px"
            ></ph-funnel-simple>
            Filtrar
          </colibri-common-g2-button>
        </div>
      </g2-dialog>
    `}get formattedData(){return this.dataList.map((t,e)=>({...t,View:h` <style>
          .link {
            color: blue;
            cursor: pointer;
          }
        </style>
        <a
          class="link"
          @click=${()=>{window.innerWidth<880?console.log(""):this.handleClick(e)}}
          >Visualizar</a
        >`,Child:t.Child,Itens:h` <colibri-common-g2-table-default
        .theadData=${this.theadDataChildTable}
        .tbodyData=${this.dataFeesList(t)}
      ></colibri-common-g2-table-default>`}))}render(){var t,e,i,o,s,r;return h`
      <g2-dialog
        .isOpen=${this.showModal}
        title="Pagamentos"
        @on-close=${this.handleOpenModal}
      >
        <div class="content padding largeModalResponsive">
          ${this.completionPayment?h`<qrcode-visualizer
                id="pix"
                .servicesUrl=${this.servicesUrl}
                .token=${this.token}
                .dataQrCode=${this.dataQrCode}
                .requestId=${(t=this.dataQrCode)==null?void 0:t.requestId}
                .cancelRequest=${!0}
                .memberId=${this.memberId}
                @my-close-modal=${this.handleOpenModal}
              ></qrcode-visualizer>`:this.modalList()}

          <div class="buttonsModal">
            ${this.completionPayment?null:h`<button
                  class="button"
                  @click=${()=>{this.handleCompletionPayment(),this.generateQrCode()}}
                >
                  Finalizar pagamento
                </button>`}
          </div>
        </div>
      </g2-dialog>

      ${this.filterModalResponsive()}

      <div class="content">
        <div class="header">
          <h2 class="title">Pagamentos Pendentes</h2>

          <div class="header-actions">
            <button
              class="button-print"
              @click=${this.ExportPendingPaymentsToExcel}
            >
              <ph-cloud-arrow-down
                color="var(--gray-600)"
                size="16px"
                weight="bold"
              ></ph-cloud-arrow-down>
              Exportar
            </button>

            <button
              class="button-print"
              @click=${this.PrintPendingPaymentsToPdf}
            >
              <ph-printer
                color="var(--gray-600)"
                size="16px"
                weight="bold"
              ></ph-printer>
              Imprimir
            </button>
          </div>
        </div>
        <div class="contentTable">
          <div class="rowPayment">
            <p>Faturas Totais (${this.pagination.NumFound})</p>
          </div>

          <colibri-common-g2-button
            @onClick=${this.handleOpenModalFilters}
            class="responsiveButton"
            radius="radius-sm"
            variant="dark"
            size="xs"
          >
            <ph-funnel-simple
              color="var(--gray-50)"
              weight="bold"
              size="18px"
            ></ph-funnel-simple>
            Opções de filtro
          </colibri-common-g2-button>

          <div class="border">
            <div class="filters">
              <colibri-common-g2-input
                class="input"
                isLabel="Código"
                @on-input=${a=>this.vehicleId=a.detail.value}
              ></colibri-common-g2-input>

              <colibri-common-g2-select
                class="input"
                isLabel="Tipo de venda"
                .isChildren=${this.GetMemberVehicleDocumentosOptionsSaleType}
                @on-input=${a=>this.saleType=a.detail.value}
              ></colibri-common-g2-select>

              <colibri-common-g2-button
                @onClick=${this.fetchData}
                radius="radius-sm"
                variant="dark"
                size="xs"
              >
                <ph-funnel-simple
                  color="var(--gray-50)"
                  weight="bold"
                  size="18px"
                ></ph-funnel-simple>
                Filtrar
              </colibri-common-g2-button>
            </div>

            <div class="pagination">
              <colibri-common-g2-pagination
                limit=${(e=this.pagination)==null?void 0:e.pageSize}
                total=${(i=this.pagination)==null?void 0:i.totalPages}
                offset=${(o=this.pagination)==null?void 0:o.pageNumber}
                @my-page-changed=${a=>this.handleOnChangePagination("pageNumber",a.detail.current)}
                @row-per-page=${a=>this.handleOnChangePagination("pageSize",a.detail)}
              ></colibri-common-g2-pagination>
            </div>

            <colibri-common-g2-table-default
              .load=${this.isLoadTable}
              isSort
              .sortBy=${this.sortBy}
              .theadData=${this.tHeadFormatted()}
              .tbodyData=${this.formattedData}
              type="alternate"
              @my-sortBy=${a=>this.handleSortTable(a)}
            ></colibri-common-g2-table-default>

            <div class="pagination">
              <colibri-common-g2-pagination
                limit=${(s=this.pagination)==null?void 0:s.pageSize}
                total=${(r=this.pagination)==null?void 0:r.totalPages}
                offset=${this.pagination.pageNumber}
                @my-page-changed=${a=>this.handleOnChangePagination("pageNumber",a.detail.current)}
                @row-per-page=${a=>this.handleOnChangePagination("pageSize",a.detail)}
              ></colibri-common-g2-pagination>
            </div>
          </div>

          <div class="totalBalance">
            <p>Saldo total devido: ${this.totalFeeAmount}</p>

            <div class="buyButton">
              <p>Subtotal: ${L(this.subTotal)}</p>
              <colibri-common-g2-button
                variant="default"
                ?isDisabled=${this.selectedRows.length<1}
                @click=${this.handleOpenModal}
              >
                Realizar Pagamento
              </colibri-common-g2-button>
            </div>
          </div>
        </div>

        <div class="methodPayment">
          <div class="header">
            <p>Formas de Pagamento</p>
          </div>

          <div class="info">
            <p>
              Copart do Brasil oferece várias formas de pagamento. Escolha entre
              os seguintes métodos:
            </p>
            <ul>
              <li>
                Boleto, TED e transferência interbancária para quitação da
                compra de veículos;
              </li>
              <li>Pix para quitação de taxas de serviços;</li>
              <li>Para visualizar os pagamentos, acesse Meus Pagamentos;</li>
            </ul>

            <p>
              Para mais informações de como pagar, consulte a seção Pagamento e
              Retirada do Veículo na nossa página de Como Comprar. Se você tiver
              alguma dúvida, por favor, envie-nos um e-mail para
              faleconosco@copart.com.br.
            </p>
          </div>
        </div>
      </div>
    `}childTable(t){return h`
      <style>
        .anotherName {
          display: flex;
          flex-direction: row;
          border: 1px solid #d0d0d0;
          justify-content: space-between;
          padding: 10px;
          gap: 20px;
          border-radius: 4px;

          .logo {
            height: 200px;
            width: 250px;
            object-fit: cover;
            border-radius: 6px;
          }

          .column {
            display: flex;
            flex-direction: column;
            margin-top: 28px;

            &.none {
              margin-top: 0;
            }

            .invoice {
              display: flex;
              align-items: center;
              gap: 10px;
              background: #c8e5ff;
              padding: 6px 10px;
              border-radius: 4px;
              color: #1254ff;
              font-size: 14px;
              cursor: pointer;
            }

            a {
              font-size: 22px;
              font-weight: 900;
              color: #1254ff;
              text-decoration: underline;
            }

            p {
              font-weight: 500;
              font-size: 14px;
              margin-block: 4px;
            }
          }

          .tableChild {
            width: 40%;
          }
        }
      </style>
      <tr>
        <td colspan="11">
          <div class="anotherName">
            <img class="logo" src=${t.VehiclePic} />
            <div class="column none">
              <a>${t.VehicleDescription}</a>
              <div>
                <p>Descrição:</p>
                <p>${t.ModelDescription}</p>
              </div>
              <div>
                <p>Chassi:</p>
                <p>${t.Vin}</p>
              </div>
              <div>
                <p>Tipo chassi:</p>
                <p>${t.VinType}</p>
              </div>
            </div>

            <div class="column">
              <div>
                <p>Tipo de monta:</p>
                <p>${t.DamageType}</p>
              </div>
              <div>
                <p>Tipo de documento:</p>
                <p>${t.TitleType}</p>
              </div>
              <div>
                <p>Chaves:</p>
                <p>${t.HasKeys?"Sim":"Não"}</p>
              </div>
            </div>

            <div class="column">
              <div>
                <p>Data da Venda:</p>
                <p>${t.SaleDate}</p>
              </div>
              ${t.InvoiceLink?h`<a
                    href=${t.InvoiceLink.values[0]}
                    class="invoice"
                    style="text-decoration:none"
                  >
                    <ph-paperclip
                      color="#1254ff"
                      weight="bold"
                      size="18px"
                    ></ph-paperclip>
                    Boleto</a
                  >`:null}
            </div>

            <div class="tableChild">
              <colibri-common-g2-table-default
                .theadData=${this.theadDataChildTable}
                .tbodyData=${this.dataFeesList(t)}
              ></colibri-common-g2-table-default>
            </div>
          </div>
        </td>
      </tr>
    `}calculateTotal(t){return t.selectedFees.reduce((e,i)=>e+i.FeeAmount,0)}formatSelectedRows(){return this.selectedRows.map((e,i)=>({VehicleId:e.VehicleId,SaleTypeDescription:`${e.SaleTypeDescription}: ${this.renderSaleInfo(e)}`,VehicleDescription:e.VehicleDescription,BuyItNowId:e.BuyItNowId,LotOrder:e.LotOrder,AuctionNumber:e.AuctionNumber,TotalFeeAmount:L(this.calculateTotal(e)),View:h`<a
        style="cursor:pointer; color:blue;"
        @click=${()=>this.handleClickCheckout(i)}
        >Visualizar</a
      >`,Child:e.Child,Detail:this.tableSelectedFees(e.selectedFees)}))}modalList(){return h`
      <p>Carrinho (${this.selectedRows.length})</p>

      <colibri-common-g2-table-default
        .theadData=${this.theadDataModal()}
        .tbodyData=${this.formatSelectedRows()}
      >
      </colibri-common-g2-table-default>

      <p class="totalPayment">
        Total a pagar: R$ ${L(this.subTotal)}
      </p>
    `}tableSelectedFees(t){const e=t.map(i=>({FeeAmount:L(i.FeeAmount),FeeName:i.FeeName}));if(window.innerWidth>880)return h`
        <tr>
          <td colspan=${this.theadDataModal().length}>
            <colibri-common-g2-table-default
              .theadData=${[{label:"Descrição cobrança",id:"FeeName"},{label:"Valor",id:"FeeAmount"}]}
              .tbodyData=${e}
            >
            </colibri-common-g2-table-default>
          </td>
        </tr>
      `}toggleCheckbox(t,e,i){const o=parseFloat(t.value);if(t.checked)this.selectedOptions.push(o),this.selectedRows.some(s=>s.VehicleId==e.VehicleId)?this.selectedRows.find(s=>s.VehicleId==e.VehicleId).selectedFees.push(i):this.selectedRows.push({...e,selectedFees:[i]}),this.subTotal+=o;else{this.subTotal-=o;const s=this.selectedRows.find(r=>r.VehicleId===e.VehicleId);s&&(s.selectedFees=s.selectedFees.filter(r=>r!==i),s.selectedFees.length===0&&(this.selectedRows=this.selectedRows.filter(r=>r.VehicleId!==e.VehicleId)))}this.subTotal=parseFloat(this.subTotal.toFixed(2)),this.requestUpdate()}};x.styles=[Ss],w([Ee("#pix")],x.prototype,"pix",2),w([u()],x.prototype,"showModal",2),w([u()],x.prototype,"showModalFilters",2),w([u()],x.prototype,"completionPayment",2),w([u()],x.prototype,"isLoadTable",2),w([u()],x.prototype,"rowModalData",2),w([u()],x.prototype,"dataListNotFormatted",2),w([u()],x.prototype,"dataList",2),w([u()],x.prototype,"showHead",2),w([u()],x.prototype,"IsPaid",2),w([u()],x.prototype,"showHeadMap",2),w([u()],x.prototype,"requestId",2),w([u()],x.prototype,"FeeIds",2),w([u()],x.prototype,"visibleRows",2),w([u()],x.prototype,"subTotal",2),w([u()],x.prototype,"selectedOptions",2),w([u()],x.prototype,"dataQrCode",2),w([b()],x.prototype,"memberId",2),w([u()],x.prototype,"pagination",2),w([u()],x.prototype,"vehicleId",2),w([u()],x.prototype,"GetMemberVehicleDocumentosOptionsSaleType",2),w([u()],x.prototype,"saleType",2),w([b({type:String})],x.prototype,"sortBy",2),w([u()],x.prototype,"sortAsc",2),w([b({type:String})],x.prototype,"token",2),w([b()],x.prototype,"servicesUrl",2),x=w([R("payment-pending")],x);const As=_`
  .toast {
    position: absolute;
    right: 0;
    top: 0;
    margin: 30px;
    overflow: hidden;

    background-color: #9bf0bd;
    height: auto;
    width: 150px;
    padding: 12px;
    border-radius: 8px;
  }
`;var Ds=Object.defineProperty,Es=Object.getOwnPropertyDescriptor,Ts=(t,e,i,o)=>{for(var s=o>1?void 0:o?Es(e,i):e,r=t.length-1,a;r>=0;r--)(a=t[r])&&(s=(o?a(e,i,s):a(s))||s);return o&&s&&Ds(e,i,s),s};let ui=class extends T{static get styles(){return[As]}render(){return h`
      <div class="toast" id="toast">
        <div>
          <strong>Copiado para area de transferência</strong>
        </div>
      </div>
    `}handleOnModalCard(){const t=new CustomEvent("my-close-modal");this.dispatchEvent(t)}};ui=Ts([R("toast-copy-paste")],ui);const Os=_`
  :root {
    /* scroll */
    --scrollbar-size: 10px;

    /* Colors */
    --gray-25: #fcfcfd;
    --gray-50: #f9fafb;
    --gray-100: #f2f4f7;
    --gray-200: #eaecf0;
    --gray-300: #d0d5dd;
    --gray-400: #98a2b3;
    --gray-500: #667085;
    --gray-600: #475467;
    --gray-700: #344054;
    --gray-800: #1d2939;
    --gray-900: #101828;

    /* Primary-Color */
    --blue-50: #eaf2ff;
    --blue-100: #d5e5ff;
    --blue-200: #a6c8ff;
    --blue-300: #77abff;
    --blue-400: #489eff;
    --blue-500: #1254ff; /* Base */
    --blue-600: #0041cc;
    --blue-700: #003199;
    --blue-800: #002066;
    --blue-900: #001033;

    /* Error-Color */
    --error-50: #ffe8e0;
    --error-100: #ffd1c1;
    --error-200: #ffa392;
    --error-300: #ff7c63;
    --error-400: #ff5534;
    --error-500: #f76120;
    --error-600: #c23e18;
    --error-700: #911a0f;
    --error-800: #5f0e08;
    --error-900: #2e0704;

    /* Warning-Color */
    --yellow-50: #fff8e1;
    --yellow-100: #fff0c2;
    --yellow-200: #ffe999;
    --yellow-300: #ffdb70;
    --yellow-400: #ffce47;
    --yellow-500: #ffb838; /* Base */
    --yellow-600: #cc971f;
    --yellow-700: #996e15;
    --yellow-800: #66460c;
    --yellow-900: #332306;

    /*  Success-Color */
    --success-50: #e5f4e0;
    --success-100: #c9e9c1;
    --success-200: #9edf99;
    --success-300: #73d471;
    --success-400: #47c948;
    --success-500: #238202; /* Base */
    --success-600: #1a6300;
    --success-700: #113f00;
    --success-800: #092600;
    --success-900: #040d00;

    /* Warning-Color */
    --warning-25: #fffcf5;
    --warning-50: #fffaeb;
    --warning-100: #fef0c7;
    --warning-200: #fedf89;
    --warning-300: #fec84b;
    --warning-400: #fdb022;
    --warning-500: #f79009;
    --warning-600: #dc6803;
    --warning-700: #b54708;
    --warning-800: #93370d;
    --warning-900: #7a2e0e;

    /* Fonts */
    --body-font: 'Red Hat Display', sans-serif;
    --text-small-xs: 0.75rem; /* 12px */
    --text-small-sm: 0.875rem; /* 14px */
    --text-small-md: 1rem; /* 16px */
    --text-small-lg: 1.125rem; /* 18px */
    --text-small-xl: 1.25rem; /* 20px */
    --text-headline-sm: 1.5rem; /* 24px */
    --text-headline-md: 1.75rem; /* 28px */
    --text-headline-lg: 2.187rem; /* 35px */
    --text-display-sm: 3rem; /* 48px */
    --text-display-md: 3.75rem; /* 60px */
    --text-display-lg: 4.5rem; /* 72px */

    /* Font weight */
    --weight-light: 300;
    --weight-regular: 400;
    --weight-medium: 500;
    --weight-semibold: 600;
    --weight-bold: 700;
    --weight-extrabold: 800;
  }

  .content {
    .title {
      color: #1254ff;
      font-weight: bolder;
      font-family: 'Red Hat Display', sans-serif;
      font-size: 3rem;
      padding: 0px;
      margin: 0px;
    }

    .header {
      display: flex;
      justify-content: space-between;
      align-items: center;

      .header-actions {
        display: flex;
        align-items: center;
        gap: 12px;

        .button-print {
          display: flex;
          align-items: center;
          gap: 6px;
          font-size: var(--text-small-sm);
          font-weight: var(--weight-semibold);
          color: var(--gray-700);
          background-color: transparent;
          border: none;
          font-family: inherit;
          cursor: pointer;

          &:hover {
            color: var(--blue-600);
            text-decoration: underline;
          }
        }
      }
    }

    .border {
      border: 1px solid #ddd;
      border-radius: 6px;
    }

    .filters {
      display: flex;
      justify-content: flex-start;
      align-items: flex-end;
      gap: 20px;
      margin-top: 10px;
      margin-left: 5px;

      .input {
        width: 200px;
      }
    }
  }

  .expandChildTable::before {
    display: block;
    cursor: pointer;
  }

  .buttonsModal {
    display: flex;
    justify-content: flex-end;
    gap: 10px;
  }

  .totalPayment {
    text-align: end;
  }

  .button {
    background-color: #ffb838;
    border-radius: 4px;
    padding: 8px 16px;
    color: black;
    font-weight: 600;
    border: none;
    cursor: pointer;
    font-family: 'Red Hat Display';

    &:disabled {
      background-color: #eba930;
      cursor: not-allowed;
    }
  }

  .completionPayment {
    display: flex;
    justify-content: space-around;
    align-items: center;
  }

  .completionPayment .card {
    width: 400px;
    display: flex;
    flex-direction: column;
    border-radius: 4px;
    border: 1px solid #dfdfdf;
    height: 360px;

    p:nth-of-type(even) {
      text-align: right;
    }
  }

  .completionPayment .card .cardInfos {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    padding: 15px;
    gap: 15px;
  }

  .modal-tbody {
    display: flex;
    flex-direction: column;
    gap: 10px;

    .pagination {
      margin-inline-end: 5px;
    }
  }

  .Skeletons-tbody {
    display: flex;
    flex-direction: column;
  }

  .skeletonItem {
    width: 100%;
    height: 20px;
  }

  .tr {
    display: grid;
    grid-template-columns: repeat(7, 1fr);
  }

  .thead-td {
    background-color: #dfdfdf;
    padding: 10px;
    font-weight: bold;
    font-size: 12px;
  }

  .modal-td {
    font-size: 12px;
    padding: 4px 10px;
    color: black;
  }

  .td {
    font-size: 12px;
    padding: 4px 10px;
    color: black;
  }

  .qrCodeImage {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 10px;
    margin-bottom: 20px;

    textarea {
      width: 320px;
      resize: none;
      border-radius: 4px;
      border: 1px solid #dfdfdf;
      font-family: 'Red Hat Display', sans-serif !important;
      cursor: pointer;
    }

    img {
      height: 300px;
      width: 100%;
      border: 1px solid #dfdfdf;
      border-radius: 4px;
    }

    .pix {
      display: flex;
      flex-direction: column;
      align-items: center;

      p {
        display: flex;
        align-items: center;
        gap: 5px;
      }
    }
  }

  .checkbox {
    cursor: pointer;

    &:disabled {
      cursor: not-allowed;
    }
  }

  .theadFees {
    background-color: #ddd;
  }

  .widthTd {
    min-width: 100px;
  }

  .contentTable .rowPayment {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-inline: 2px;
  }

  .contentTable .rowPayment p {
    font-size: 13px;
    font-weight: 700;
  }

  .contentTable .rowPayment .textIcons {
    display: flex;
    /* align-items: center; */
    gap: 12px;
  }

  .contentTable .rowPayment .textIcons a {
    display: flex;
    align-items: flex-end;
    gap: 4px;
    font-weight: 700;
    font-size: 12px;
    cursor: pointer;
  }

  .align {
    display: flex;
    justify-content: center;
  }

  .none {
    display: none;
  }

  .childTableRow {
    border: 1px solid #d0d0d0;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    padding: 10px;
    gap: 20px;

    .logo {
      height: 200px;
      width: 200px;
      object-fit: cover;
    }
  }

  .childTableRow .column {
    display: flex;
    flex-direction: column;
    margin-top: 28px;

    &.none {
      margin-top: 0;
    }

    .invoice {
      display: flex;
      align-items: center;
      gap: 10px;
      background: #c8e5ff;
      padding: 6px 10px;
      border-radius: 4px;
      color: #1254ff;
      font-size: 14px;
      cursor: pointer;
    }

    a {
      font-size: 22px;
      font-weight: 900;
      color: #1254ff;
      text-decoration: underline;
    }

    p {
      font-weight: bolder;
      font-size: 14px;
      margin-block: 4px;
    }
  }

  .childTableRowTr {
    display: grid;
    grid-template-columns: 50px repeat(auto-fill, minmax(230px, 1fr));
    border: 1px solid #d0d0d0;
    width: 600px;
    background-color: white;

    .bold {
      font-weight: bold;
      text-align: center;
    }

    .amount {
      text-align: right;
    }
  }

  .contentChildrenTable {
    padding: 10px;
  }

  .childTableRowTrTable {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(230px, 1fr));
    border: 1px solid #d0d0d0;
    width: 600px;
    background-color: white;
  }

  .contentTable .rowPayment .textIcons a:hover {
    color: #1254ff;
  }

  .totalBalance {
    border-top: 1px solid #ddd;
    background-color: #e1ffb9;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 5px;
  }

  .totalBalance .buyButton {
    display: flex;
    align-items: center;
    gap: 10px;
  }

  .totalBalance p {
    font-size: 17px;
    margin: 0;
    font-weight: 700;
  }

  .methodPayment {
    margin-top: 40px;
    display: flex;
    flex-direction: column;
    border: 1px solid #ddd;
    border-top-left-radius: 4px;
    border-top-right-radius: 4px;
    overflow: hidden;
  }

  .methodPayment .header {
    background-color: #1254ff;
    color: white;
    margin: 0;
    padding: 10px;
  }

  .methodPayment .header p {
    margin: 0;
    font-weight: 700;
  }

  .methodPayment .info {
    padding: 10px;
  }

  .methodPayment .info p {
    margin: 0;
    font-size: 14px;
  }

  .methodPayment .info p a {
    color: blue;
    cursor: pointer;
  }

  .methodPayment .info ul li {
    margin: 0;
    font-size: 14px;
  }

  .copied-message {
    position: fixed;
    top: 20px;
    left: 50%;
    transform: translateX(-50%);
    background-color: #4caf50;
    color: white;
    padding: 15px;
    border-radius: 5px;
    font-size: 16px;
    z-index: 9999;
    display: none;
  }

  .skeletons {
    display: flex;
    gap: 60px;
    width: 100%;
    margin-bottom: 10px;
  }

  .skeleton {
    animation: skeleton-loading 1s linear infinite alternate;
  }

  .skeleton2 {
    animation: skeleton-loading2 1s linear infinite alternate;
  }

  .skeletonWidth {
    width: 100%;
    height: 350px;
  }

  .responsiveButton {
    display: none;
  }

  @keyframes skeleton-loading {
    0% {
      background-color: hsl(200, 20%, 80%);
    }
    100% {
      background-color: hsl(200, 20%, 95%);
    }
  }
  @keyframes skeleton-loading2 {
    0% {
      background-color: hsl(200, 20%, 95%);
    }
    100% {
      background-color: hsl(200, 20%, 80%);
    }
  }

  @media (max-width: 880px) {
    .content {
      .header {
        flex-direction: column;

        .title {
          font-size: 2rem;
        }
      }

      .filters {
        display: none;
      }
    }

    .responsiveButton {
      display: block;
      margin-block: 10px;
    }

    .filtersResponsive {
      padding: 10px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      width: 300px;
    }
  }
`;var Is=Object.defineProperty,Fs=Object.getOwnPropertyDescriptor,D=(t,e,i,o)=>{for(var s=o>1?void 0:o?Fs(e,i):e,r=t.length-1,a;r>=0;r--)(a=t[r])&&(s=(o?a(e,i,s):a(s))||s);return o&&s&&Is(e,i,s),s};let P=class extends T{constructor(){super(...arguments),this.showModal=!1,this.isLoadTable=!1,this.titleModal="",this.showHead=!1,this.showHeadMap=new Map,this.vehicleId=0,this.statusId=0,this.PaymentsHistoryOption=[],this.memberId=1024863,this.pagination={memberId:this.memberId,baseQuery:"",pageSize:20,pageNumber:1,sortField:"",sortOrder:"",totalPages:0,NumFound:0},this.token="",this.servicesUrl="",this.selectedRows=[],this.theadData=[{label:"Identificação",id:"ServiceNumber"},{label:"Data de emissão",id:"CreationDateStr"},{label:"Status",id:"PaymentStatus"},{label:"Data de vencimento",id:"DueDateStr"},{label:"Data do pagamento",id:"PaymentDateStr"},{label:"Valor",id:"SaleValue"},{label:"",id:"view"}],this.subTotal=0,this.selectedOptions=[]}formatDataList(t){const e=o=>{let s;switch(o){case 1:s="warning";break;case 2:s="gray";break;case 3:s="error";break;case 4:s="yellow";break;default:s="gray"}return s};return t.items.map(o=>({...o,CreationDateStr:this.formatDate(o.CreationDate),PaymentDateStr:this.formatDate(o.PaymentDate),DueDateStr:this.formatDate(o.DueDate),SaleValue:this.formatMoney(o.SaleValue),PaymentStatus:h` <colibri-common-g2-badge
        type=${e(o.PaymentStatusID)}
        size="sm"
        text=${o.PaymentStatus}
      ></colibri-common-g2-badge>`,view:h`<a
        style="color: #1254ff; cursor: pointer;"
        @click=${()=>{this.dataQrCode={creationDate:o.CreationDate,dueDate:o.DueDate,copyPaste:o.CopyPaste,qrcode:o.QRCode,requestId:o.RequestId,requestAmount:o.RequestAmount,PaymentStatusID:o.PaymentStatusID,Items:o.Items},this.handleOpenModal()}}
        >Visualizar</a
      >`}))}fetchData(){this.showModalFilters&&(this.showModalFilters=!1),this.isLoadTable=!0,I(`${this.servicesUrl}/G2OnlineServices/GetPaymentHistory`,this.token,{memberId:this.memberId,pageSize:this.pagination.pageSize,pageNumber:this.pagination.pageNumber,vehicleId:this.vehicleId==0?0:this.vehicleId,statusId:this.statusId},t=>{this.isLoadTable=!1,this.dataListNotFormatted=t.items,this.dataList=this.formatDataList(t),this.pagination=this.pagination={...this.pagination,NumFound:t.pagination.NumFound,pageSize:t.pagination.pageSize,pageNumber:t.pagination.pageNumber,totalPages:t.pagination.totalPages},this.requestUpdate()},()=>{})}GetPaymentsHistoryFilters(){pe(`${this.servicesUrl}/G2OnlineServices/GetPaymentsHistoryFilters`,this.token,t=>{this.PaymentsHistoryOption=t.Filters.map(e=>({id:String(e.id),value:String(e.id),name:e.descricao})),this.PaymentsHistoryOption.unshift({id:"0",value:"0",name:"Selecione uma opção"}),this.requestUpdate()},()=>{})}handleOpenModal(){this.titleModalChange(),this.showModal=!this.showModal,this.showModal==!1&&(this.pix.clearTime(),this.fetchData()),this.requestUpdate()}formatDate(t){if(t==null)return"";const e=new Date(t),i=String(e.getDate()).padStart(2,"0"),o=String(e.getMonth()+1).padStart(2,"0"),s=e.getFullYear();return`${i}/${o}/${s}`}formatMoney(t){return new Intl.NumberFormat("pt-BR",{style:"currency",currency:"BRL"}).format(t)}handleOpenModalFilters(){this.showModalFilters=!this.showModalFilters}filterModalResponsive(){return h`
      <g2-dialog
        .isOpen=${this.showModalFilters}
        title="Filtros"
        @on-close=${this.handleOpenModalFilters}
      >
        <div class="filtersResponsive">
          <colibri-common-g2-input
            class="input"
            isLabel="Código Veículo"
            @on-input=${t=>this.vehicleId=t.detail.value}
          ></colibri-common-g2-input>

          <colibri-common-g2-select
            class="input"
            isLabel="Status"
            .isChildren=${this.PaymentsHistoryOption}
            @on-input=${t=>this.statusId=t.detail.value}
          ></colibri-common-g2-select>

          <colibri-common-g2-button
            @onClick=${this.fetchData}
            radius="radius-sm"
            variant="dark"
            size="xs"
          >
            <ph-funnel-simple
              color="var(--gray-50)"
              weight="bold"
              size="18px"
            ></ph-funnel-simple>
            Filtrar
          </colibri-common-g2-button>
        </div>
      </g2-dialog>
    `}async connectedCallback(){super.connectedCallback(),await super.updateComplete,this.fetchData(),this.GetPaymentsHistoryFilters()}PrintPaymentRequestsToPdf(){I(`${this.servicesUrl}/G2OnlineServices/PrintPaymentRequestsToPdf`,this.token,{items:this.dataListNotFormatted},t=>{if(t.resultCode===0&&t.content){const e=atob(t.content),i=new Array(e.length);for(let l=0;l<e.length;l++)i[l]=e.charCodeAt(l);const o=new Uint8Array(i),s=new Blob([o],{type:"application/pdf"}),r=URL.createObjectURL(s),a=new Date,n=String(a.getDate()).padStart(2,"0"),c=String(a.getMonth()+1).padStart(2,"0"),m=a.getFullYear(),p=document.createElement("a");p.style.display="none",p.href=r,p.download=`meusPagamentos${n}/${c}/${m}.pdf`,document.body.appendChild(p),p.click(),URL.revokeObjectURL(r),document.body.removeChild(p)}},()=>{})}ExportPaymentRequestsToExcel(){I(`${this.servicesUrl}/G2OnlineServices/ExportPaymentRequestsToExcel`,this.token,{items:this.dataListNotFormatted},t=>{if(t.resultCode===0&&t.content){const e=atob(t.content),i=new Array(e.length);for(let l=0;l<e.length;l++)i[l]=e.charCodeAt(l);const o=new Uint8Array(i),s=new Blob([o],{type:"application/vnd.ms-excel"}),r=URL.createObjectURL(s),a=new Date,n=String(a.getDate()).padStart(2,"0"),c=String(a.getMonth()+1).padStart(2,"0"),m=a.getFullYear(),p=document.createElement("a");p.style.display="none",p.href=r,p.download=`meusPagamentos${n}/${c}/${m}.xls`,document.body.appendChild(p),p.click(),URL.revokeObjectURL(r),document.body.removeChild(p)}},()=>{})}handleOnParams(t){this.pagination.pageNumber=t,this.fetchData()}handlePaginationSize(t){this.pagination.pageSize=t,this.fetchData()}titleModalChange(){this.dataQrCode.PaymentStatusID==2?this.titleModal="Pagamento Realizado":this.dataQrCode.PaymentStatusID==3?this.titleModal="Pagamento Cancelado":this.dataQrCode.PaymentStatusID==4?this.titleModal="Pagamento Expirado":(this.titleModal="Aguardando Pagamento",this.messageModal&&(this.titleModal="Aviso"))}updated(t){super.updated(t),t.has("messageModal")&&this.titleModalChange()}render(){var t,e,i,o,s,r,a;return h`
      <div id="copiedMessage" class="copied-message">
        Texto copiado com sucesso!
      </div>

      <g2-dialog
        .isOpen=${this.showModal}
        title=${this.titleModal}
        @on-close=${this.handleOpenModal}
      >
        ${this.showModal?h`<qrcode-visualizer
              id="pix"
              .dataQrCode=${this.dataQrCode}
              .token=${this.token}
              .servicesUrl=${this.servicesUrl}
              .requestId=${(t=this.dataQrCode)==null?void 0:t.requestId}
              .cancelRequest=${!0}
              .memberId=${this.memberId}
              @my-close-modal=${this.handleOpenModal}
              @message-callback=${n=>this.messageModal=n.detail}
            ></qrcode-visualizer>`:null}
      </g2-dialog>

      ${this.filterModalResponsive()}

      <div class="content">
        <div class="header">
          <h2 class="title">Meus Pagamentos</h2>

          <div class="header-actions">
            <button
              class="button-print"
              @click=${this.PrintPaymentRequestsToPdf}
            >
              <ph-cloud-arrow-down
                color="var(--gray-600)"
                size="16px"
                weight="bold"
              ></ph-cloud-arrow-down>
              Exportar
            </button>

            <button
              class="button-print"
              @click=${this.ExportPaymentRequestsToExcel}
            >
              <ph-printer
                color="var(--gray-600)"
                size="16px"
                weight="bold"
              ></ph-printer>
              Imprimir
            </button>
          </div>
        </div>
        <div class="contentTable">
          <div class="rowPayment">
            <p>Faturas Totais (${this.pagination.NumFound})</p>
          </div>

          <colibri-common-g2-button
            @onClick=${this.handleOpenModalFilters}
            class="responsiveButton"
            radius="radius-sm"
            variant="dark"
            size="xs"
          >
            <ph-funnel-simple
              color="var(--gray-50)"
              weight="bold"
              size="18px"
            ></ph-funnel-simple>
            Opções de filtro
          </colibri-common-g2-button>

          <div class="border">
            <div class="filters">
              <colibri-common-g2-input
                class="input"
                isLabel="Código Veículo"
                @on-input=${n=>this.vehicleId=n.detail.value}
              ></colibri-common-g2-input>

              <colibri-common-g2-select
                class="input"
                isLabel="Status"
                .isChildren=${this.PaymentsHistoryOption}
                @on-input=${n=>this.statusId=n.detail.value}
              ></colibri-common-g2-select>

              <colibri-common-g2-button
                @onClick=${this.fetchData}
                radius="radius-sm"
                variant="dark"
                size="xs"
              >
                <ph-funnel-simple
                  color="var(--gray-50)"
                  weight="bold"
                  size="18px"
                ></ph-funnel-simple>
                Filtrar
              </colibri-common-g2-button>
            </div>

            <div class="modal-tbody">
              <div class="pagination">
                <colibri-common-g2-pagination
                  limit=${(e=this.pagination)==null?void 0:e.pageSize}
                  total=${(i=this.pagination)==null?void 0:i.totalPages}
                  offset=${(o=this.pagination)==null?void 0:o.pageNumber}
                  @my-page-changed=${n=>this.handleOnParams(n.detail.current)}
                  @row-per-page=${n=>this.handlePaginationSize(n.detail)}
                ></colibri-common-g2-pagination>
              </div>

              ${this.isLoadTable?h`
                    <colibri-common-g2-load-table></colibri-common-g2-load-table>
                  `:h`<colibri-common-g2-table-default
                    .theadData=${this.theadData}
                    .tbodyData=${this.dataList}
                    type="alternate"
                  ></colibri-common-g2-table-default>`}

              <div class="pagination">
                <colibri-common-g2-pagination
                  limit=${(s=this.pagination)==null?void 0:s.pageSize}
                  total=${(r=this.pagination)==null?void 0:r.totalPages}
                  offset=${(a=this.pagination)==null?void 0:a.pageNumber}
                  @my-page-changed=${n=>this.handleOnParams(n.detail.current)}
                  @row-per-page=${n=>this.handlePaginationSize(n.detail)}
                ></colibri-common-g2-pagination>
              </div>
            </div>
          </div>
        </div>

        <div class="methodPayment">
          <div class="header">
            <p>Informações</p>
          </div>

          <div class="info">
            <p>
              Acima você pode acessar os pagamentos gerados sobre itens da
              página de Pagamentos Pendentes. Atente-se para:
            </p>
            <ul>
              <li>
                Os pagamentos possuem data de vencimento. Após a data de
                vencimento o pagamento será expirado, sendo necessário gerar um
                novo;
              </li>
              <li>
                Pagamentos relacionados a envio de documentos, quando expirado
                ou cancelado, automaticamente cancela a solicitação de envio do
                documento;
              </li>
            </ul>

            <p>
              Para mais informações como pagar, consulte a secção Pagamento e
              Retirada do Veículo na nossa página de Como Comprar. Se você tiver
              alguma dúvida, por favor, envie-nos um e-mail para
              <a href="mailto:faleconosco@copart.com.br"
                >faleconosco@copart.com.br</a
              >
            </p>
          </div>
        </div>
      </div>
    `}calculatesubTotal(){let t=0;this.selectedRows.forEach(e=>{e.selectedFees.forEach(i=>{const o=e.Fees.find(s=>s.FeeType===i);o&&(t+=parseInt(o.FeeAmount))})}),this.subTotal=t,this.requestUpdate()}copyPaste(t){navigator.clipboard.writeText(t);const e=this.shadowRoot.getElementById("copiedMessage");e.style.display="block",setTimeout(()=>{e.style.display="none"},3e3)}};P.styles=[Os],D([Ee("#pix")],P.prototype,"pix",2),D([u()],P.prototype,"showModal",2),D([u()],P.prototype,"isLoadTable",2),D([u()],P.prototype,"titleModal",2),D([u()],P.prototype,"showModalFilters",2),D([u()],P.prototype,"dataListNotFormatted",2),D([u()],P.prototype,"dataList",2),D([u()],P.prototype,"showHead",2),D([u()],P.prototype,"showHeadMap",2),D([u()],P.prototype,"vehicleId",2),D([u()],P.prototype,"statusId",2),D([u()],P.prototype,"PaymentsHistoryOption",2),D([u()],P.prototype,"messageModal",2),D([b()],P.prototype,"memberId",2),D([u()],P.prototype,"pagination",2),D([b({type:String})],P.prototype,"token",2),D([b()],P.prototype,"servicesUrl",2),D([u()],P.prototype,"dataQrCode",2),D([u()],P.prototype,"subTotal",2),D([u()],P.prototype,"selectedOptions",2),P=D([R("request-payment")],P);const _s=_`
  :root {
    /* scroll */
    --scrollbar-size: 10px;

    /* Colors */
    --gray-25: #fcfcfd;
    --gray-50: #f9fafb;
    --gray-100: #f2f4f7;
    --gray-200: #eaecf0;
    --gray-300: #d0d5dd;
    --gray-400: #98a2b3;
    --gray-500: #667085;
    --gray-600: #475467;
    --gray-700: #344054;
    --gray-800: #1d2939;
    --gray-900: #101828;

    /* Primary-Color */
    --blue-50: #eaf2ff;
    --blue-100: #d5e5ff;
    --blue-200: #a6c8ff;
    --blue-300: #77abff;
    --blue-400: #489eff;
    --blue-500: #1254ff; /* Base */
    --blue-600: #0041cc;
    --blue-700: #003199;
    --blue-800: #002066;
    --blue-900: #001033;

    /* Error-Color */
    --error-50: #ffe8e0;
    --error-100: #ffd1c1;
    --error-200: #ffa392;
    --error-300: #ff7c63;
    --error-400: #ff5534;
    --error-500: #f76120;
    --error-600: #c23e18;
    --error-700: #911a0f;
    --error-800: #5f0e08;
    --error-900: #2e0704;

    /* Warning-Color */
    --yellow-50: #fff8e1;
    --yellow-100: #fff0c2;
    --yellow-200: #ffe999;
    --yellow-300: #ffdb70;
    --yellow-400: #ffce47;
    --yellow-500: #ffb838; /* Base */
    --yellow-600: #cc971f;
    --yellow-700: #996e15;
    --yellow-800: #66460c;
    --yellow-900: #332306;

    /*  Success-Color */
    --success-50: #e5f4e0;
    --success-100: #c9e9c1;
    --success-200: #9edf99;
    --success-300: #73d471;
    --success-400: #47c948;
    --success-500: #238202; /* Base */
    --success-600: #1a6300;
    --success-700: #113f00;
    --success-800: #092600;
    --success-900: #040d00;

    /* Warning-Color */
    --warning-25: #fffcf5;
    --warning-50: #fffaeb;
    --warning-100: #fef0c7;
    --warning-200: #fedf89;
    --warning-300: #fec84b;
    --warning-400: #fdb022;
    --warning-500: #f79009;
    --warning-600: #dc6803;
    --warning-700: #b54708;
    --warning-800: #93370d;
    --warning-900: #7a2e0e;

    /* Fonts */
    --body-font: 'Red Hat Display', sans-serif;
    --text-small-xs: 0.75rem; /* 12px */
    --text-small-sm: 0.875rem; /* 14px */
    --text-small-md: 1rem; /* 16px */
    --text-small-lg: 1.125rem; /* 18px */
    --text-small-xl: 1.25rem; /* 20px */
    --text-headline-sm: 1.5rem; /* 24px */
    --text-headline-md: 1.75rem; /* 28px */
    --text-headline-lg: 2.187rem; /* 35px */
    --text-display-sm: 3rem; /* 48px */
    --text-display-md: 3.75rem; /* 60px */
    --text-display-lg: 4.5rem; /* 72px */

    /* Font weight */
    --weight-light: 300;
    --weight-regular: 400;
    --weight-medium: 500;
    --weight-semibold: 600;
    --weight-bold: 700;
    --weight-extrabold: 800;
  }

  .content {
    .filters {
      display: flex;
      justify-content: flex-start;
      align-items: flex-end;
      gap: 20px;
      margin-left: 5px;
      margin-top: 10px;

      .input {
        width: 200px;
      }
    }

    .border {
      border: 1px solid #ddd;
      border-radius: 4px;
    }

    .header {
      display: flex;
      justify-content: space-between;
      align-items: center;

      .title {
        color: #1254ff;
        font-weight: bolder;
        font-family: 'Red Hat Display', sans-serif;
        font-size: 3rem;
        padding: 0px;
        margin: 0px;
      }

      .header-actions {
        display: flex;
        align-items: center;
        gap: 12px;

        .button-print {
          display: flex;
          align-items: center;
          gap: 6px;
          font-size: var(--text-small-sm);
          font-weight: var(--weight-semibold);
          color: var(--gray-700);
          background-color: transparent;
          border: none;
          font-family: inherit;
          cursor: pointer;

          &:hover {
            color: var(--blue-600);
            text-decoration: underline;
          }
        }
      }
    }

    .footer {
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
  }

  .expandChildTable::before {
    display: block;
    cursor: pointer;
  }

  .buttonsModal {
    display: flex;
    justify-content: flex-end;
    gap: 10px;
  }

  .totalPayment {
    text-align: end;
  }

  .button {
    background-color: #ffb838;
    border-radius: 4px;
    padding: 8px 16px;
    color: black;
    font-weight: 600;
    border: none;
    cursor: pointer;
    font-family: 'Red Hat Display';

    &:disabled {
      background-color: #eba930;
      cursor: not-allowed;
    }
  }

  .completionPayment {
    display: flex;
    justify-content: space-around;
    align-items: center;
  }

  .completionPayment .card {
    width: 400px;
    display: flex;
    flex-direction: column;
    border-radius: 4px;
    border: 1px solid #dfdfdf;
    height: 360px;

    p:nth-of-type(even) {
      text-align: right;
    }
  }

  .completionPayment .card .cardInfos {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    padding: 15px;
    gap: 15px;
  }

  .pagination {
    margin-block: 10px !important;
  }

  .modal-tbody {
    display: flex;
    flex-direction: column;
  }

  .Skeletons-tbody {
    display: flex;
    flex-direction: column;
  }

  .skeletonItem {
    width: 100%;
    height: 20px;
  }

  .modal-tr {
    display: grid;
    grid-template-columns: 100px 180px 1fr 1fr 100px;
  }

  .tr {
    display: grid;
    grid-template-columns: 60px repeat(8, 1fr);
  }

  .thead-td {
    background-color: #dfdfdf;
    padding: 10px;
    font-weight: bold;
    font-size: 12px;
  }

  .modal-td {
    font-size: 12px;
    padding: 4px 10px;
    color: black;
  }

  .td {
    font-size: 12px;
    padding: 4px 10px;
    color: black;
  }

  .qrCodeImage {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 10px;
    margin-bottom: 20px;

    textarea {
      width: 320px;
      resize: none;
      border-radius: 4px;
      border: 1px solid #dfdfdf;
      font-family: 'Red Hat Display', sans-serif !important;
      cursor: pointer;
    }

    img {
      height: 300px;
      width: 100%;
      border: 1px solid #dfdfdf;
      border-radius: 4px;
    }

    .pix {
      display: flex;
      flex-direction: column;
      align-items: center;

      p {
        display: flex;
        align-items: center;
        gap: 5px;
      }
    }
  }

  .checkbox {
    cursor: pointer;

    &:disabled {
      cursor: not-allowed;
    }
  }

  .theadFees {
    background-color: #ddd;
  }

  .widthTd {
    min-width: 100px;
  }

  .contentTable {
    display: flex;
    flex-direction: column;
    gap: 10px;
  }

  .contentTable .rowPayment {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-inline: 2px;
  }

  .contentTable .rowPayment p {
    font-size: 13px;
    font-weight: 700;
  }

  .contentTable .rowPayment .textIcons {
    display: flex;
    /* align-items: center; */
    gap: 12px;
  }

  .contentTable .rowPayment .textIcons a {
    display: flex;
    align-items: flex-end;
    gap: 4px;
    font-weight: 700;
    font-size: 12px;
    cursor: pointer;
  }

  .align {
    display: flex;
    justify-content: center;
  }

  .link {
    color: #1254ff;
    cursor: pointer;
  }

  .none {
    display: none;
  }

  .childTableRow {
    border: 1px solid #d0d0d0;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    padding: 10px;
    gap: 20px;

    .logo {
      height: 200px;
      width: 200px;
      object-fit: cover;
    }
  }

  .childTableRow .column {
    display: flex;
    flex-direction: column;
    margin-top: 28px;

    &.none {
      margin-top: 0;
    }

    .invoice {
      display: flex;
      align-items: center;
      gap: 10px;
      background: #c8e5ff;
      padding: 6px 10px;
      border-radius: 4px;
      color: #1254ff;
      font-size: 14px;
      cursor: pointer;
    }

    a {
      font-size: 22px;
      font-weight: 900;
      color: #1254ff;
      text-decoration: underline;
    }

    p {
      font-weight: bolder;
      font-size: 14px;
      margin-block: 4px;
    }
  }

  .contentTable .rowPayment .textIcons a:hover {
    color: #1254ff;
  }

  .table thead .th-table {
    padding: 8px;
    font-size: 12px;
    color: #151317;
    background-clip: padding-box !important;
    text-align: left;
    border-right: 1px solid white;
  }

  .totalBalance {
    border-top: 1px solid #ddd;
    background-color: #e1ffb9;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 5px;
  }

  .totalBalance .buyButton {
    display: flex;
    align-items: center;
    gap: 10px;
  }

  .totalBalance p {
    font-size: 17px;
    margin: 0;
    font-weight: 700;
  }

  .methodPayment {
    margin-top: 20px;
    display: flex;
    flex-direction: column;
    border: 1px solid #ddd;
    border-top-left-radius: 4px;
    border-top-right-radius: 4px;
    overflow: hidden;
  }

  .methodPayment .header {
    background-color: #1254ff;
    color: white;
    margin: 0;
    padding: 10px;
  }

  .methodPayment .header p {
    margin: 0;
    font-weight: 700;
  }

  .methodPayment .info {
    padding: 10px;

    p {
      margin: 0;
      font-size: 14px;

      a {
        color: blue;
        cursor: pointer;
      }
    }

    ul li {
      margin: 0;
      font-size: 14px;
    }
  }

  .copied-message {
    position: fixed;
    top: 20px;
    left: 50%;
    transform: translateX(-50%);
    background-color: #4caf50;
    color: white;
    padding: 15px;
    border-radius: 5px;
    font-size: 16px;
    z-index: 9999;
    display: none;
  }

  .skeletons {
    display: flex;
    gap: 60px;
    width: 100%;
    margin-bottom: 10px;
  }

  .responsiveButton {
    display: none;
  }

  .skeleton {
    animation: skeleton-loading 1s linear infinite alternate;
  }

  .skeleton2 {
    animation: skeleton-loading2 1s linear infinite alternate;
  }

  .skeletonWidth {
    width: 100%;
    height: 350px;
  }

  @keyframes skeleton-loading {
    0% {
      background-color: hsl(200, 20%, 80%);
    }
    100% {
      background-color: hsl(200, 20%, 95%);
    }
  }
  @keyframes skeleton-loading2 {
    0% {
      background-color: hsl(200, 20%, 95%);
    }
    100% {
      background-color: hsl(200, 20%, 80%);
    }
  }

  @media (max-width: 880px) {
    .content {
      .header {
        flex-direction: column;

        .title {
          font-size: 2rem;
        }
      }

      .filters {
        display: none;
      }
    }

    .responsiveButton {
      display: block;
      margin-block: 10px;
    }

    .filtersResponsive {
      padding: 10px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      width: 300px;
    }
  }
`;var Rs=Object.defineProperty,Ls=Object.getOwnPropertyDescriptor,S=(t,e,i,o)=>{for(var s=o>1?void 0:o?Ls(e,i):e,r=t.length-1,a;r>=0;r--)(a=t[r])&&(s=(o?a(e,i,s):a(s))||s);return o&&s&&Rs(e,i,s),s};let $=class extends T{constructor(){super(...arguments),this.showModal=!1,this.completionPayment=!1,this.isLoadTable=!1,this.showHead=!1,this.showHeadMap=new Map,this.memberId=1024863,this.pagination={memberId:this.memberId,baseQuery:"",pageSize:20,pageNumber:1,sortField:"",sortOrder:"",totalPages:0,numFound:0},this.selectedRows=[],this.titleModal="Aguardando Pagamento",this.vehicleId=0,this.saleStatus=0,this.saleType=0,this.token="",this.servicesUrl="",this.theadData=[{id:"-",label:"-",hoverMensage:"-"},{label:"Código",id:"VehicleId"},{label:"Tipo de Venda",id:"Info"},{label:"Ano",id:"ModelYear"},{label:"Marca",id:"Make"},{label:"Modelo",id:"Model"},{label:"Data da Venda",id:"SaleDate"},{label:"Doc Previsto",id:"DocPrevisto",hoverMensage:"mensagem do hover"},{label:"Status",id:"Status"},{label:"Local Retirada",id:"PickupLocation"},{label:"Código de Rastreio",id:"TrackingCode"}]}formatDataList(t){const e=o=>{let s;switch(o){case 1:s="warning";break;case 2:s="lime";break;case 3:s="blue";break;case 4:s="yellow";break;case 5:s="violet";break;case 6:s="gold";break;case 7:s="success";break;case 8:s="gray";break;default:s="gray"}return s};return t.items.map(o=>({...o,SaleDate:this.formatDate(o.SaleDate),DocPrevisto:h`
      <div title="Essa é a previsão de disponibilidade do documento na Copart">
        ${this.formatDate(o.DocPrevisto)}
      </div>`,SaleValue:this.formatMoney(o.SaleValue),"-":this.checkBoxTable(o),Info:`${o.SaleType}: ${o.SaleInfo}`,TrackingCode:h`<tracking-code-table
        .TrackingCode=${o.TrackingCode}
      ></tracking-code-table>`,Status:o.IsBlocked?h`<colibri-common-g2-badge
            type=${"error"}
            size="sm"
            text=${"Bloqueado"}
          ></colibri-common-g2-badge>`:h`<colibri-common-g2-badge
            type=${e(o.StatusId)}
            size="sm"
            text=${o.Status}
          ></colibri-common-g2-badge>`}))}fetchData(){this.showModalFilters&&(this.showModalFilters=!1),this.isLoadTable=!0,I(`${this.servicesUrl}/G2OnlineServices/GetMemberVehicleDocuments`,this.token,{memberId:this.memberId,pageSize:this.pagination.pageSize,pageNumber:this.pagination.pageNumber,vehicleId:this.vehicleId==0?0:this.vehicleId,statusId:this.saleStatus,saleType:this.saleType},t=>{this.isLoadTable=!1,this.dataListNotFormatted=t.items,this.dataList=this.formatDataList(t),this.pagination=this.pagination={...this.pagination,numFound:t.pagination.numFound,pageSize:t.pagination.pageSize,pageNumber:t.pagination.pageNumber,totalPages:t.pagination.totalPages},this.requestUpdate()},()=>{})}GetMemberVehicleDocumentosFilters(){pe(`${this.servicesUrl}/G2OnlineServices/GetMemberVehicleDocumentosFilters`,this.token,t=>{this.GetMemberVehicleDocumentosOptionsStatus=t.Status.map(e=>({id:String(e.id),value:String(e.id),name:e.descricao})),this.GetMemberVehicleDocumentosOptionsStatus.unshift({id:"0",value:"0",name:"Selecione uma opção"}),this.GetMemberVehicleDocumentosOptionsSaleType=t.SaleType.map(e=>({id:String(e.id),value:String(e.id),name:e.descricao})),this.GetMemberVehicleDocumentosOptionsSaleType.unshift({id:"0",value:"0",name:"Selecione uma opção"}),this.requestUpdate()},()=>{})}PrintVehicleDocumentsToPdf(){I(`${this.servicesUrl}/G2OnlineServices/PrintVehicleDocumentsToPdf`,this.token,{items:this.dataListNotFormatted},t=>{if(t.resultCode===0&&t.content){const e=atob(t.content),i=new Array(e.length);for(let l=0;l<e.length;l++)i[l]=e.charCodeAt(l);const o=new Uint8Array(i),s=new Blob([o],{type:"application/pdf"}),r=URL.createObjectURL(s),a=new Date,n=String(a.getDate()).padStart(2,"0"),c=String(a.getMonth()+1).padStart(2,"0"),m=a.getFullYear(),p=document.createElement("a");p.style.display="none",p.href=r,p.download=`documentosDosVeículos${n}/${c}/${m}.pdf`,document.body.appendChild(p),p.click(),URL.revokeObjectURL(r),document.body.removeChild(p)}},()=>{})}ExportVehicleDocumentsToExcel(){I(`${this.servicesUrl}/G2OnlineServices/ExportVehicleDocumentsToExcel`,this.token,{items:this.dataListNotFormatted},t=>{if(t.resultCode===0&&t.content){const e=atob(t.content),i=new Array(e.length);for(let l=0;l<e.length;l++)i[l]=e.charCodeAt(l);const o=new Uint8Array(i),s=new Blob([o],{type:"application/vnd.ms-excel"}),r=URL.createObjectURL(s),a=new Date,n=String(a.getDate()).padStart(2,"0"),c=String(a.getMonth()+1).padStart(2,"0"),m=a.getFullYear(),p=document.createElement("a");p.style.display="none",p.href=r,p.download=`documentosDosVeículos${n}/${c}/${m}.xls`,document.body.appendChild(p),p.click(),URL.revokeObjectURL(r),document.body.removeChild(p)}},()=>{})}toggleCheckbox(t,e){t.target.checked?this.selectedRows=[...this.selectedRows,e]:this.selectedRows=this.selectedRows.filter(o=>o.VehicleId!==e.VehicleId)}async connectedCallback(){super.connectedCallback(),await super.updateComplete,this.fetchData(),this.GetMemberVehicleDocumentosFilters(),this.addEventListener("selection-removed",t=>{const{vehicleId:e}=t.detail;this.selectedRows=this.selectedRows.filter(i=>i.VehicleId!==e)})}async handleOnChangePagination(t,e){t==="pageSize"&&(this.pagination={...this.pagination,pageNumber:1}),this.pagination={...this.pagination,[t]:e},this.fetchData()}handleShowModal(){this.showModal=!this.showModal,this.showModal!=!0&&(this.fetchData(),this.selectedRows=[],this.documentsSend.clearInterval())}handleOpenModalFilters(){this.showModalFilters=!this.showModalFilters}filterModalResponsive(){return h`
      <g2-dialog
        .isOpen=${this.showModalFilters}
        title="Filtros"
        @on-close=${this.handleOpenModalFilters}
      >
        <div class="filtersResponsive">
          <colibri-common-g2-input
            class="input"
            isLabel="Código Veículo"
            @on-input=${t=>this.vehicleId=t.detail.value}
          ></colibri-common-g2-input>

          <colibri-common-g2-select
            class="input"
            isLabel="Status"
            .isChildren=${this.GetMemberVehicleDocumentosOptionsStatus}
            @on-input=${t=>this.saleStatus=t.detail.value}
          ></colibri-common-g2-select>

          <colibri-common-g2-select
            class="input"
            isLabel="Tipo de venda"
            .isChildren=${this.GetMemberVehicleDocumentosOptionsSaleType}
            @on-input=${t=>this.saleType=t.detail.value}
          ></colibri-common-g2-select>

          <colibri-common-g2-button
            @onClick=${this.fetchData}
            radius="radius-sm"
            variant="dark"
            size="xs"
          >
            <ph-funnel-simple
              color="var(--gray-50)"
              weight="bold"
              size="18px"
            ></ph-funnel-simple>
            Filtrar
          </colibri-common-g2-button>
        </div>
      </g2-dialog>
    `}render(){var t,e,i,o;return h`
      <g2-dialog
        .isOpen=${this.showModal}
        title=${this.messageCallback?"Aviso":this.titleModal}
        @on-close=${this.handleShowModal}
      >
        ${this.showModal?h`<documents-send
              id="documentsSend"
              .dataList=${this.selectedRows}
              .memberId=${this.memberId}
              .servicesUrl=${this.servicesUrl}
              .token=${this.token}
              @data-QrCode=${s=>this.titleModal=s.detail}
              @message-callback=${s=>this.messageCallback=s.detail}
            ></documents-send>`:null}
      </g2-dialog>

      ${this.filterModalResponsive()}

      <div class="content">
        <div class="header">
          <h2 class="title">Documentos dos Veículos</h2>
          <div class="header-actions">
            <button
              @click=${this.ExportVehicleDocumentsToExcel}
              class="button-print"
            >
              <ph-cloud-arrow-down
                color="var(--gray-600)"
                size="16px"
                weight="bold"
              ></ph-cloud-arrow-down>
              Exportar
            </button>

            <button
              class="button-print"
              @click=${this.PrintVehicleDocumentsToPdf}
            >
              <ph-printer
                color="var(--gray-600)"
                size="16px"
                weight="bold"
              ></ph-printer>
              Imprimir
            </button>
          </div>
        </div>

        <p>
          Nesta página você pode verificar os documentos dos veículos comprados
        </p>

        <colibri-common-g2-button
          @onClick=${this.handleOpenModalFilters}
          class="responsiveButton"
          radius="radius-sm"
          variant="dark"
          size="xs"
        >
          <ph-funnel-simple
            color="var(--gray-50)"
            weight="bold"
            size="18px"
          ></ph-funnel-simple>
          Opções de filtro
        </colibri-common-g2-button>
        <div class="border">

          <div class="filters">
            <colibri-common-g2-input
              class="input"
              isLabel="Código Veículo"
              @on-input=${s=>this.vehicleId=s.detail.value}
            ></colibri-common-g2-input>

            <colibri-common-g2-select
              class="input"
              isLabel="Status"
              .isChildren=${this.GetMemberVehicleDocumentosOptionsStatus}
              @on-input=${s=>this.saleStatus=s.detail.value}
            ></colibri-common-g2-select>

            <colibri-common-g2-select
              class="input"
              isLabel="Tipo de venda"
              .isChildren=${this.GetMemberVehicleDocumentosOptionsSaleType}
              @on-input=${s=>this.saleType=s.detail.value}
            ></colibri-common-g2-select>

            <colibri-common-g2-button
              @onClick=${this.fetchData}
              radius="radius-sm"
              variant="dark"
              size="xs"
            >
              <ph-funnel-simple
                color="var(--gray-50)"
                weight="bold"
                size="18px"
              ></ph-funnel-simple>
              Filtrar
            </colibri-common-g2-button>
          </div>

          <div class="contentTable">
            <colibri-common-g2-pagination
              limit=${(t=this.pagination)==null?void 0:t.pageSize}
              total=${(e=this.pagination)==null?void 0:e.totalPages}
              offset=${this.pagination.pageNumber}
              @my-page-changed=${s=>this.handleOnChangePagination("pageNumber",s.detail.current)}
              @row-per-page=${s=>this.handleOnChangePagination("pageSize",s.detail)}
            ></colibri-common-g2-pagination>

            <div class="modal-tbody">
              <colibri-common-g2-table-default
                .load=${this.isLoadTable}
                .theadData=${this.theadData}
                .tbodyData=${this.dataList}
                type="alternate"
                isSort
              ></colibri-common-g2-table-default>
            </div>
          </div>

          <div class="pagination">
            <colibri-common-g2-pagination
              limit=${(i=this.pagination)==null?void 0:i.pageSize}
              total=${(o=this.pagination)==null?void 0:o.totalPages}
              offset=${this.pagination.pageNumber}
              @my-page-changed=${s=>this.handleOnChangePagination("pageNumber",s.detail.current)}
              @row-per-page=${s=>this.handleOnChangePagination("pageSize",s.detail)}
            ></colibri-common-g2-pagination>
          </div>
        </div>

        <div class="footer">
          <p>Quantidade selecionados: ${this.selectedRows.length}</p>

          <colibri-common-g2-button
            .isDisabled=${this.selectedRows.length==0}
            @onClick=${this.handleShowModal}
            variant="default"
          >
            Solicitar Envio
          </colibri-common-g2-button>
        </div>

        <div class="methodPayment">
          <div class="header">
            <p>Como retirar o meu documento?</p>
          </div>

          <div class="info">
            <p>
              A Copart do Brasil oferece várias formas para que realize a
              retirada do seu documento. Escolha entre os seguintes métodos:
            </p>
            <ul>
              <li>
                Solicite o envio do documento para o seu endereço cadastrado na
                Copart do Brasil
              </li>
              <li>
                Solicite o envio do documento para outro endereço de sua
                preferência
              </li>
              <li>
                Solicite a retirada do documento em um de nossos pátios fora de
                São Paulo. Documento será disponibilizado em até 5 dias úteis
              </li>
              <li>
                Faça a retirada do documento direto no balcão. O pátio será
                informado no campo Local do Documento
              </li>
            </ul>

            <p>
              A Copart do Brasil não se responsabilizará por eventuais extravios
              ou rasuras nos documentos enviados por Sedex.
            </p>
          </div>
        </div>
      </div>
    `}formatDate(t){if(t===null||t===0)return"";const e=new Date(t),i=String(e.getDate()).padStart(2,"0"),o=String(e.getMonth()+1).padStart(2,"0"),s=e.getFullYear();return`${i}/${o}/${s}`}formatMoney(t){return new Intl.NumberFormat("pt-BR",{style:"currency",currency:"BRL"}).format(t)}checkBoxTable(t){return h`<input
      ?disabled=${!t.IsSelectable}
      @input=${e=>{this.toggleCheckbox(e,t)}}
      type="checkbox"
    />`}};$.styles=[_s],S([Ee("#documentsSend")],$.prototype,"documentsSend",2),S([u()],$.prototype,"showModal",2),S([u()],$.prototype,"completionPayment",2),S([u()],$.prototype,"isLoadTable",2),S([u()],$.prototype,"dataList",2),S([u()],$.prototype,"dataListNotFormatted",2),S([u()],$.prototype,"isActiveClipBoard",2),S([u()],$.prototype,"showHead",2),S([u()],$.prototype,"showModalFilters",2),S([u()],$.prototype,"showHeadMap",2),S([b()],$.prototype,"memberId",2),S([u()],$.prototype,"pagination",2),S([u()],$.prototype,"dataQrCode",2),S([u()],$.prototype,"selectedRows",2),S([u()],$.prototype,"GetMemberVehicleDocumentosOptionsStatus",2),S([u()],$.prototype,"GetMemberVehicleDocumentosOptionsSaleType",2),S([u()],$.prototype,"titleModal",2),S([u()],$.prototype,"messageCallback",2),S([u()],$.prototype,"vehicleId",2),S([u()],$.prototype,"saleStatus",2),S([u()],$.prototype,"saleType",2),S([b({type:String})],$.prototype,"token",2),S([b()],$.prototype,"servicesUrl",2),$=S([R("vehicle-document")],$);const mi=_`
  .container {
    width: 100%;
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    margin-top: 10px;
    gap: 10px;

    .span {
      grid-column: span 2;
    }

    .contentButtons {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .secondColumn {
      margin-left: auto;
      grid-column: 2;
    }
  }

  @media (max-width: 880px) {
    .container {
      display: flex;
      flex-direction: column;

      .contentButtons {
        display: flex;
        align-items: center;
        gap: 10px;
      }

      .secondColumn {
        margin-left: auto;
        grid-column: 2;
      }
    }
  }
`;var Ns=Object.defineProperty,Ms=Object.getOwnPropertyDescriptor,Q=(t,e,i,o)=>{for(var s=o>1?void 0:o?Ms(e,i):e,r=t.length-1,a;r>=0;r--)(a=t[r])&&(s=(o?a(e,i,s):a(s))||s);return o&&s&&Ns(e,i,s),s};let q=class extends T{constructor(){super(...arguments),this.isDisabledInput=!0,this.loadSkeletonInput=!1,this.zipCodeDetails={streetName:"",neighborhood:"",cityId:"",state:""},this.servicesUrl="",this.memberId=0,this.token="",this.data={AddressName:"",AddressNumber:"",ZipCode:"",Neighborhood:"",City:"",State:"",Complement:"",CityId:""},this.errors={AddressNumber:"",ZipCode:""}}static get styles(){return[mi]}async connectedCallback(){super.connectedCallback(),await super.updateComplete}onChange(t){const e=t.detail,{name:i,value:o}=e;this.dispatchEvent(new CustomEvent("on-Change",{detail:{name:i,value:o}}))}saveNewAddress(){this.dispatchEvent(new CustomEvent("save-new-address")),this.isDisabledInput=!0}fetchAZipCode(){this.loadSkeletonInput=!0,I(`${this.servicesUrl}/G2Member/SearchZipCode`,this.token,{zipCode:this.data.ZipCode},t=>{this.data={...this.data,AddressName:t.zipCodeDetails.streetName,Neighborhood:t.zipCodeDetails.neighborhood,City:t.zipCodeDetails.cityDescription,CityId:t.zipCodeDetails.cityId,State:t.zipCodeDetails.state},this.loadSkeletonInput=!1,this.dispatchEvent(new CustomEvent("zipcode-searched-sucessfully",{detail:this.data})),this.requestUpdate()},()=>{})}render(){var t,e,i,o,s,r,a,n,c;return h`
      <div class="container">
        <colibri-common-g2-input
          isLabel="Cep"
          name="ZipCode"
          .value=${(t=this.data)==null?void 0:t.ZipCode}
          @on-input=${m=>this.onChange(m)}
          @blur=${()=>this.fetchAZipCode()}
          .error=${(e=this.errors)==null?void 0:e.ZipCode}
          .isDisabled=${this.isDisabledInput}
          type="text"
        >
        </colibri-common-g2-input>

        ${this.loadSkeletonInput?h`<ui-load-input
              isLabel="Logradouro"
              style="align-self:start"
            ></ui-load-input>`:h`<colibri-common-g2-input
              isLabel="Logradouro"
              name="name"
              value=${(i=this.data)==null?void 0:i.AddressName}
              @on-input=${m=>this.onChange(m)}
              isDisabled
              type="text"
            >
            </colibri-common-g2-input>`}

        <colibri-common-g2-input
          isLabel="Número"
          name="AddressNumber"
          value=${(o=this.data)==null?void 0:o.AddressNumber}
          @on-input=${m=>this.onChange(m)}
          .isDisabled=${this.isDisabledInput}
          .error=${(s=this.errors)==null?void 0:s.AddressNumber}
          type="text"
        >
        </colibri-common-g2-input>

        <colibri-common-g2-input
          isLabel="Complemento"
          name="Complement"
          value=${(r=this.data)==null?void 0:r.Complement}
          @on-input=${m=>this.onChange(m)}
          .isDisabled=${this.isDisabledInput}
          type="text"
        >
        </colibri-common-g2-input>

        ${this.loadSkeletonInput?h`<ui-load-input
              isLabel="Logradouro"
              style="align-self:start"
            ></ui-load-input>`:h`<colibri-common-g2-input
              isLabel="Bairro"
              name="name"
              value=${(a=this.data)==null?void 0:a.Neighborhood}
              isDisabled
              type="text"
            >
            </colibri-common-g2-input>`}
        ${this.loadSkeletonInput?h`<ui-load-input
              isLabel="Cidade"
              style="align-self:start"
            ></ui-load-input>`:h`<colibri-common-g2-input
              isLabel="Cidade"
              name="name"
              value=${(n=this.data)==null?void 0:n.City}
              isDisabled
              type="text"
            >
            </colibri-common-g2-input>`}
        ${this.loadSkeletonInput?h`<ui-load-input isLabel="Estado" class="span"></ui-load-input>`:h`<colibri-common-g2-input
              class="span"
              isLabel="Estado"
              name="State"
              value=${(c=this.data)==null?void 0:c.State}
              isDisabled
              type="text"
            >
            </colibri-common-g2-input>`}

        <div class="contentButtons secondColumn">
          ${this.isDisabledInput?null:h`<colibri-common-g2-button
                @onClick=${this.saveNewAddress}
                variant="default"
              >
                Salvar
              </colibri-common-g2-button>`}
        </div>
      </div>
    `}};Q([b()],q.prototype,"isDisabledInput",2),Q([u()],q.prototype,"loadSkeletonInput",2),Q([u()],q.prototype,"zipCodeDetails",2),Q([b()],q.prototype,"servicesUrl",2),Q([b()],q.prototype,"memberId",2),Q([b({type:String})],q.prototype,"token",2),Q([b()],q.prototype,"data",2),Q([b()],q.prototype,"errors",2),q=Q([R("actual-form")],q);var zs=Object.defineProperty,Us=Object.getOwnPropertyDescriptor,W=(t,e,i,o)=>{for(var s=o>1?void 0:o?Us(e,i):e,r=t.length-1,a;r>=0;r--)(a=t[r])&&(s=(o?a(e,i,s):a(s))||s);return o&&s&&zs(e,i,s),s};let H=class extends T{constructor(){super(...arguments),this.zipCodeDetails={streetName:"",neighborhood:"",cityDescription:"",state:""},this.loadSkeletonInput=!1,this.servicesUrl="",this.memberId=0,this.token="",this.errors={AddressNumber:"",ZipCode:""},this.data={AddressName:"",AddressNumber:"",ZipCode:"",Neighborhood:"",City:"",State:"",Complement:"",CityId:""}}static get styles(){return[mi]}async connectedCallback(){super.connectedCallback(),await super.updateComplete}fetchAZipCode(){this.loadSkeletonInput=!0,I(`${this.servicesUrl}/G2Member/SearchZipCode`,this.token,{zipCode:this.data.ZipCode},t=>{this.data={...this.data,AddressName:t.zipCodeDetails.streetName,Neighborhood:t.zipCodeDetails.neighborhood,City:t.zipCodeDetails.cityDescription,CityId:t.zipCodeDetails.cityId,State:t.zipCodeDetails.state},this.loadSkeletonInput=!1,this.dispatchEvent(new CustomEvent("zipcode-searched-sucessfully",{detail:this.data})),this.requestUpdate()},()=>{})}onChange(t){const e=t.detail,{name:i,value:o}=e;if(i=="ZipCode")if(isNaN(parseInt(o))){this.errors.ZipCode="Digíte apenas números!";return}else this.errors.ZipCode="";this.dispatchEvent(new CustomEvent("on-Change",{detail:{name:i,value:o}}))}render(){var t,e,i,o;return h`
      <div class="container">
        <colibri-common-g2-input
          isLabel="Cep"
          name="ZipCode"
          @on-input=${s=>this.onChange(s)}
          @blur=${()=>this.fetchAZipCode()}
          maxlength="8"
          @keypress=${s=>{s.keyCode==13&&this.fetchAZipCode()}}
          error=${this.errors.ZipCode}
          type="text"
        >
        </colibri-common-g2-input>

        ${this.loadSkeletonInput?h`<ui-load-input
              isLabel="Logradouro"
              style="align-self:start"
            ></ui-load-input>`:h`<colibri-common-g2-input
              isLabel="Logradouro"
              name="AddressName"
              @on-input=${s=>this.onChange(s)}
              .value=${(t=this.data)==null?void 0:t.AddressName}
              isDisabled
              type="text"
            >
            </colibri-common-g2-input>`}

        <colibri-common-g2-input
          isLabel="Número"
          name="AddressNumber"
          @on-input=${s=>this.onChange(s)}
          error=${this.errors.AddressNumber}
          type="text"
        >
        </colibri-common-g2-input>

        <colibri-common-g2-input
          isLabel="Complemento"
          name="Complement"
          @on-input=${s=>this.onChange(s)}
          type="text"
        >
        </colibri-common-g2-input>

        ${this.loadSkeletonInput?h`<ui-load-input isLabel="Bairro"></ui-load-input>`:h`<colibri-common-g2-input
              isLabel="Bairro"
              name="Neighborhood"
              @on-input=${s=>this.onChange(s)}
              .value=${(e=this.data)==null?void 0:e.Neighborhood}
              isDisabled
              type="text"
            >
            </colibri-common-g2-input>`}
        ${this.loadSkeletonInput?h`<ui-load-input
              isLabel="Cidade"
              style="align-self:end"
            ></ui-load-input>`:h`<colibri-common-g2-input
              isLabel="Cidade"
              name="City"
              @on-input=${s=>this.onChange(s)}
              .value=${(i=this.data)==null?void 0:i.City}
              isDisabled
              type="text"
            >
            </colibri-common-g2-input>`}
        ${this.loadSkeletonInput?h`<ui-load-input isLabel="Estado" class="span"></ui-load-input>`:h`<colibri-common-g2-input
              class="span"
              isLabel="Estado"
              name="State"
              .value=${(o=this.data)==null?void 0:o.State}
              @on-input=${s=>this.onChange(s)}
              isDisabled
              type="text"
            >
            </colibri-common-g2-input>`}
      </div>
    `}};W([u()],H.prototype,"zipCodeDetails",2),W([u()],H.prototype,"loadSkeletonInput",2),W([b()],H.prototype,"servicesUrl",2),W([b()],H.prototype,"memberId",2),W([b({type:String})],H.prototype,"token",2),W([b()],H.prototype,"errors",2),W([b()],H.prototype,"data",2),W([u()],H.prototype,"cep",2),H=W([R("third-form")],H)});
