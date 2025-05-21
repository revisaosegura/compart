(function(ne){typeof define=="function"&&define.amd?define(ne):ne()})(function(){"use strict";/*! colibri-online-payments - v1.0.0 *//**
 * @license
 * Copyright 2019 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */var Ei;const ne=globalThis,Ze=ne.ShadowRoot&&(ne.ShadyCSS===void 0||ne.ShadyCSS.nativeShadow)&&"adoptedStyleSheets"in Document.prototype&&"replace"in CSSStyleSheet.prototype,Ye=Symbol(),Pt=new WeakMap;let kt=class{constructor(e,i,o){if(this._$cssResult$=!0,o!==Ye)throw Error("CSSResult is not constructable. Use `unsafeCSS` or `css` instead.");this.cssText=e,this.t=i}get styleSheet(){let e=this.o;const i=this.t;if(Ze&&e===void 0){const o=i!==void 0&&i.length===1;o&&(e=Pt.get(i)),e===void 0&&((this.o=e=new CSSStyleSheet).replaceSync(this.cssText),o&&Pt.set(i,e))}return e}toString(){return this.cssText}};const Oi=t=>new kt(typeof t=="string"?t:t+"",void 0,Ye),N=(t,...e)=>{const i=t.length===1?t[0]:e.reduce((o,s,r)=>o+(n=>{if(n._$cssResult$===!0)return n.cssText;if(typeof n=="number")return n;throw Error("Value passed to 'css' function must be a 'css' function result: "+n+". Use 'unsafeCSS' to pass non-literal values, but take care to ensure page security.")})(s)+t[r+1],t[0]);return new kt(i,t,Ye)},Ri=(t,e)=>{if(Ze)t.adoptedStyleSheets=e.map(i=>i instanceof CSSStyleSheet?i:i.styleSheet);else for(const i of e){const o=document.createElement("style"),s=ne.litNonce;s!==void 0&&o.setAttribute("nonce",s),o.textContent=i.cssText,t.appendChild(o)}},Dt=Ze?t=>t:t=>t instanceof CSSStyleSheet?(e=>{let i="";for(const o of e.cssRules)i+=o.cssText;return Oi(i)})(t):t;/**
 * @license
 * Copyright 2017 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */const{is:Ii,defineProperty:_i,getOwnPropertyDescriptor:Fi,getOwnPropertyNames:Li,getOwnPropertySymbols:Ni,getPrototypeOf:Mi}=Object,X=globalThis,At=X.trustedTypes,zi=At?At.emptyScript:"",Je=X.reactiveElementPolyfillSupport,ve=(t,e)=>t,Re={toAttribute(t,e){switch(e){case Boolean:t=t?zi:null;break;case Object:case Array:t=t==null?t:JSON.stringify(t)}return t},fromAttribute(t,e){let i=t;switch(e){case Boolean:i=t!==null;break;case Number:i=t===null?null:Number(t);break;case Object:case Array:try{i=JSON.parse(t)}catch{i=null}}return i}},Ke=(t,e)=>!Ii(t,e),Et={attribute:!0,type:String,converter:Re,reflect:!1,hasChanged:Ke};Symbol.metadata??(Symbol.metadata=Symbol("metadata")),X.litPropertyMetadata??(X.litPropertyMetadata=new WeakMap);let ue=class extends HTMLElement{static addInitializer(e){this._$Ei(),(this.l??(this.l=[])).push(e)}static get observedAttributes(){return this.finalize(),this._$Eh&&[...this._$Eh.keys()]}static createProperty(e,i=Et){if(i.state&&(i.attribute=!1),this._$Ei(),this.elementProperties.set(e,i),!i.noAccessor){const o=Symbol(),s=this.getPropertyDescriptor(e,o,i);s!==void 0&&_i(this.prototype,e,s)}}static getPropertyDescriptor(e,i,o){const{get:s,set:r}=Fi(this.prototype,e)??{get(){return this[i]},set(n){this[i]=n}};return{get(){return s==null?void 0:s.call(this)},set(n){const a=s==null?void 0:s.call(this);r.call(this,n),this.requestUpdate(e,a,o)},configurable:!0,enumerable:!0}}static getPropertyOptions(e){return this.elementProperties.get(e)??Et}static _$Ei(){if(this.hasOwnProperty(ve("elementProperties")))return;const e=Mi(this);e.finalize(),e.l!==void 0&&(this.l=[...e.l]),this.elementProperties=new Map(e.elementProperties)}static finalize(){if(this.hasOwnProperty(ve("finalized")))return;if(this.finalized=!0,this._$Ei(),this.hasOwnProperty(ve("properties"))){const i=this.properties,o=[...Li(i),...Ni(i)];for(const s of o)this.createProperty(s,i[s])}const e=this[Symbol.metadata];if(e!==null){const i=litPropertyMetadata.get(e);if(i!==void 0)for(const[o,s]of i)this.elementProperties.set(o,s)}this._$Eh=new Map;for(const[i,o]of this.elementProperties){const s=this._$Eu(i,o);s!==void 0&&this._$Eh.set(s,i)}this.elementStyles=this.finalizeStyles(this.styles)}static finalizeStyles(e){const i=[];if(Array.isArray(e)){const o=new Set(e.flat(1/0).reverse());for(const s of o)i.unshift(Dt(s))}else e!==void 0&&i.push(Dt(e));return i}static _$Eu(e,i){const o=i.attribute;return o===!1?void 0:typeof o=="string"?o:typeof e=="string"?e.toLowerCase():void 0}constructor(){super(),this._$Ep=void 0,this.isUpdatePending=!1,this.hasUpdated=!1,this._$Em=null,this._$Ev()}_$Ev(){var e;this._$ES=new Promise(i=>this.enableUpdating=i),this._$AL=new Map,this._$E_(),this.requestUpdate(),(e=this.constructor.l)==null||e.forEach(i=>i(this))}addController(e){var i;(this._$EO??(this._$EO=new Set)).add(e),this.renderRoot!==void 0&&this.isConnected&&((i=e.hostConnected)==null||i.call(e))}removeController(e){var i;(i=this._$EO)==null||i.delete(e)}_$E_(){const e=new Map,i=this.constructor.elementProperties;for(const o of i.keys())this.hasOwnProperty(o)&&(e.set(o,this[o]),delete this[o]);e.size>0&&(this._$Ep=e)}createRenderRoot(){const e=this.shadowRoot??this.attachShadow(this.constructor.shadowRootOptions);return Ri(e,this.constructor.elementStyles),e}connectedCallback(){var e;this.renderRoot??(this.renderRoot=this.createRenderRoot()),this.enableUpdating(!0),(e=this._$EO)==null||e.forEach(i=>{var o;return(o=i.hostConnected)==null?void 0:o.call(i)})}enableUpdating(e){}disconnectedCallback(){var e;(e=this._$EO)==null||e.forEach(i=>{var o;return(o=i.hostDisconnected)==null?void 0:o.call(i)})}attributeChangedCallback(e,i,o){this._$AK(e,o)}_$EC(e,i){var r;const o=this.constructor.elementProperties.get(e),s=this.constructor._$Eu(e,o);if(s!==void 0&&o.reflect===!0){const n=(((r=o.converter)==null?void 0:r.toAttribute)!==void 0?o.converter:Re).toAttribute(i,o.type);this._$Em=e,n==null?this.removeAttribute(s):this.setAttribute(s,n),this._$Em=null}}_$AK(e,i){var r;const o=this.constructor,s=o._$Eh.get(e);if(s!==void 0&&this._$Em!==s){const n=o.getPropertyOptions(s),a=typeof n.converter=="function"?{fromAttribute:n.converter}:((r=n.converter)==null?void 0:r.fromAttribute)!==void 0?n.converter:Re;this._$Em=s,this[s]=a.fromAttribute(i,n.type),this._$Em=null}}requestUpdate(e,i,o){if(e!==void 0){if(o??(o=this.constructor.getPropertyOptions(e)),!(o.hasChanged??Ke)(this[e],i))return;this.P(e,i,o)}this.isUpdatePending===!1&&(this._$ES=this._$ET())}P(e,i,o){this._$AL.has(e)||this._$AL.set(e,i),o.reflect===!0&&this._$Em!==e&&(this._$Ej??(this._$Ej=new Set)).add(e)}async _$ET(){this.isUpdatePending=!0;try{await this._$ES}catch(i){Promise.reject(i)}const e=this.scheduleUpdate();return e!=null&&await e,!this.isUpdatePending}scheduleUpdate(){return this.performUpdate()}performUpdate(){var o;if(!this.isUpdatePending)return;if(!this.hasUpdated){if(this.renderRoot??(this.renderRoot=this.createRenderRoot()),this._$Ep){for(const[r,n]of this._$Ep)this[r]=n;this._$Ep=void 0}const s=this.constructor.elementProperties;if(s.size>0)for(const[r,n]of s)n.wrapped!==!0||this._$AL.has(r)||this[r]===void 0||this.P(r,this[r],n)}let e=!1;const i=this._$AL;try{e=this.shouldUpdate(i),e?(this.willUpdate(i),(o=this._$EO)==null||o.forEach(s=>{var r;return(r=s.hostUpdate)==null?void 0:r.call(s)}),this.update(i)):this._$EU()}catch(s){throw e=!1,this._$EU(),s}e&&this._$AE(i)}willUpdate(e){}_$AE(e){var i;(i=this._$EO)==null||i.forEach(o=>{var s;return(s=o.hostUpdated)==null?void 0:s.call(o)}),this.hasUpdated||(this.hasUpdated=!0,this.firstUpdated(e)),this.updated(e)}_$EU(){this._$AL=new Map,this.isUpdatePending=!1}get updateComplete(){return this.getUpdateComplete()}getUpdateComplete(){return this._$ES}shouldUpdate(e){return!0}update(e){this._$Ej&&(this._$Ej=this._$Ej.forEach(i=>this._$EC(i,this[i]))),this._$EU()}updated(e){}firstUpdated(e){}};ue.elementStyles=[],ue.shadowRootOptions={mode:"open"},ue[ve("elementProperties")]=new Map,ue[ve("finalized")]=new Map,Je==null||Je({ReactiveElement:ue}),(X.reactiveElementVersions??(X.reactiveElementVersions=[])).push("2.0.4");/**
 * @license
 * Copyright 2017 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */const we=globalThis,Ie=we.trustedTypes,Tt=Ie?Ie.createPolicy("lit-html",{createHTML:t=>t}):void 0,Ot="$lit$",ee=`lit$${Math.random().toFixed(9).slice(2)}$`,Rt="?"+ee,Ui=`<${Rt}>`,re=document,Ce=()=>re.createComment(""),$e=t=>t===null||typeof t!="object"&&typeof t!="function",Xe=Array.isArray,Bi=t=>Xe(t)||typeof(t==null?void 0:t[Symbol.iterator])=="function",et=`[ 	
\f\r]`,Se=/<(?:(!--|\/[^a-zA-Z])|(\/?[a-zA-Z][^>\s]*)|(\/?$))/g,It=/-->/g,_t=/>/g,ae=RegExp(`>|${et}(?:([^\\s"'>=/]+)(${et}*=${et}*(?:[^ 	
\f\r"'\`<>=]|("|')|))|$)`,"g"),Ft=/'/g,Lt=/"/g,Nt=/^(?:script|style|textarea|title)$/i,Mt=t=>(e,...i)=>({_$litType$:t,strings:e,values:i}),u=Mt(1),_e=Mt(2),me=Symbol.for("lit-noChange"),_=Symbol.for("lit-nothing"),zt=new WeakMap,le=re.createTreeWalker(re,129);function Ut(t,e){if(!Xe(t)||!t.hasOwnProperty("raw"))throw Error("invalid template strings array");return Tt!==void 0?Tt.createHTML(e):e}const ji=(t,e)=>{const i=t.length-1,o=[];let s,r=e===2?"<svg>":e===3?"<math>":"",n=Se;for(let a=0;a<i;a++){const p=t[a];let c,l,h=-1,v=0;for(;v<p.length&&(n.lastIndex=v,l=n.exec(p),l!==null);)v=n.lastIndex,n===Se?l[1]==="!--"?n=It:l[1]!==void 0?n=_t:l[2]!==void 0?(Nt.test(l[2])&&(s=RegExp("</"+l[2],"g")),n=ae):l[3]!==void 0&&(n=ae):n===ae?l[0]===">"?(n=s??Se,h=-1):l[1]===void 0?h=-2:(h=n.lastIndex-l[2].length,c=l[1],n=l[3]===void 0?ae:l[3]==='"'?Lt:Ft):n===Lt||n===Ft?n=ae:n===It||n===_t?n=Se:(n=ae,s=void 0);const C=n===ae&&t[a+1].startsWith("/>")?" ":"";r+=n===Se?p+Ui:h>=0?(o.push(c),p.slice(0,h)+Ot+p.slice(h)+ee+C):p+ee+(h===-2?a:C)}return[Ut(t,r+(t[i]||"<?>")+(e===2?"</svg>":e===3?"</math>":"")),o]};class Pe{constructor({strings:e,_$litType$:i},o){let s;this.parts=[];let r=0,n=0;const a=e.length-1,p=this.parts,[c,l]=ji(e,i);if(this.el=Pe.createElement(c,o),le.currentNode=this.el.content,i===2||i===3){const h=this.el.content.firstChild;h.replaceWith(...h.childNodes)}for(;(s=le.nextNode())!==null&&p.length<a;){if(s.nodeType===1){if(s.hasAttributes())for(const h of s.getAttributeNames())if(h.endsWith(Ot)){const v=l[n++],C=s.getAttribute(h).split(ee),f=/([.?@])?(.*)/.exec(v);p.push({type:1,index:r,name:f[2],strings:C,ctor:f[1]==="."?Vi:f[1]==="?"?Hi:f[1]==="@"?Gi:Fe}),s.removeAttribute(h)}else h.startsWith(ee)&&(p.push({type:6,index:r}),s.removeAttribute(h));if(Nt.test(s.tagName)){const h=s.textContent.split(ee),v=h.length-1;if(v>0){s.textContent=Ie?Ie.emptyScript:"";for(let C=0;C<v;C++)s.append(h[C],Ce()),le.nextNode(),p.push({type:2,index:++r});s.append(h[v],Ce())}}}else if(s.nodeType===8)if(s.data===Rt)p.push({type:2,index:r});else{let h=-1;for(;(h=s.data.indexOf(ee,h+1))!==-1;)p.push({type:7,index:r}),h+=ee.length-1}r++}}static createElement(e,i){const o=re.createElement("template");return o.innerHTML=e,o}}function fe(t,e,i=t,o){var n,a;if(e===me)return e;let s=o!==void 0?(n=i._$Co)==null?void 0:n[o]:i._$Cl;const r=$e(e)?void 0:e._$litDirective$;return(s==null?void 0:s.constructor)!==r&&((a=s==null?void 0:s._$AO)==null||a.call(s,!1),r===void 0?s=void 0:(s=new r(t),s._$AT(t,i,o)),o!==void 0?(i._$Co??(i._$Co=[]))[o]=s:i._$Cl=s),s!==void 0&&(e=fe(t,s._$AS(t,e.values),s,o)),e}class qi{constructor(e,i){this._$AV=[],this._$AN=void 0,this._$AD=e,this._$AM=i}get parentNode(){return this._$AM.parentNode}get _$AU(){return this._$AM._$AU}u(e){const{el:{content:i},parts:o}=this._$AD,s=((e==null?void 0:e.creationScope)??re).importNode(i,!0);le.currentNode=s;let r=le.nextNode(),n=0,a=0,p=o[0];for(;p!==void 0;){if(n===p.index){let c;p.type===2?c=new ke(r,r.nextSibling,this,e):p.type===1?c=new p.ctor(r,p.name,p.strings,this,e):p.type===6&&(c=new Qi(r,this,e)),this._$AV.push(c),p=o[++a]}n!==(p==null?void 0:p.index)&&(r=le.nextNode(),n++)}return le.currentNode=re,s}p(e){let i=0;for(const o of this._$AV)o!==void 0&&(o.strings!==void 0?(o._$AI(e,o,i),i+=o.strings.length-2):o._$AI(e[i])),i++}}class ke{get _$AU(){var e;return((e=this._$AM)==null?void 0:e._$AU)??this._$Cv}constructor(e,i,o,s){this.type=2,this._$AH=_,this._$AN=void 0,this._$AA=e,this._$AB=i,this._$AM=o,this.options=s,this._$Cv=(s==null?void 0:s.isConnected)??!0}get parentNode(){let e=this._$AA.parentNode;const i=this._$AM;return i!==void 0&&(e==null?void 0:e.nodeType)===11&&(e=i.parentNode),e}get startNode(){return this._$AA}get endNode(){return this._$AB}_$AI(e,i=this){e=fe(this,e,i),$e(e)?e===_||e==null||e===""?(this._$AH!==_&&this._$AR(),this._$AH=_):e!==this._$AH&&e!==me&&this._(e):e._$litType$!==void 0?this.$(e):e.nodeType!==void 0?this.T(e):Bi(e)?this.k(e):this._(e)}O(e){return this._$AA.parentNode.insertBefore(e,this._$AB)}T(e){this._$AH!==e&&(this._$AR(),this._$AH=this.O(e))}_(e){this._$AH!==_&&$e(this._$AH)?this._$AA.nextSibling.data=e:this.T(re.createTextNode(e)),this._$AH=e}$(e){var r;const{values:i,_$litType$:o}=e,s=typeof o=="number"?this._$AC(e):(o.el===void 0&&(o.el=Pe.createElement(Ut(o.h,o.h[0]),this.options)),o);if(((r=this._$AH)==null?void 0:r._$AD)===s)this._$AH.p(i);else{const n=new qi(s,this),a=n.u(this.options);n.p(i),this.T(a),this._$AH=n}}_$AC(e){let i=zt.get(e.strings);return i===void 0&&zt.set(e.strings,i=new Pe(e)),i}k(e){Xe(this._$AH)||(this._$AH=[],this._$AR());const i=this._$AH;let o,s=0;for(const r of e)s===i.length?i.push(o=new ke(this.O(Ce()),this.O(Ce()),this,this.options)):o=i[s],o._$AI(r),s++;s<i.length&&(this._$AR(o&&o._$AB.nextSibling,s),i.length=s)}_$AR(e=this._$AA.nextSibling,i){var o;for((o=this._$AP)==null?void 0:o.call(this,!1,!0,i);e&&e!==this._$AB;){const s=e.nextSibling;e.remove(),e=s}}setConnected(e){var i;this._$AM===void 0&&(this._$Cv=e,(i=this._$AP)==null||i.call(this,e))}}class Fe{get tagName(){return this.element.tagName}get _$AU(){return this._$AM._$AU}constructor(e,i,o,s,r){this.type=1,this._$AH=_,this._$AN=void 0,this.element=e,this.name=i,this._$AM=s,this.options=r,o.length>2||o[0]!==""||o[1]!==""?(this._$AH=Array(o.length-1).fill(new String),this.strings=o):this._$AH=_}_$AI(e,i=this,o,s){const r=this.strings;let n=!1;if(r===void 0)e=fe(this,e,i,0),n=!$e(e)||e!==this._$AH&&e!==me,n&&(this._$AH=e);else{const a=e;let p,c;for(e=r[0],p=0;p<r.length-1;p++)c=fe(this,a[o+p],i,p),c===me&&(c=this._$AH[p]),n||(n=!$e(c)||c!==this._$AH[p]),c===_?e=_:e!==_&&(e+=(c??"")+r[p+1]),this._$AH[p]=c}n&&!s&&this.j(e)}j(e){e===_?this.element.removeAttribute(this.name):this.element.setAttribute(this.name,e??"")}}class Vi extends Fe{constructor(){super(...arguments),this.type=3}j(e){this.element[this.name]=e===_?void 0:e}}class Hi extends Fe{constructor(){super(...arguments),this.type=4}j(e){this.element.toggleAttribute(this.name,!!e&&e!==_)}}class Gi extends Fe{constructor(e,i,o,s,r){super(e,i,o,s,r),this.type=5}_$AI(e,i=this){if((e=fe(this,e,i,0)??_)===me)return;const o=this._$AH,s=e===_&&o!==_||e.capture!==o.capture||e.once!==o.once||e.passive!==o.passive,r=e!==_&&(o===_||s);s&&this.element.removeEventListener(this.name,this,o),r&&this.element.addEventListener(this.name,this,e),this._$AH=e}handleEvent(e){var i;typeof this._$AH=="function"?this._$AH.call(((i=this.options)==null?void 0:i.host)??this.element,e):this._$AH.handleEvent(e)}}class Qi{constructor(e,i,o){this.element=e,this.type=6,this._$AN=void 0,this._$AM=i,this.options=o}get _$AU(){return this._$AM._$AU}_$AI(e){fe(this,e)}}const tt=we.litHtmlPolyfillSupport;tt==null||tt(Pe,ke),(we.litHtmlVersions??(we.litHtmlVersions=[])).push("3.2.1");const Wi=(t,e,i)=>{const o=(i==null?void 0:i.renderBefore)??e;let s=o._$litPart$;if(s===void 0){const r=(i==null?void 0:i.renderBefore)??null;o._$litPart$=s=new ke(e.insertBefore(Ce(),r),r,void 0,i??{})}return s._$AI(t),s};/**
 * @license
 * Copyright 2017 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */let R=class extends ue{constructor(){super(...arguments),this.renderOptions={host:this},this._$Do=void 0}createRenderRoot(){var i;const e=super.createRenderRoot();return(i=this.renderOptions).renderBefore??(i.renderBefore=e.firstChild),e}update(e){const i=this.render();this.hasUpdated||(this.renderOptions.isConnected=this.isConnected),super.update(e),this._$Do=Wi(i,this.renderRoot,this.renderOptions)}connectedCallback(){var e;super.connectedCallback(),(e=this._$Do)==null||e.setConnected(!0)}disconnectedCallback(){var e;super.disconnectedCallback(),(e=this._$Do)==null||e.setConnected(!1)}render(){return me}};R._$litElement$=!0,R.finalized=!0,(Ei=globalThis.litElementHydrateSupport)==null||Ei.call(globalThis,{LitElement:R});const it=globalThis.litElementPolyfillSupport;it==null||it({LitElement:R}),(globalThis.litElementVersions??(globalThis.litElementVersions=[])).push("4.1.1");/**
 * @license
 * Copyright 2017 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */const M=t=>(e,i)=>{i!==void 0?i.addInitializer(()=>{customElements.define(t,e)}):customElements.define(t,e)};/**
 * @license
 * Copyright 2017 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */const Zi={attribute:!0,type:String,converter:Re,reflect:!1,hasChanged:Ke},Yi=(t=Zi,e,i)=>{const{kind:o,metadata:s}=i;let r=globalThis.litPropertyMetadata.get(s);if(r===void 0&&globalThis.litPropertyMetadata.set(s,r=new Map),r.set(i.name,t),o==="accessor"){const{name:n}=i;return{set(a){const p=e.get.call(this);e.set.call(this,a),this.requestUpdate(n,p,t)},init(a){return a!==void 0&&this.P(n,void 0,t),a}}}if(o==="setter"){const{name:n}=i;return function(a){const p=this[n];e.call(this,a),this.requestUpdate(n,p,t)}}throw Error("Unsupported decorator location: "+o)};function b(t){return(e,i)=>typeof i=="object"?Yi(t,e,i):((o,s,r)=>{const n=s.hasOwnProperty(r);return s.constructor.createProperty(r,n?{...o,wrapped:!0}:o),n?Object.getOwnPropertyDescriptor(s,r):void 0})(t,e,i)}/**
 * @license
 * Copyright 2017 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */function m(t){return b({...t,state:!0,attribute:!1})}/**
 * @license
 * Copyright 2017 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */const Ji=(t,e,i)=>(i.configurable=!0,i.enumerable=!0,Reflect.decorate&&typeof e!="object"&&Object.defineProperty(t,e,i),i);/**
 * @license
 * Copyright 2017 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */function Le(t,e){return(i,o,s)=>{const r=n=>{var a;return((a=n.renderRoot)==null?void 0:a.querySelector(t))??null};return Ji(i,o,{get(){return r(this)}})}}const Ki=N`
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
`;var Xi=Object.defineProperty,eo=Object.getOwnPropertyDescriptor,to=(t,e,i,o)=>{for(var s=o>1?void 0:o?eo(e,i):e,r=t.length-1,n;r>=0;r--)(n=t[r])&&(s=(o?n(e,i,s):n(s))||s);return o&&s&&Xi(e,i,s),s};let Bt=class extends R{static get styles(){return[Ki]}async connectedCallback(){super.connectedCallback(),await super.updateComplete}completeSvg(){return _e`
    <svg width="40" height="40" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path fill-rule="evenodd" clip-rule="evenodd" d="M10 20C4.47667 20 0 15.5233 0 10C0 4.47667 4.47667 0 10 0C15.5233 0 20 4.47667 20 10C20 15.5233 15.5233 20 10 20Z" fill="#12B76A"/>
      <path d="M13.6108 8.33337L8.74967 13.1945L5.83301 10.2778" stroke="#F6FEF9" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
    `}render(){return u`
      <div class="container">
        ${this.completeSvg()}
        <p>Pagamento Cancelado</p>
      </div>
    `}};Bt=to([M("message-callback")],Bt);const io=N`
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
`;var oo=Object.defineProperty,so=Object.getOwnPropertyDescriptor,ot=(t,e,i,o)=>{for(var s=o>1?void 0:o?so(e,i):e,r=t.length-1,n;r>=0;r--)(n=t[r])&&(s=(o?n(e,i,s):n(s))||s);return o&&s&&oo(e,i,s),s};let De=class extends R{constructor(){super(...arguments),this.TrackingCode="",this.isActiveClipBoard=!1}copyText(){navigator.clipboard.writeText(this.TrackingCode),this.isActiveClipBoard=!0,setTimeout(()=>{this.isActiveClipBoard=!1},1e3)}render(){return u`
      <div
        @click=${this.TrackingCode!=null?this.copyText:null}
        title="Copiar"
        class="clipBoard ${this.isActiveClipBoard?"active":""}"
      >
        <button class="trackingCode">${this.TrackingCode}</button>
      </div>
    `}};De.styles=[io],ot([b({type:String})],De.prototype,"TrackingCode",2),ot([m()],De.prototype,"isActiveClipBoard",2),De=ot([M("tracking-code-table")],De);const no=N`
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
`;var ro=Object.defineProperty,ao=Object.getOwnPropertyDescriptor,st=(t,e,i,o)=>{for(var s=o>1?void 0:o?ao(e,i):e,r=t.length-1,n;r>=0;r--)(n=t[r])&&(s=(o?n(e,i,s):n(s))||s);return o&&s&&ro(e,i,s),s};let Ne=class extends R{constructor(){super(...arguments),this.isCloseButton=!0}static get styles(){return[no]}render(){const e=u`
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
    `;return u`
      <div class="overlay" id="over">
        <div class=${"container lg"}>
          <div class="headerModal">
            <h1>${this.title}</h1>
            ${this.isCloseButton?u`<button @click=${this.handleOnModalCard}>
                  ${e}
                </button>`:null}
          </div>
          <div class="mainModal">
            <slot></slot>
          </div>
        </div>
      </div>
    `}handleOnModalCard(){const e=new CustomEvent("my-close-modal");this.dispatchEvent(e)}};st([b()],Ne.prototype,"title",2),st([b()],Ne.prototype,"isCloseButton",2),Ne=st([M("payment-online-modal")],Ne);const lo=N`
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
`;function jt(t,e){return function(){return t.apply(e,arguments)}}const{toString:co}=Object.prototype,{getPrototypeOf:nt}=Object,Me=(t=>e=>{const i=co.call(e);return t[i]||(t[i]=i.slice(8,-1).toLowerCase())})(Object.create(null)),G=t=>(t=t.toLowerCase(),e=>Me(e)===t),ze=t=>e=>typeof e===t,{isArray:ge}=Array,Ae=ze("undefined");function po(t){return t!==null&&!Ae(t)&&t.constructor!==null&&!Ae(t.constructor)&&q(t.constructor.isBuffer)&&t.constructor.isBuffer(t)}const qt=G("ArrayBuffer");function ho(t){let e;return typeof ArrayBuffer<"u"&&ArrayBuffer.isView?e=ArrayBuffer.isView(t):e=t&&t.buffer&&qt(t.buffer),e}const uo=ze("string"),q=ze("function"),Vt=ze("number"),Ue=t=>t!==null&&typeof t=="object",mo=t=>t===!0||t===!1,Be=t=>{if(Me(t)!=="object")return!1;const e=nt(t);return(e===null||e===Object.prototype||Object.getPrototypeOf(e)===null)&&!(Symbol.toStringTag in t)&&!(Symbol.iterator in t)},fo=G("Date"),go=G("File"),bo=G("Blob"),yo=G("FileList"),xo=t=>Ue(t)&&q(t.pipe),vo=t=>{let e;return t&&(typeof FormData=="function"&&t instanceof FormData||q(t.append)&&((e=Me(t))==="formdata"||e==="object"&&q(t.toString)&&t.toString()==="[object FormData]"))},wo=G("URLSearchParams"),[Co,$o,So,Po]=["ReadableStream","Request","Response","Headers"].map(G),ko=t=>t.trim?t.trim():t.replace(/^[\s\uFEFF\xA0]+|[\s\uFEFF\xA0]+$/g,"");function Ee(t,e,{allOwnKeys:i=!1}={}){if(t===null||typeof t>"u")return;let o,s;if(typeof t!="object"&&(t=[t]),ge(t))for(o=0,s=t.length;o<s;o++)e.call(null,t[o],o,t);else{const r=i?Object.getOwnPropertyNames(t):Object.keys(t),n=r.length;let a;for(o=0;o<n;o++)a=r[o],e.call(null,t[a],a,t)}}function Ht(t,e){e=e.toLowerCase();const i=Object.keys(t);let o=i.length,s;for(;o-- >0;)if(s=i[o],e===s.toLowerCase())return s;return null}const de=typeof globalThis<"u"?globalThis:typeof self<"u"?self:typeof window<"u"?window:global,Gt=t=>!Ae(t)&&t!==de;function rt(){const{caseless:t}=Gt(this)&&this||{},e={},i=(o,s)=>{const r=t&&Ht(e,s)||s;Be(e[r])&&Be(o)?e[r]=rt(e[r],o):Be(o)?e[r]=rt({},o):ge(o)?e[r]=o.slice():e[r]=o};for(let o=0,s=arguments.length;o<s;o++)arguments[o]&&Ee(arguments[o],i);return e}const Do=(t,e,i,{allOwnKeys:o}={})=>(Ee(e,(s,r)=>{i&&q(s)?t[r]=jt(s,i):t[r]=s},{allOwnKeys:o}),t),Ao=t=>(t.charCodeAt(0)===65279&&(t=t.slice(1)),t),Eo=(t,e,i,o)=>{t.prototype=Object.create(e.prototype,o),t.prototype.constructor=t,Object.defineProperty(t,"super",{value:e.prototype}),i&&Object.assign(t.prototype,i)},To=(t,e,i,o)=>{let s,r,n;const a={};if(e=e||{},t==null)return e;do{for(s=Object.getOwnPropertyNames(t),r=s.length;r-- >0;)n=s[r],(!o||o(n,t,e))&&!a[n]&&(e[n]=t[n],a[n]=!0);t=i!==!1&&nt(t)}while(t&&(!i||i(t,e))&&t!==Object.prototype);return e},Oo=(t,e,i)=>{t=String(t),(i===void 0||i>t.length)&&(i=t.length),i-=e.length;const o=t.indexOf(e,i);return o!==-1&&o===i},Ro=t=>{if(!t)return null;if(ge(t))return t;let e=t.length;if(!Vt(e))return null;const i=new Array(e);for(;e-- >0;)i[e]=t[e];return i},Io=(t=>e=>t&&e instanceof t)(typeof Uint8Array<"u"&&nt(Uint8Array)),_o=(t,e)=>{const o=(t&&t[Symbol.iterator]).call(t);let s;for(;(s=o.next())&&!s.done;){const r=s.value;e.call(t,r[0],r[1])}},Fo=(t,e)=>{let i;const o=[];for(;(i=t.exec(e))!==null;)o.push(i);return o},Lo=G("HTMLFormElement"),No=t=>t.toLowerCase().replace(/[-_\s]([a-z\d])(\w*)/g,function(i,o,s){return o.toUpperCase()+s}),Qt=(({hasOwnProperty:t})=>(e,i)=>t.call(e,i))(Object.prototype),Mo=G("RegExp"),Wt=(t,e)=>{const i=Object.getOwnPropertyDescriptors(t),o={};Ee(i,(s,r)=>{let n;(n=e(s,r,t))!==!1&&(o[r]=n||s)}),Object.defineProperties(t,o)},zo=t=>{Wt(t,(e,i)=>{if(q(t)&&["arguments","caller","callee"].indexOf(i)!==-1)return!1;const o=t[i];if(q(o)){if(e.enumerable=!1,"writable"in e){e.writable=!1;return}e.set||(e.set=()=>{throw Error("Can not rewrite read-only method '"+i+"'")})}})},Uo=(t,e)=>{const i={},o=s=>{s.forEach(r=>{i[r]=!0})};return ge(t)?o(t):o(String(t).split(e)),i},Bo=()=>{},jo=(t,e)=>t!=null&&Number.isFinite(t=+t)?t:e,at="abcdefghijklmnopqrstuvwxyz",Zt="0123456789",Yt={DIGIT:Zt,ALPHA:at,ALPHA_DIGIT:at+at.toUpperCase()+Zt},qo=(t=16,e=Yt.ALPHA_DIGIT)=>{let i="";const{length:o}=e;for(;t--;)i+=e[Math.random()*o|0];return i};function Vo(t){return!!(t&&q(t.append)&&t[Symbol.toStringTag]==="FormData"&&t[Symbol.iterator])}const Ho=t=>{const e=new Array(10),i=(o,s)=>{if(Ue(o)){if(e.indexOf(o)>=0)return;if(!("toJSON"in o)){e[s]=o;const r=ge(o)?[]:{};return Ee(o,(n,a)=>{const p=i(n,s+1);!Ae(p)&&(r[a]=p)}),e[s]=void 0,r}}return o};return i(t,0)},Go=G("AsyncFunction"),Qo=t=>t&&(Ue(t)||q(t))&&q(t.then)&&q(t.catch),Jt=((t,e)=>t?setImmediate:e?((i,o)=>(de.addEventListener("message",({source:s,data:r})=>{s===de&&r===i&&o.length&&o.shift()()},!1),s=>{o.push(s),de.postMessage(i,"*")}))(`axios@${Math.random()}`,[]):i=>setTimeout(i))(typeof setImmediate=="function",q(de.postMessage)),Wo=typeof queueMicrotask<"u"?queueMicrotask.bind(de):typeof process<"u"&&process.nextTick||Jt,d={isArray:ge,isArrayBuffer:qt,isBuffer:po,isFormData:vo,isArrayBufferView:ho,isString:uo,isNumber:Vt,isBoolean:mo,isObject:Ue,isPlainObject:Be,isReadableStream:Co,isRequest:$o,isResponse:So,isHeaders:Po,isUndefined:Ae,isDate:fo,isFile:go,isBlob:bo,isRegExp:Mo,isFunction:q,isStream:xo,isURLSearchParams:wo,isTypedArray:Io,isFileList:yo,forEach:Ee,merge:rt,extend:Do,trim:ko,stripBOM:Ao,inherits:Eo,toFlatObject:To,kindOf:Me,kindOfTest:G,endsWith:Oo,toArray:Ro,forEachEntry:_o,matchAll:Fo,isHTMLForm:Lo,hasOwnProperty:Qt,hasOwnProp:Qt,reduceDescriptors:Wt,freezeMethods:zo,toObjectSet:Uo,toCamelCase:No,noop:Bo,toFiniteNumber:jo,findKey:Ht,global:de,isContextDefined:Gt,ALPHABET:Yt,generateString:qo,isSpecCompliantForm:Vo,toJSONObject:Ho,isAsyncFn:Go,isThenable:Qo,setImmediate:Jt,asap:Wo};function y(t,e,i,o,s){Error.call(this),Error.captureStackTrace?Error.captureStackTrace(this,this.constructor):this.stack=new Error().stack,this.message=t,this.name="AxiosError",e&&(this.code=e),i&&(this.config=i),o&&(this.request=o),s&&(this.response=s,this.status=s.status?s.status:null)}d.inherits(y,Error,{toJSON:function(){return{message:this.message,name:this.name,description:this.description,number:this.number,fileName:this.fileName,lineNumber:this.lineNumber,columnNumber:this.columnNumber,stack:this.stack,config:d.toJSONObject(this.config),code:this.code,status:this.status}}});const Kt=y.prototype,Xt={};["ERR_BAD_OPTION_VALUE","ERR_BAD_OPTION","ECONNABORTED","ETIMEDOUT","ERR_NETWORK","ERR_FR_TOO_MANY_REDIRECTS","ERR_DEPRECATED","ERR_BAD_RESPONSE","ERR_BAD_REQUEST","ERR_CANCELED","ERR_NOT_SUPPORT","ERR_INVALID_URL"].forEach(t=>{Xt[t]={value:t}}),Object.defineProperties(y,Xt),Object.defineProperty(Kt,"isAxiosError",{value:!0}),y.from=(t,e,i,o,s,r)=>{const n=Object.create(Kt);return d.toFlatObject(t,n,function(p){return p!==Error.prototype},a=>a!=="isAxiosError"),y.call(n,t.message,e,i,o,s),n.cause=t,n.name=t.name,r&&Object.assign(n,r),n};const Zo=null;function lt(t){return d.isPlainObject(t)||d.isArray(t)}function ei(t){return d.endsWith(t,"[]")?t.slice(0,-2):t}function ti(t,e,i){return t?t.concat(e).map(function(s,r){return s=ei(s),!i&&r?"["+s+"]":s}).join(i?".":""):e}function Yo(t){return d.isArray(t)&&!t.some(lt)}const Jo=d.toFlatObject(d,{},null,function(e){return/^is[A-Z]/.test(e)});function je(t,e,i){if(!d.isObject(t))throw new TypeError("target must be an object");e=e||new FormData,i=d.toFlatObject(i,{metaTokens:!0,dots:!1,indexes:!1},!1,function(x,g){return!d.isUndefined(g[x])});const o=i.metaTokens,s=i.visitor||l,r=i.dots,n=i.indexes,p=(i.Blob||typeof Blob<"u"&&Blob)&&d.isSpecCompliantForm(e);if(!d.isFunction(s))throw new TypeError("visitor must be a function");function c(f){if(f===null)return"";if(d.isDate(f))return f.toISOString();if(!p&&d.isBlob(f))throw new y("Blob is not supported. Use a Buffer instead.");return d.isArrayBuffer(f)||d.isTypedArray(f)?p&&typeof Blob=="function"?new Blob([f]):Buffer.from(f):f}function l(f,x,g){let O=f;if(f&&!g&&typeof f=="object"){if(d.endsWith(x,"{}"))x=o?x:x.slice(0,-2),f=JSON.stringify(f);else if(d.isArray(f)&&Yo(f)||(d.isFileList(f)||d.endsWith(x,"[]"))&&(O=d.toArray(f)))return x=ei(x),O.forEach(function(F,K){!(d.isUndefined(F)||F===null)&&e.append(n===!0?ti([x],K,r):n===null?x:x+"[]",c(F))}),!1}return lt(f)?!0:(e.append(ti(g,x,r),c(f)),!1)}const h=[],v=Object.assign(Jo,{defaultVisitor:l,convertValue:c,isVisitable:lt});function C(f,x){if(!d.isUndefined(f)){if(h.indexOf(f)!==-1)throw Error("Circular reference detected in "+x.join("."));h.push(f),d.forEach(f,function(O,I){(!(d.isUndefined(O)||O===null)&&s.call(e,O,d.isString(I)?I.trim():I,x,v))===!0&&C(O,x?x.concat(I):[I])}),h.pop()}}if(!d.isObject(t))throw new TypeError("data must be an object");return C(t),e}function ii(t){const e={"!":"%21","'":"%27","(":"%28",")":"%29","~":"%7E","%20":"+","%00":"\0"};return encodeURIComponent(t).replace(/[!'()~]|%20|%00/g,function(o){return e[o]})}function dt(t,e){this._pairs=[],t&&je(t,this,e)}const oi=dt.prototype;oi.append=function(e,i){this._pairs.push([e,i])},oi.toString=function(e){const i=e?function(o){return e.call(this,o,ii)}:ii;return this._pairs.map(function(s){return i(s[0])+"="+i(s[1])},"").join("&")};function Ko(t){return encodeURIComponent(t).replace(/%3A/gi,":").replace(/%24/g,"$").replace(/%2C/gi,",").replace(/%20/g,"+").replace(/%5B/gi,"[").replace(/%5D/gi,"]")}function si(t,e,i){if(!e)return t;const o=i&&i.encode||Ko,s=i&&i.serialize;let r;if(s?r=s(e,i):r=d.isURLSearchParams(e)?e.toString():new dt(e,i).toString(o),r){const n=t.indexOf("#");n!==-1&&(t=t.slice(0,n)),t+=(t.indexOf("?")===-1?"?":"&")+r}return t}class ni{constructor(){this.handlers=[]}use(e,i,o){return this.handlers.push({fulfilled:e,rejected:i,synchronous:o?o.synchronous:!1,runWhen:o?o.runWhen:null}),this.handlers.length-1}eject(e){this.handlers[e]&&(this.handlers[e]=null)}clear(){this.handlers&&(this.handlers=[])}forEach(e){d.forEach(this.handlers,function(o){o!==null&&e(o)})}}const ri={silentJSONParsing:!0,forcedJSONParsing:!0,clarifyTimeoutError:!1},Xo={isBrowser:!0,classes:{URLSearchParams:typeof URLSearchParams<"u"?URLSearchParams:dt,FormData:typeof FormData<"u"?FormData:null,Blob:typeof Blob<"u"?Blob:null},protocols:["http","https","file","blob","url","data"]},ct=typeof window<"u"&&typeof document<"u",pt=typeof navigator=="object"&&navigator||void 0,es=ct&&(!pt||["ReactNative","NativeScript","NS"].indexOf(pt.product)<0),ts=typeof WorkerGlobalScope<"u"&&self instanceof WorkerGlobalScope&&typeof self.importScripts=="function",is=ct&&window.location.href||"http://localhost",U={...Object.freeze(Object.defineProperty({__proto__:null,hasBrowserEnv:ct,hasStandardBrowserEnv:es,hasStandardBrowserWebWorkerEnv:ts,navigator:pt,origin:is},Symbol.toStringTag,{value:"Module"})),...Xo};function os(t,e){return je(t,new U.classes.URLSearchParams,Object.assign({visitor:function(i,o,s,r){return U.isNode&&d.isBuffer(i)?(this.append(o,i.toString("base64")),!1):r.defaultVisitor.apply(this,arguments)}},e))}function ss(t){return d.matchAll(/\w+|\[(\w*)]/g,t).map(e=>e[0]==="[]"?"":e[1]||e[0])}function ns(t){const e={},i=Object.keys(t);let o;const s=i.length;let r;for(o=0;o<s;o++)r=i[o],e[r]=t[r];return e}function ai(t){function e(i,o,s,r){let n=i[r++];if(n==="__proto__")return!0;const a=Number.isFinite(+n),p=r>=i.length;return n=!n&&d.isArray(s)?s.length:n,p?(d.hasOwnProp(s,n)?s[n]=[s[n],o]:s[n]=o,!a):((!s[n]||!d.isObject(s[n]))&&(s[n]=[]),e(i,o,s[n],r)&&d.isArray(s[n])&&(s[n]=ns(s[n])),!a)}if(d.isFormData(t)&&d.isFunction(t.entries)){const i={};return d.forEachEntry(t,(o,s)=>{e(ss(o),s,i,0)}),i}return null}function rs(t,e,i){if(d.isString(t))try{return(e||JSON.parse)(t),d.trim(t)}catch(o){if(o.name!=="SyntaxError")throw o}return(0,JSON.stringify)(t)}const Te={transitional:ri,adapter:["xhr","http","fetch"],transformRequest:[function(e,i){const o=i.getContentType()||"",s=o.indexOf("application/json")>-1,r=d.isObject(e);if(r&&d.isHTMLForm(e)&&(e=new FormData(e)),d.isFormData(e))return s?JSON.stringify(ai(e)):e;if(d.isArrayBuffer(e)||d.isBuffer(e)||d.isStream(e)||d.isFile(e)||d.isBlob(e)||d.isReadableStream(e))return e;if(d.isArrayBufferView(e))return e.buffer;if(d.isURLSearchParams(e))return i.setContentType("application/x-www-form-urlencoded;charset=utf-8",!1),e.toString();let a;if(r){if(o.indexOf("application/x-www-form-urlencoded")>-1)return os(e,this.formSerializer).toString();if((a=d.isFileList(e))||o.indexOf("multipart/form-data")>-1){const p=this.env&&this.env.FormData;return je(a?{"files[]":e}:e,p&&new p,this.formSerializer)}}return r||s?(i.setContentType("application/json",!1),rs(e)):e}],transformResponse:[function(e){const i=this.transitional||Te.transitional,o=i&&i.forcedJSONParsing,s=this.responseType==="json";if(d.isResponse(e)||d.isReadableStream(e))return e;if(e&&d.isString(e)&&(o&&!this.responseType||s)){const n=!(i&&i.silentJSONParsing)&&s;try{return JSON.parse(e)}catch(a){if(n)throw a.name==="SyntaxError"?y.from(a,y.ERR_BAD_RESPONSE,this,null,this.response):a}}return e}],timeout:0,xsrfCookieName:"XSRF-TOKEN",xsrfHeaderName:"X-XSRF-TOKEN",maxContentLength:-1,maxBodyLength:-1,env:{FormData:U.classes.FormData,Blob:U.classes.Blob},validateStatus:function(e){return e>=200&&e<300},headers:{common:{Accept:"application/json, text/plain, */*","Content-Type":void 0}}};d.forEach(["delete","get","head","post","put","patch"],t=>{Te.headers[t]={}});const as=d.toObjectSet(["age","authorization","content-length","content-type","etag","expires","from","host","if-modified-since","if-unmodified-since","last-modified","location","max-forwards","proxy-authorization","referer","retry-after","user-agent"]),ls=t=>{const e={};let i,o,s;return t&&t.split(`
`).forEach(function(n){s=n.indexOf(":"),i=n.substring(0,s).trim().toLowerCase(),o=n.substring(s+1).trim(),!(!i||e[i]&&as[i])&&(i==="set-cookie"?e[i]?e[i].push(o):e[i]=[o]:e[i]=e[i]?e[i]+", "+o:o)}),e},li=Symbol("internals");function Oe(t){return t&&String(t).trim().toLowerCase()}function qe(t){return t===!1||t==null?t:d.isArray(t)?t.map(qe):String(t)}function ds(t){const e=Object.create(null),i=/([^\s,;=]+)\s*(?:=\s*([^,;]+))?/g;let o;for(;o=i.exec(t);)e[o[1]]=o[2];return e}const cs=t=>/^[-_a-zA-Z0-9^`|~,!#$%&'*+.]+$/.test(t.trim());function ht(t,e,i,o,s){if(d.isFunction(o))return o.call(this,e,i);if(s&&(e=i),!!d.isString(e)){if(d.isString(o))return e.indexOf(o)!==-1;if(d.isRegExp(o))return o.test(e)}}function ps(t){return t.trim().toLowerCase().replace(/([a-z\d])(\w*)/g,(e,i,o)=>i.toUpperCase()+o)}function hs(t,e){const i=d.toCamelCase(" "+e);["get","set","has"].forEach(o=>{Object.defineProperty(t,o+i,{value:function(s,r,n){return this[o].call(this,e,s,r,n)},configurable:!0})})}class B{constructor(e){e&&this.set(e)}set(e,i,o){const s=this;function r(a,p,c){const l=Oe(p);if(!l)throw new Error("header name must be a non-empty string");const h=d.findKey(s,l);(!h||s[h]===void 0||c===!0||c===void 0&&s[h]!==!1)&&(s[h||p]=qe(a))}const n=(a,p)=>d.forEach(a,(c,l)=>r(c,l,p));if(d.isPlainObject(e)||e instanceof this.constructor)n(e,i);else if(d.isString(e)&&(e=e.trim())&&!cs(e))n(ls(e),i);else if(d.isHeaders(e))for(const[a,p]of e.entries())r(p,a,o);else e!=null&&r(i,e,o);return this}get(e,i){if(e=Oe(e),e){const o=d.findKey(this,e);if(o){const s=this[o];if(!i)return s;if(i===!0)return ds(s);if(d.isFunction(i))return i.call(this,s,o);if(d.isRegExp(i))return i.exec(s);throw new TypeError("parser must be boolean|regexp|function")}}}has(e,i){if(e=Oe(e),e){const o=d.findKey(this,e);return!!(o&&this[o]!==void 0&&(!i||ht(this,this[o],o,i)))}return!1}delete(e,i){const o=this;let s=!1;function r(n){if(n=Oe(n),n){const a=d.findKey(o,n);a&&(!i||ht(o,o[a],a,i))&&(delete o[a],s=!0)}}return d.isArray(e)?e.forEach(r):r(e),s}clear(e){const i=Object.keys(this);let o=i.length,s=!1;for(;o--;){const r=i[o];(!e||ht(this,this[r],r,e,!0))&&(delete this[r],s=!0)}return s}normalize(e){const i=this,o={};return d.forEach(this,(s,r)=>{const n=d.findKey(o,r);if(n){i[n]=qe(s),delete i[r];return}const a=e?ps(r):String(r).trim();a!==r&&delete i[r],i[a]=qe(s),o[a]=!0}),this}concat(...e){return this.constructor.concat(this,...e)}toJSON(e){const i=Object.create(null);return d.forEach(this,(o,s)=>{o!=null&&o!==!1&&(i[s]=e&&d.isArray(o)?o.join(", "):o)}),i}[Symbol.iterator](){return Object.entries(this.toJSON())[Symbol.iterator]()}toString(){return Object.entries(this.toJSON()).map(([e,i])=>e+": "+i).join(`
`)}get[Symbol.toStringTag](){return"AxiosHeaders"}static from(e){return e instanceof this?e:new this(e)}static concat(e,...i){const o=new this(e);return i.forEach(s=>o.set(s)),o}static accessor(e){const o=(this[li]=this[li]={accessors:{}}).accessors,s=this.prototype;function r(n){const a=Oe(n);o[a]||(hs(s,n),o[a]=!0)}return d.isArray(e)?e.forEach(r):r(e),this}}B.accessor(["Content-Type","Content-Length","Accept","Accept-Encoding","User-Agent","Authorization"]),d.reduceDescriptors(B.prototype,({value:t},e)=>{let i=e[0].toUpperCase()+e.slice(1);return{get:()=>t,set(o){this[i]=o}}}),d.freezeMethods(B);function ut(t,e){const i=this||Te,o=e||i,s=B.from(o.headers);let r=o.data;return d.forEach(t,function(a){r=a.call(i,r,s.normalize(),e?e.status:void 0)}),s.normalize(),r}function di(t){return!!(t&&t.__CANCEL__)}function be(t,e,i){y.call(this,t??"canceled",y.ERR_CANCELED,e,i),this.name="CanceledError"}d.inherits(be,y,{__CANCEL__:!0});function ci(t,e,i){const o=i.config.validateStatus;!i.status||!o||o(i.status)?t(i):e(new y("Request failed with status code "+i.status,[y.ERR_BAD_REQUEST,y.ERR_BAD_RESPONSE][Math.floor(i.status/100)-4],i.config,i.request,i))}function us(t){const e=/^([-+\w]{1,25})(:?\/\/|:)/.exec(t);return e&&e[1]||""}function ms(t,e){t=t||10;const i=new Array(t),o=new Array(t);let s=0,r=0,n;return e=e!==void 0?e:1e3,function(p){const c=Date.now(),l=o[r];n||(n=c),i[s]=p,o[s]=c;let h=r,v=0;for(;h!==s;)v+=i[h++],h=h%t;if(s=(s+1)%t,s===r&&(r=(r+1)%t),c-n<e)return;const C=l&&c-l;return C?Math.round(v*1e3/C):void 0}}function fs(t,e){let i=0,o=1e3/e,s,r;const n=(c,l=Date.now())=>{i=l,s=null,r&&(clearTimeout(r),r=null),t.apply(null,c)};return[(...c)=>{const l=Date.now(),h=l-i;h>=o?n(c,l):(s=c,r||(r=setTimeout(()=>{r=null,n(s)},o-h)))},()=>s&&n(s)]}const Ve=(t,e,i=3)=>{let o=0;const s=ms(50,250);return fs(r=>{const n=r.loaded,a=r.lengthComputable?r.total:void 0,p=n-o,c=s(p),l=n<=a;o=n;const h={loaded:n,total:a,progress:a?n/a:void 0,bytes:p,rate:c||void 0,estimated:c&&a&&l?(a-n)/c:void 0,event:r,lengthComputable:a!=null,[e?"download":"upload"]:!0};t(h)},i)},pi=(t,e)=>{const i=t!=null;return[o=>e[0]({lengthComputable:i,total:t,loaded:o}),e[1]]},hi=t=>(...e)=>d.asap(()=>t(...e)),gs=U.hasStandardBrowserEnv?function(){const e=U.navigator&&/(msie|trident)/i.test(U.navigator.userAgent),i=document.createElement("a");let o;function s(r){let n=r;return e&&(i.setAttribute("href",n),n=i.href),i.setAttribute("href",n),{href:i.href,protocol:i.protocol?i.protocol.replace(/:$/,""):"",host:i.host,search:i.search?i.search.replace(/^\?/,""):"",hash:i.hash?i.hash.replace(/^#/,""):"",hostname:i.hostname,port:i.port,pathname:i.pathname.charAt(0)==="/"?i.pathname:"/"+i.pathname}}return o=s(window.location.href),function(n){const a=d.isString(n)?s(n):n;return a.protocol===o.protocol&&a.host===o.host}}():function(){return function(){return!0}}(),bs=U.hasStandardBrowserEnv?{write(t,e,i,o,s,r){const n=[t+"="+encodeURIComponent(e)];d.isNumber(i)&&n.push("expires="+new Date(i).toGMTString()),d.isString(o)&&n.push("path="+o),d.isString(s)&&n.push("domain="+s),r===!0&&n.push("secure"),document.cookie=n.join("; ")},read(t){const e=document.cookie.match(new RegExp("(^|;\\s*)("+t+")=([^;]*)"));return e?decodeURIComponent(e[3]):null},remove(t){this.write(t,"",Date.now()-864e5)}}:{write(){},read(){return null},remove(){}};function ys(t){return/^([a-z][a-z\d+\-.]*:)?\/\//i.test(t)}function xs(t,e){return e?t.replace(/\/?\/$/,"")+"/"+e.replace(/^\/+/,""):t}function ui(t,e){return t&&!ys(e)?xs(t,e):e}const mi=t=>t instanceof B?{...t}:t;function ce(t,e){e=e||{};const i={};function o(c,l,h){return d.isPlainObject(c)&&d.isPlainObject(l)?d.merge.call({caseless:h},c,l):d.isPlainObject(l)?d.merge({},l):d.isArray(l)?l.slice():l}function s(c,l,h){if(d.isUndefined(l)){if(!d.isUndefined(c))return o(void 0,c,h)}else return o(c,l,h)}function r(c,l){if(!d.isUndefined(l))return o(void 0,l)}function n(c,l){if(d.isUndefined(l)){if(!d.isUndefined(c))return o(void 0,c)}else return o(void 0,l)}function a(c,l,h){if(h in e)return o(c,l);if(h in t)return o(void 0,c)}const p={url:r,method:r,data:r,baseURL:n,transformRequest:n,transformResponse:n,paramsSerializer:n,timeout:n,timeoutMessage:n,withCredentials:n,withXSRFToken:n,adapter:n,responseType:n,xsrfCookieName:n,xsrfHeaderName:n,onUploadProgress:n,onDownloadProgress:n,decompress:n,maxContentLength:n,maxBodyLength:n,beforeRedirect:n,transport:n,httpAgent:n,httpsAgent:n,cancelToken:n,socketPath:n,responseEncoding:n,validateStatus:a,headers:(c,l)=>s(mi(c),mi(l),!0)};return d.forEach(Object.keys(Object.assign({},t,e)),function(l){const h=p[l]||s,v=h(t[l],e[l],l);d.isUndefined(v)&&h!==a||(i[l]=v)}),i}const fi=t=>{const e=ce({},t);let{data:i,withXSRFToken:o,xsrfHeaderName:s,xsrfCookieName:r,headers:n,auth:a}=e;e.headers=n=B.from(n),e.url=si(ui(e.baseURL,e.url),t.params,t.paramsSerializer),a&&n.set("Authorization","Basic "+btoa((a.username||"")+":"+(a.password?unescape(encodeURIComponent(a.password)):"")));let p;if(d.isFormData(i)){if(U.hasStandardBrowserEnv||U.hasStandardBrowserWebWorkerEnv)n.setContentType(void 0);else if((p=n.getContentType())!==!1){const[c,...l]=p?p.split(";").map(h=>h.trim()).filter(Boolean):[];n.setContentType([c||"multipart/form-data",...l].join("; "))}}if(U.hasStandardBrowserEnv&&(o&&d.isFunction(o)&&(o=o(e)),o||o!==!1&&gs(e.url))){const c=s&&r&&bs.read(r);c&&n.set(s,c)}return e},vs=typeof XMLHttpRequest<"u"&&function(t){return new Promise(function(i,o){const s=fi(t);let r=s.data;const n=B.from(s.headers).normalize();let{responseType:a,onUploadProgress:p,onDownloadProgress:c}=s,l,h,v,C,f;function x(){C&&C(),f&&f(),s.cancelToken&&s.cancelToken.unsubscribe(l),s.signal&&s.signal.removeEventListener("abort",l)}let g=new XMLHttpRequest;g.open(s.method.toUpperCase(),s.url,!0),g.timeout=s.timeout;function O(){if(!g)return;const F=B.from("getAllResponseHeaders"in g&&g.getAllResponseHeaders()),j={data:!a||a==="text"||a==="json"?g.responseText:g.response,status:g.status,statusText:g.statusText,headers:F,config:t,request:g};ci(function(he){i(he),x()},function(he){o(he),x()},j),g=null}"onloadend"in g?g.onloadend=O:g.onreadystatechange=function(){!g||g.readyState!==4||g.status===0&&!(g.responseURL&&g.responseURL.indexOf("file:")===0)||setTimeout(O)},g.onabort=function(){g&&(o(new y("Request aborted",y.ECONNABORTED,t,g)),g=null)},g.onerror=function(){o(new y("Network Error",y.ERR_NETWORK,t,g)),g=null},g.ontimeout=function(){let K=s.timeout?"timeout of "+s.timeout+"ms exceeded":"timeout exceeded";const j=s.transitional||ri;s.timeoutErrorMessage&&(K=s.timeoutErrorMessage),o(new y(K,j.clarifyTimeoutError?y.ETIMEDOUT:y.ECONNABORTED,t,g)),g=null},r===void 0&&n.setContentType(null),"setRequestHeader"in g&&d.forEach(n.toJSON(),function(K,j){g.setRequestHeader(j,K)}),d.isUndefined(s.withCredentials)||(g.withCredentials=!!s.withCredentials),a&&a!=="json"&&(g.responseType=s.responseType),c&&([v,f]=Ve(c,!0),g.addEventListener("progress",v)),p&&g.upload&&([h,C]=Ve(p),g.upload.addEventListener("progress",h),g.upload.addEventListener("loadend",C)),(s.cancelToken||s.signal)&&(l=F=>{g&&(o(!F||F.type?new be(null,t,g):F),g.abort(),g=null)},s.cancelToken&&s.cancelToken.subscribe(l),s.signal&&(s.signal.aborted?l():s.signal.addEventListener("abort",l)));const I=us(s.url);if(I&&U.protocols.indexOf(I)===-1){o(new y("Unsupported protocol "+I+":",y.ERR_BAD_REQUEST,t));return}g.send(r||null)})},ws=(t,e)=>{const{length:i}=t=t?t.filter(Boolean):[];if(e||i){let o=new AbortController,s;const r=function(c){if(!s){s=!0,a();const l=c instanceof Error?c:this.reason;o.abort(l instanceof y?l:new be(l instanceof Error?l.message:l))}};let n=e&&setTimeout(()=>{n=null,r(new y(`timeout ${e} of ms exceeded`,y.ETIMEDOUT))},e);const a=()=>{t&&(n&&clearTimeout(n),n=null,t.forEach(c=>{c.unsubscribe?c.unsubscribe(r):c.removeEventListener("abort",r)}),t=null)};t.forEach(c=>c.addEventListener("abort",r));const{signal:p}=o;return p.unsubscribe=()=>d.asap(a),p}},Cs=function*(t,e){let i=t.byteLength;if(i<e){yield t;return}let o=0,s;for(;o<i;)s=o+e,yield t.slice(o,s),o=s},$s=async function*(t,e){for await(const i of Ss(t))yield*Cs(i,e)},Ss=async function*(t){if(t[Symbol.asyncIterator]){yield*t;return}const e=t.getReader();try{for(;;){const{done:i,value:o}=await e.read();if(i)break;yield o}}finally{await e.cancel()}},gi=(t,e,i,o)=>{const s=$s(t,e);let r=0,n,a=p=>{n||(n=!0,o&&o(p))};return new ReadableStream({async pull(p){try{const{done:c,value:l}=await s.next();if(c){a(),p.close();return}let h=l.byteLength;if(i){let v=r+=h;i(v)}p.enqueue(new Uint8Array(l))}catch(c){throw a(c),c}},cancel(p){return a(p),s.return()}},{highWaterMark:2})},He=typeof fetch=="function"&&typeof Request=="function"&&typeof Response=="function",bi=He&&typeof ReadableStream=="function",Ps=He&&(typeof TextEncoder=="function"?(t=>e=>t.encode(e))(new TextEncoder):async t=>new Uint8Array(await new Response(t).arrayBuffer())),yi=(t,...e)=>{try{return!!t(...e)}catch{return!1}},ks=bi&&yi(()=>{let t=!1;const e=new Request(U.origin,{body:new ReadableStream,method:"POST",get duplex(){return t=!0,"half"}}).headers.has("Content-Type");return t&&!e}),xi=64*1024,mt=bi&&yi(()=>d.isReadableStream(new Response("").body)),Ge={stream:mt&&(t=>t.body)};He&&(t=>{["text","arrayBuffer","blob","formData","stream"].forEach(e=>{!Ge[e]&&(Ge[e]=d.isFunction(t[e])?i=>i[e]():(i,o)=>{throw new y(`Response type '${e}' is not supported`,y.ERR_NOT_SUPPORT,o)})})})(new Response);const Ds=async t=>{if(t==null)return 0;if(d.isBlob(t))return t.size;if(d.isSpecCompliantForm(t))return(await new Request(U.origin,{method:"POST",body:t}).arrayBuffer()).byteLength;if(d.isArrayBufferView(t)||d.isArrayBuffer(t))return t.byteLength;if(d.isURLSearchParams(t)&&(t=t+""),d.isString(t))return(await Ps(t)).byteLength},As=async(t,e)=>{const i=d.toFiniteNumber(t.getContentLength());return i??Ds(e)},ft={http:Zo,xhr:vs,fetch:He&&(async t=>{let{url:e,method:i,data:o,signal:s,cancelToken:r,timeout:n,onDownloadProgress:a,onUploadProgress:p,responseType:c,headers:l,withCredentials:h="same-origin",fetchOptions:v}=fi(t);c=c?(c+"").toLowerCase():"text";let C=ws([s,r&&r.toAbortSignal()],n),f;const x=C&&C.unsubscribe&&(()=>{C.unsubscribe()});let g;try{if(p&&ks&&i!=="get"&&i!=="head"&&(g=await As(l,o))!==0){let j=new Request(e,{method:"POST",body:o,duplex:"half"}),se;if(d.isFormData(o)&&(se=j.headers.get("content-type"))&&l.setContentType(se),j.body){const[he,We]=pi(g,Ve(hi(p)));o=gi(j.body,xi,he,We)}}d.isString(h)||(h=h?"include":"omit");const O="credentials"in Request.prototype;f=new Request(e,{...v,signal:C,method:i.toUpperCase(),headers:l.normalize().toJSON(),body:o,duplex:"half",credentials:O?h:void 0});let I=await fetch(f);const F=mt&&(c==="stream"||c==="response");if(mt&&(a||F&&x)){const j={};["status","statusText","headers"].forEach(Ti=>{j[Ti]=I[Ti]});const se=d.toFiniteNumber(I.headers.get("content-length")),[he,We]=a&&pi(se,Ve(hi(a),!0))||[];I=new Response(gi(I.body,xi,he,()=>{We&&We(),x&&x()}),j)}c=c||"text";let K=await Ge[d.findKey(Ge,c)||"text"](I,t);return!F&&x&&x(),await new Promise((j,se)=>{ci(j,se,{data:K,headers:B.from(I.headers),status:I.status,statusText:I.statusText,config:t,request:f})})}catch(O){throw x&&x(),O&&O.name==="TypeError"&&/fetch/i.test(O.message)?Object.assign(new y("Network Error",y.ERR_NETWORK,t,f),{cause:O.cause||O}):y.from(O,O&&O.code,t,f)}})};d.forEach(ft,(t,e)=>{if(t){try{Object.defineProperty(t,"name",{value:e})}catch{}Object.defineProperty(t,"adapterName",{value:e})}});const vi=t=>`- ${t}`,Es=t=>d.isFunction(t)||t===null||t===!1,wi={getAdapter:t=>{t=d.isArray(t)?t:[t];const{length:e}=t;let i,o;const s={};for(let r=0;r<e;r++){i=t[r];let n;if(o=i,!Es(i)&&(o=ft[(n=String(i)).toLowerCase()],o===void 0))throw new y(`Unknown adapter '${n}'`);if(o)break;s[n||"#"+r]=o}if(!o){const r=Object.entries(s).map(([a,p])=>`adapter ${a} `+(p===!1?"is not supported by the environment":"is not available in the build"));let n=e?r.length>1?`since :
`+r.map(vi).join(`
`):" "+vi(r[0]):"as no adapter specified";throw new y("There is no suitable adapter to dispatch the request "+n,"ERR_NOT_SUPPORT")}return o},adapters:ft};function gt(t){if(t.cancelToken&&t.cancelToken.throwIfRequested(),t.signal&&t.signal.aborted)throw new be(null,t)}function Ci(t){return gt(t),t.headers=B.from(t.headers),t.data=ut.call(t,t.transformRequest),["post","put","patch"].indexOf(t.method)!==-1&&t.headers.setContentType("application/x-www-form-urlencoded",!1),wi.getAdapter(t.adapter||Te.adapter)(t).then(function(o){return gt(t),o.data=ut.call(t,t.transformResponse,o),o.headers=B.from(o.headers),o},function(o){return di(o)||(gt(t),o&&o.response&&(o.response.data=ut.call(t,t.transformResponse,o.response),o.response.headers=B.from(o.response.headers))),Promise.reject(o)})}const $i="1.7.7",bt={};["object","boolean","number","function","string","symbol"].forEach((t,e)=>{bt[t]=function(o){return typeof o===t||"a"+(e<1?"n ":" ")+t}});const Si={};bt.transitional=function(e,i,o){function s(r,n){return"[Axios v"+$i+"] Transitional option '"+r+"'"+n+(o?". "+o:"")}return(r,n,a)=>{if(e===!1)throw new y(s(n," has been removed"+(i?" in "+i:"")),y.ERR_DEPRECATED);return i&&!Si[n]&&(Si[n]=!0,console.warn(s(n," has been deprecated since v"+i+" and will be removed in the near future"))),e?e(r,n,a):!0}};function Ts(t,e,i){if(typeof t!="object")throw new y("options must be an object",y.ERR_BAD_OPTION_VALUE);const o=Object.keys(t);let s=o.length;for(;s-- >0;){const r=o[s],n=e[r];if(n){const a=t[r],p=a===void 0||n(a,r,t);if(p!==!0)throw new y("option "+r+" must be "+p,y.ERR_BAD_OPTION_VALUE);continue}if(i!==!0)throw new y("Unknown option "+r,y.ERR_BAD_OPTION)}}const yt={assertOptions:Ts,validators:bt},te=yt.validators;class pe{constructor(e){this.defaults=e,this.interceptors={request:new ni,response:new ni}}async request(e,i){try{return await this._request(e,i)}catch(o){if(o instanceof Error){let s;Error.captureStackTrace?Error.captureStackTrace(s={}):s=new Error;const r=s.stack?s.stack.replace(/^.+\n/,""):"";try{o.stack?r&&!String(o.stack).endsWith(r.replace(/^.+\n.+\n/,""))&&(o.stack+=`
`+r):o.stack=r}catch{}}throw o}}_request(e,i){typeof e=="string"?(i=i||{},i.url=e):i=e||{},i=ce(this.defaults,i);const{transitional:o,paramsSerializer:s,headers:r}=i;o!==void 0&&yt.assertOptions(o,{silentJSONParsing:te.transitional(te.boolean),forcedJSONParsing:te.transitional(te.boolean),clarifyTimeoutError:te.transitional(te.boolean)},!1),s!=null&&(d.isFunction(s)?i.paramsSerializer={serialize:s}:yt.assertOptions(s,{encode:te.function,serialize:te.function},!0)),i.method=(i.method||this.defaults.method||"get").toLowerCase();let n=r&&d.merge(r.common,r[i.method]);r&&d.forEach(["delete","get","head","post","put","patch","common"],f=>{delete r[f]}),i.headers=B.concat(n,r);const a=[];let p=!0;this.interceptors.request.forEach(function(x){typeof x.runWhen=="function"&&x.runWhen(i)===!1||(p=p&&x.synchronous,a.unshift(x.fulfilled,x.rejected))});const c=[];this.interceptors.response.forEach(function(x){c.push(x.fulfilled,x.rejected)});let l,h=0,v;if(!p){const f=[Ci.bind(this),void 0];for(f.unshift.apply(f,a),f.push.apply(f,c),v=f.length,l=Promise.resolve(i);h<v;)l=l.then(f[h++],f[h++]);return l}v=a.length;let C=i;for(h=0;h<v;){const f=a[h++],x=a[h++];try{C=f(C)}catch(g){x.call(this,g);break}}try{l=Ci.call(this,C)}catch(f){return Promise.reject(f)}for(h=0,v=c.length;h<v;)l=l.then(c[h++],c[h++]);return l}getUri(e){e=ce(this.defaults,e);const i=ui(e.baseURL,e.url);return si(i,e.params,e.paramsSerializer)}}d.forEach(["delete","get","head","options"],function(e){pe.prototype[e]=function(i,o){return this.request(ce(o||{},{method:e,url:i,data:(o||{}).data}))}}),d.forEach(["post","put","patch"],function(e){function i(o){return function(r,n,a){return this.request(ce(a||{},{method:e,headers:o?{"Content-Type":"multipart/form-data"}:{},url:r,data:n}))}}pe.prototype[e]=i(),pe.prototype[e+"Form"]=i(!0)});class xt{constructor(e){if(typeof e!="function")throw new TypeError("executor must be a function.");let i;this.promise=new Promise(function(r){i=r});const o=this;this.promise.then(s=>{if(!o._listeners)return;let r=o._listeners.length;for(;r-- >0;)o._listeners[r](s);o._listeners=null}),this.promise.then=s=>{let r;const n=new Promise(a=>{o.subscribe(a),r=a}).then(s);return n.cancel=function(){o.unsubscribe(r)},n},e(function(r,n,a){o.reason||(o.reason=new be(r,n,a),i(o.reason))})}throwIfRequested(){if(this.reason)throw this.reason}subscribe(e){if(this.reason){e(this.reason);return}this._listeners?this._listeners.push(e):this._listeners=[e]}unsubscribe(e){if(!this._listeners)return;const i=this._listeners.indexOf(e);i!==-1&&this._listeners.splice(i,1)}toAbortSignal(){const e=new AbortController,i=o=>{e.abort(o)};return this.subscribe(i),e.signal.unsubscribe=()=>this.unsubscribe(i),e.signal}static source(){let e;return{token:new xt(function(s){e=s}),cancel:e}}}function Os(t){return function(i){return t.apply(null,i)}}function Rs(t){return d.isObject(t)&&t.isAxiosError===!0}const vt={Continue:100,SwitchingProtocols:101,Processing:102,EarlyHints:103,Ok:200,Created:201,Accepted:202,NonAuthoritativeInformation:203,NoContent:204,ResetContent:205,PartialContent:206,MultiStatus:207,AlreadyReported:208,ImUsed:226,MultipleChoices:300,MovedPermanently:301,Found:302,SeeOther:303,NotModified:304,UseProxy:305,Unused:306,TemporaryRedirect:307,PermanentRedirect:308,BadRequest:400,Unauthorized:401,PaymentRequired:402,Forbidden:403,NotFound:404,MethodNotAllowed:405,NotAcceptable:406,ProxyAuthenticationRequired:407,RequestTimeout:408,Conflict:409,Gone:410,LengthRequired:411,PreconditionFailed:412,PayloadTooLarge:413,UriTooLong:414,UnsupportedMediaType:415,RangeNotSatisfiable:416,ExpectationFailed:417,ImATeapot:418,MisdirectedRequest:421,UnprocessableEntity:422,Locked:423,FailedDependency:424,TooEarly:425,UpgradeRequired:426,PreconditionRequired:428,TooManyRequests:429,RequestHeaderFieldsTooLarge:431,UnavailableForLegalReasons:451,InternalServerError:500,NotImplemented:501,BadGateway:502,ServiceUnavailable:503,GatewayTimeout:504,HttpVersionNotSupported:505,VariantAlsoNegotiates:506,InsufficientStorage:507,LoopDetected:508,NotExtended:510,NetworkAuthenticationRequired:511};Object.entries(vt).forEach(([t,e])=>{vt[e]=t});function Pi(t){const e=new pe(t),i=jt(pe.prototype.request,e);return d.extend(i,pe.prototype,e,{allOwnKeys:!0}),d.extend(i,e,null,{allOwnKeys:!0}),i.create=function(s){return Pi(ce(t,s))},i}const E=Pi(Te);E.Axios=pe,E.CanceledError=be,E.CancelToken=xt,E.isCancel=di,E.VERSION=$i,E.toFormData=je,E.AxiosError=y,E.Cancel=E.CanceledError,E.all=function(e){return Promise.all(e)},E.spread=Os,E.isAxiosError=Rs,E.mergeConfig=ce,E.AxiosHeaders=B,E.formToJSON=t=>ai(d.isHTMLForm(t)?new FormData(t):t),E.getAdapter=wi.getAdapter,E.HttpStatusCode=vt,E.default=E;const L=(t,e,i,o,s)=>{E.post(`${t}`,i,{headers:{Accept:"*/*","Content-Type":"application/json-patch+json",Authorization:`Bearer ${e}`}}).then(r=>{o(r.data)}).catch(r=>{s("Erro na solicitação:",r)})},ye=(t,e,i,o)=>{E.get(`${t}`,{headers:{Accept:"*/*","Content-Type":"application/json-patch+json",Authorization:`Bearer ${e}`}}).then(s=>{i(s.data)}).catch(s=>{o("Erro na solicitação:",s)})};function wt(t){const e=new Date(t),i=String(e.getDate()).padStart(2,"0"),o=String(e.getMonth()+1).padStart(2,"0"),s=e.getFullYear();return`${i}/${o}/${s}`}function z(t){return new Intl.NumberFormat("pt-BR",{style:"currency",currency:"BRL"}).format(t)}var Is=Object.defineProperty,_s=Object.getOwnPropertyDescriptor,H=(t,e,i,o)=>{for(var s=o>1?void 0:o?_s(e,i):e,r=t.length-1,n;r>=0;r--)(n=t[r])&&(s=(o?n(e,i,s):n(s))||s);return o&&s&&Is(e,i,s),s};let V=class extends R{constructor(){super(...arguments),this.memberId=0,this.cancelRequest=!1,this.requestId=0,this.confirmCancel=!1,this.messageCallback=!1,this.isLoading=!1,this.intervalId=0,this.token="",this.servicesUrl="",this.headerTableDetailPayment=[{label:"Veículo",id:"VehicleId"},{label:"Descrição",id:"FeeName"},{label:"Valor",id:"FeeAmount"}]}static get styles(){return[lo]}checkPaymentStatus(t){ye(`${this.servicesUrl}/G2OnlineServices/CheckPaymentStatus?requestId=${t}`,this.token,e=>{this.IsPaid=e.IsPaid,this.IsPaid&&(this.clearTime(),this.dispatchEvent(new CustomEvent("paid",{composed:!0,bubbles:!0}))),this.requestUpdate()},()=>{})}CancelPayment(){this.isLoading=!0,L(`${this.servicesUrl}/G2OnlineServices/CancelPayment`,this.token,{memberId:this.memberId,requestID:this.requestId},()=>{this.messageCallback=!0,this.dispatchEvent(new CustomEvent("message-callback",{composed:!0,bubbles:!0,detail:this.messageCallback})),this.isLoading=!1,this.clearTime()},t=>{console.log(t)})}checkoutCompleteSvg(){return _e`
    <svg width="100" height="100" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path fill-rule="evenodd" clip-rule="evenodd" d="M10 20C4.47667 20 0 15.5233 0 10C0 4.47667 4.47667 0 10 0C15.5233 0 20 4.47667 20 10C20 15.5233 15.5233 20 10 20Z" fill="#12B76A"/>
      <path d="M13.6108 8.33337L8.74967 13.1945L5.83301 10.2778" stroke="#F6FEF9" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
    `}checkoutCanceledSvg(){return _e`
    <svg width="120" height="120" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M12 2C6.486 2 2 6.486 2 12C2 17.514 6.486 22 12 22C17.514 22 22 17.514 22 12C22 6.486 17.514 2 12 2ZM16.207 14.793L14.793 16.207L12 13.414L9.207 16.207L7.793 14.793L10.586 12L7.793 9.207L9.207 7.793L12 10.586L14.793 7.793L16.207 9.207L13.414 12L16.207 14.793Z" fill="#F04438"/>
    </svg>

    `}copyPaste(t){navigator.clipboard.writeText(t);const e=this.shadowRoot.getElementById("copiedMessage");e.style.display="block",setTimeout(()=>{e.style.display="none"},3e3)}updated(t){super.updated(t),t.has("dataQrCode")&&(this.requestId=this.dataQrCode.requestId,this.IsPaid||this.dataQrCode.PaymentStatusID==1&&(this.intervalId=setInterval(()=>this.checkPaymentStatus(this.dataQrCode.requestId),3e3)))}clearTime(){clearInterval(this.intervalId)}async connectedCallback(){super.connectedCallback(),await super.updateComplete}render(){return u`
      <div id="copiedMessage" class="copied-message">
        Texto copiado com sucesso!
      </div>
      ${this.isLoading?u`<div class="spinner"><loading-spinner></loading-spinner></div>`:this.messageCallback?u`<div class="">
              <message-callback></message-callback>
            </div>`:u` ${this.showCofirmModal()} `}
    `}alertOctagon(){return _e`
    <svg width="110" height="110" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M12 8V12M12 16H12.01M7.86 2H16.14L22 7.86V16.14L16.14 22H7.86L2 16.14V7.86L7.86 2Z" stroke="#e73300" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
    `}formatDataDetailPayment(){return this.dataQrCode.Items.map(e=>({VehicleId:e.VehicleId,FeeName:e.FeeName,FeeAmount:z(e==null?void 0:e.FeeAmount)}))}showCofirmModal(){var t,e,i,o,s,r;return this.dataQrCode?u`
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
                  <p>${wt((e=this.dataQrCode)==null?void 0:e.creationDate)}</p>
                </div>

                <div class="itemDetails">
                  <p>Data Vencimento PIX:</p>
                  <p>${wt((i=this.dataQrCode)==null?void 0:i.dueDate)}</p>
                </div>

                <div class="itemDetails">
                  <p>Valor Total:</p>
                  <p>${z((o=this.dataQrCode)==null?void 0:o.requestAmount)}</p>
                </div>
              

                <div class="childItems">
                  <p>Itens:</p>
                  <colibri-common-g2-table-default .theadData=${this.headerTableDetailPayment} .tbodyData=${this.formatDataDetailPayment()}></colibri-common-g2-table-default>                   
                </div>
              </div>
            </div>

          </div>
          ${window.innerWidth<880?u`
                  <div class="pix">
                    ${this.dataQrCode.PaymentStatusID!=1||this.IsPaid||this.confirmCancel?null:u` <colibri-common-g2-button
                          @onClick=${()=>{var n;return this.copyPaste((n=this.dataQrCode)==null?void 0:n.copyPaste)}}
                          class="button"
                        >
                          <ph-pix-logo size="20"></ph-pix-logo> Copiar Pix
                        </colibri-common-g2-button>`}
                  </div>
                `:null}
          
          ${this.confirmCancel?null:u`<div class="cancelButtonDiv">
                  ${this.renderCancelButton()}
                </div>`}
      </div>

          ${this.confirmCancel?u`
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
                `:window.innerWidth<880?this.renderBadgeMessage():u`<div class="qrCodeImage">
                    ${this.dataQrCode.PaymentStatusID==1?u`<p style="margin:0;">Escaneie o QR Code</p>`:null}

                    <div class="imgPix">
                      <img src=${(s=this.dataQrCode)==null?void 0:s.qrcode} />
                      ${this.IsPaid||((r=this.dataQrCode)==null?void 0:r.PaymentStatusID)==2?u`<div class="svgCheck">
                            ${this.checkoutCompleteSvg()}
                          </div>`:null}
                      ${this.statusPayment()}
                    </div>
                    <div class="pix">
                      ${this.dataQrCode.PaymentStatusID!=1||this.IsPaid||this.confirmCancel?null:u`<colibri-common-g2-button
                            @onClick=${()=>{var n;return this.copyPaste((n=this.dataQrCode)==null?void 0:n.copyPaste)}}
                            class="button"
                          >
                            <ph-pix-logo size="20"></ph-pix-logo> Copiar Pix
                          </colibri-common-g2-button>`}
                    </div>
                  </div>`}
        </div>
        ${this.confirmCancel?u`
                <div class="badgeContent">
                  <ph-warning
                    color="var(--warning-600)"
                    weight="bold"
                    size="22"
                  ></ph-warning>

                  <p>
                    Envio de documento e autenticação de termo, relacionados a este pagamento, serão cancelados
                  </p>
                </div>
              `:null}
        </div>
          `:u`
        <div class="skeletons skeletonChildWidth">
          <div class="skeleton skeletonSize"></div>
          <div class="skeleton skeletonSize"></div>
        </div>
      `}shouldShowCancelButton(){var t;return!this.IsPaid&&this.cancelRequest&&((t=this.dataQrCode)==null?void 0:t.PaymentStatusID)===1}toggleConfirmCancel(){this.confirmCancel=!this.confirmCancel}renderCancelButton(){return this.shouldShowCancelButton()?u`
        <colibri-common-g2-button
          variant="error"
          class="button"
          @click=${this.toggleConfirmCancel}
        >
          Cancelar
        </colibri-common-g2-button>
      `:null}renderBadgeMessage(){var t,e,i;if(((t=this.dataQrCode)==null?void 0:t.PaymentStatusID)==2)return u`<colibri-common-g2-badge
        type="success"
        text="Pagamento Concluído"
      ></colibri-common-g2-badge>`;if(((e=this.dataQrCode)==null?void 0:e.PaymentStatusID)==3)return u`<colibri-common-g2-badge
        type="yellow"
        text="Pagamento Cancelado"
      ></colibri-common-g2-badge>`;if(((i=this.dataQrCode)==null?void 0:i.PaymentStatusID)==4)return u`<colibri-common-g2-badge
        type="yellow"
        text="Pagamento Expirado"
      ></colibri-common-g2-badge>`}statusPayment(){var t,e;if(((t=this.dataQrCode)==null?void 0:t.PaymentStatusID)==3||((e=this.dataQrCode)==null?void 0:e.PaymentStatusID)==4)return u`<div class="svgCanceled">${this.checkoutCanceledSvg()}</div>`}handleOnModalCard(){const t=new CustomEvent("my-close-modal");this.dispatchEvent(t)}};H([b()],V.prototype,"dataQrCode",2),H([b()],V.prototype,"memberId",2),H([b()],V.prototype,"cancelRequest",2),H([m()],V.prototype,"requestId",2),H([m()],V.prototype,"confirmCancel",2),H([m()],V.prototype,"messageCallback",2),H([m()],V.prototype,"paidCallback",2),H([m()],V.prototype,"isLoading",2),H([m()],V.prototype,"intervalId",2),H([b({type:String})],V.prototype,"token",2),H([b()],V.prototype,"servicesUrl",2),V=H([M("qrcode-visualizer")],V);const Fs=N`
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
`;var Ls=Object.defineProperty,Ns=Object.getOwnPropertyDescriptor,xe=(t,e,i,o)=>{for(var s=o>1?void 0:o?Ns(e,i):e,r=t.length-1,n;r>=0;r--)(n=t[r])&&(s=(o?n(e,i,s):n(s))||s);return o&&s&&Ls(e,i,s),s};let ie=class extends R{constructor(){super(...arguments),this.zipCode="",this.dataAddress=null,this.servicesUrl="https://g2services-qa4.copart.com.br/",this.token=""}async connectedCallback(){super.connectedCallback(),await super.updateComplete}fetchData(){L(`${this.servicesUrl}/G2Member/SearchZipCode`,this.token,{zipCode:this.zipCode},e=>{this.zipCodeDetails=e.zipCodeDetails,this.requestUpdate()},()=>{})}handleSaveChanges(){const e=this.shadowRoot.querySelectorAll(".inputClass");let i=!0;e.forEach(o=>{const s=this.shadowRoot.getElementById(`${o.id}Error`);o.value.trim()?o.id==="cep"&&!this.isValidCEP(o.value.trim())?(i=!1,o.classList.add("error"),s.textContent="CEP inválido."):(o.classList.remove("error"),s.textContent=""):(i=!1,o.classList.add("error"),s.textContent="Este campo é obrigatório.")}),i?this.saveData():console.log("Por favor, corrija os erros antes de salvar.")}saveData(){console.log("Dados salvos com sucesso!")}handleCloseModal(){this.dispatchEvent(new CustomEvent("colibri-handle-show-shipping-address",{composed:!0,bubbles:!0,detail:{}}))}render(){var e,i,o,s,r,n,a;return u`
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
              value=${(n=this.dataAddress)==null?void 0:n.City}
              id="city"
              class="inputClass"
              type="text"
            />
            <span id="cityError" class="error-message"></span>
          </div>
          <div class="input">
            <label for="">Estado</label>
            <input
              value=${(a=this.dataAddress)==null?void 0:a.State}
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
    `}isValidCEP(e){return/^\d{5}-\d{3}$/.test(e)}handleInput(e){const i=e.target,o=i.value.replace(/\D/g,""),s=this.formatCEP(o);this.zipCode=i.value,i.value=s}formatCEP(e){const i=/^(\d{0,5})(\d{0,3})$/,o=e.match(i);return o?`${o[1]}${o[2]?"-"+o[2]:""}`:e}};ie.styles=[Fs],xe([m()],ie.prototype,"zipCode",2),xe([m()],ie.prototype,"zipCodeDetails",2),xe([b()],ie.prototype,"dataAddress",2),xe([b()],ie.prototype,"servicesUrl",2),xe([b({type:String})],ie.prototype,"token",2),ie=xe([M("shipping-address")],ie);const Ms=N`
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
`,zs=N`
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
`,Us=N`
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
`;var Bs=Object.defineProperty,js=Object.getOwnPropertyDescriptor,ki=(t,e,i,o)=>{for(var s=o>1?void 0:o?js(e,i):e,r=t.length-1,n;r>=0;r--)(n=t[r])&&(s=(o?n(e,i,s):n(s))||s);return o&&s&&Bs(e,i,s),s};let Ct=class extends R{constructor(){super(...arguments),this.isLabel=""}static get styles(){return[zs,Us,Ms]}shimmerTable(){return u`
      <div class="row">
        <div class="column">
          <div class="skeleton">
            <div class="row-skeleton white"></div>
          </div>
        </div>
      </div>
    `}skeleton(){return u` <div>
      ${this.isLabel&&u`<label for=${this.isLabel}>${this.isLabel}</label>`}

      <div class="skeleton-container">${this.shimmerTable()}</div>
    </div>`}render(){return u` ${this.skeleton()} `}};ki([b({type:String})],Ct.prototype,"isLabel",2),Ct=ki([M("ui-load-input")],Ct);var qs=Object.defineProperty,Vs=Object.getOwnPropertyDescriptor,Hs=(t,e,i,o)=>{for(var s=o>1?void 0:o?Vs(e,i):e,r=t.length-1,n;r>=0;r--)(n=t[r])&&(s=(o?n(e,i,s):n(s))||s);return o&&s&&qs(e,i,s),s};let $t=class extends R{render(){return u`
      <div class="spinner"></div>
    `}};$t.styles=N`
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
  `,$t=Hs([M("loading-spinner")],$t);const Gs=N`
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
`;var Qs=Object.defineProperty,Ws=Object.getOwnPropertyDescriptor,oe=(t,e,i,o)=>{for(var s=o>1?void 0:o?Ws(e,i):e,r=t.length-1,n;r>=0;r--)(n=t[r])&&(s=(o?n(e,i,s):n(s))||s);return o&&s&&Qs(e,i,s),s};let Q=class extends R{constructor(){super(...arguments),this.isLoadTable=!1,this.shippingType=0,this.servicesUrl="",this.memberId=0,this.token="",this.theadData=[{label:"Código",id:"VehicleId"},{label:"Leilão",id:"SaleInfo"},{label:"Lote",id:"ProcessId"},{label:"Status",id:"Status"}]}async connectedCallback(){super.connectedCallback(),await super.updateComplete,this.fetchData()}fetchData(){ye(`${this.servicesUrl}/G2OnlineServices/GetMemberAddress?id=${this.memberId}`,this.token,e=>{this.addressData=e.Address,this.requestUpdate()},()=>{})}handleHideShippingAddress(){this.shippingType=0,this.requestUpdate()}changeStep(e){e==0?(this.shippingType=0,this.requestUpdate()):e==1?(this.shippingType=1,this.requestUpdate()):e==2?(this.shippingType=2,this.requestUpdate()):e==3?(this.shippingType=3,this.requestUpdate()):e==4&&(this.shippingType=4,this.requestUpdate())}renderStep0(){var e,i,o,s,r,n;return u`<div class="content">
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
          <p>${(r=this.addressData)==null?void 0:r.City} - ${(n=this.addressData)==null?void 0:n.State}</p>
        </div>
        <button @click=${()=>this.changeStep(2)} class="button minHeight">
          ALTERAR ENDEREÇO
        </button>
      </div>
    </div>`}renderStep1(){var e,i,o,s,r,n;return u`${u`<div class="content displayRow">
      <div class="modal-tbody">
        <div class="tr">
          ${this.theadData.map(a=>u` <div class="thead-td">${a.label}</div> `)}
        </div>

        ${this.isLoadTable?u`
              <div class="Skeletons-tbody">
                <div class="skeleton skeletonItem"></div>
                <div class="skeleton2 skeletonItem"></div>
                <div class="skeleton skeletonItem"></div>
                <div class="skeleton2 skeletonItem"></div>
              </div>
            `:(e=this.dataList)==null?void 0:e.map((a,p)=>u`
                <div
                  class=${p%2===0?"tr firstLine":"tr secondLine"}
                >
                  ${this.theadData.map(c=>u` <div class="td">${a[c.id]}</div> `)}
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
          <p>CEP: ${(n=this.addressData)==null?void 0:n.ZipCode}</p>
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
    </div>`}`}renderStep2(){return u`<shipping-address
      @colibri-handle-show-shipping-address=${this.handleHideShippingAddress}
      .dataAddress=${this.addressData}
    ></shipping-address>`}renderStep3(){return u`<p>OPa</p>`}renderStep4(){return u` <shipping-address
      @colibri-handle-show-shipping-address=${this.handleHideShippingAddress}
    ></shipping-address>`}steps(){switch(this.shippingType){case 1:return this.renderStep1();case 2:return this.renderStep2();case 3:return this.renderStep3();case 4:return this.renderStep4();default:return this.renderStep0()}}render(){return this.steps()}};Q.styles=[Gs],oe([m()],Q.prototype,"isLoadTable",2),oe([m()],Q.prototype,"shippingType",2),oe([m()],Q.prototype,"addressData",2),oe([b()],Q.prototype,"dataList",2),oe([b()],Q.prototype,"servicesUrl",2),oe([b()],Q.prototype,"memberId",2),oe([b({type:String})],Q.prototype,"token",2),Q=oe([M("document-shipping")],Q);const Zs=N`
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
`,Ys=(t,e,i)=>{let o="";return e===!1?!0:t[e]&&i.length===0?(o=t[e].errorNull,{[e]:o}):t[e]&&!t[e].regex.test(i)?(o=t[e].message,{[e]:o}):(o=null,{[e]:o})};function Qe(t,e){const s=Object.entries(e).map(n=>Ys(t,n[0],n[1])).reduce((n,a)=>{const p=Object.keys(a)[0],c=a[p];return c!==null&&(n[p]=c),n},{});return Object.keys(t).filter(n=>!e[n]).forEach(n=>{s[n]||(s[n]=t[n].errorNull)}),s}const St={AddressNumber:{regex:/^\d+$/,message:"Valor inválido",errorNull:"Preencha o campo Número"},ZipCode:{regex:/^\d{8}$/,message:"CEP inválido",errorNull:"Preencha o campo CEP"}},Js={Yard:{regex:/^\d+$/,message:"Valor inválido",errorNull:"Selecione uma opção"}};var Ks=Object.defineProperty,Xs=Object.getOwnPropertyDescriptor,A=(t,e,i,o)=>{for(var s=o>1?void 0:o?Xs(e,i):e,r=t.length-1,n;r>=0;r--)(n=t[r])&&(s=(o?n(e,i,s):n(s))||s);return o&&s&&Ks(e,i,s),s};let P=class extends R{constructor(){super(...arguments),this.isLoadTable=!1,this.shippingType=0,this.activeStep="Meu Endereço",this.isEditActualForm=!1,this.yardSelected={Yard:""},this.showPixModal=!1,this.actualForm={AddressName:"",AddressNumber:"",ZipCode:"",Neighborhood:"",City:"",State:"",Complement:"",CityId:""},this.thirdForm={AddressName:"",AddressNumber:"",ZipCode:"",Neighborhood:"",City:"",State:"",Complement:"",CityId:""},this.errorsActualForm={AddressNumber:"",ZipCode:""},this.errorYardSelect={Yard:""},this.errorsThirdForm={AddressNumber:"",ZipCode:""},this.servicesUrl="",this.memberId=0,this.token="",this.theadData=[{label:"Código",id:"VehicleId"},{label:"Marca",id:"Make"},{label:"Modelo",id:"Model"},{label:"Tipo de Venda",id:"SaleType"},{label:"Status",id:"Status"}]}async connectedCallback(){super.connectedCallback(),await super.updateComplete,this.fetchData()}fetchData(){ye(`${this.servicesUrl}/G2OnlineServices/GetShippingOptions?id=${this.memberId}&qt=${this.dataList.length}`,this.token,e=>{this.actualForm=e.MemberAddress,this.addressData=e,this.yardsChildren=e.Yards.map(i=>({id:String(i.Amount),value:String(i.YardId),name:i.YardName})),this.yardsChildren.unshift({id:"0",value:"0",name:"Selecione uma opção"}),this.feeCost=e.MemberAddress.Amount,this.requestUpdate()},()=>{})}save(){this.errorsActualForm=Qe(St,this.actualForm),!Object.entries(this.errorsActualForm).length&&L(`${this.servicesUrl}/G2OnlineServices/ChangeMemberAddress`,this.token,{memberId:this.memberId,addressName:this.actualForm.AddressName,number:this.actualForm.AddressNumber,zipCode:this.actualForm.ZipCode,neighborhood:this.actualForm.Neighborhood,cityId:this.actualForm.CityId,complement:this.actualForm.Complement},()=>{this.GetFeeCostByStateOrYard(this.actualForm.State),this.requestUpdate()},()=>{})}handleStepChange(e){this.activeStep=e,this.isEditActualForm=!1,this.activeStep=="Meu Endereço"?this.feeCost=this.addressData.MemberAddress.Amount:this.feeCost=0}wichFormProp(e){return this.activeStep=="Meu Endereço"?this.actualForm[e]:this.thirdForm[e]}titleModalChange(e){let i;return e.PaymentStatusID==2?i="Pagamento Realizado":e.PaymentStatusID==3?i="Pagamento Cancelado":(i="Aguardando Pagamento",this.messageCallback&&(i="Aviso")),i}updated(e){super.updated(e),e.has("messageModal")&&this.titleModalChange(this.dataQrCode)}requestDispatchDocuments(){this.errorsActualForm=Qe(St,this.actualForm),this.errorsThirdForm=Qe(St,this.thirdForm),this.errorYardSelect=Qe(Js,this.yardSelected);const e=this.dataList.map(s=>s.ProcessId);let i;if(this.activeStep=="Meu Endereço"?i=this.errorsActualForm:this.activeStep=="Outro Endereço"?i=this.errorsThirdForm:i=this.errorYardSelect,Object.entries(i).length)return;this.showPixModal=!this.showPixModal;const o={memberId:this.memberId,requestsIds:e,requestType:this.activeStep=="Pátio Copart"?2:this.activeStep=="Meu Endereço"?1:3,yardIdSelect:Number(this.yardSelected.Yard),address:this.wichFormProp("AddressName"),addressNumber:this.wichFormProp("AddressNumber"),neighborhood:this.wichFormProp("Neighborhood"),complement:this.wichFormProp("Complement"),zipCode:this.wichFormProp("ZipCode"),cityId:Number(this.wichFormProp("CityId"))};L(`${this.servicesUrl}/G2OnlineServices/RequestDispatchDocuments`,this.token,o,s=>{this.dataQrCode={...s.invoice,Items:s.Items},this.dispatchEvent(new CustomEvent("data-QrCode",{composed:!0,detail:this.titleModalChange(this.dataQrCode)})),this.requestUpdate()},()=>{})}GetFeeCostByStateOrYard(e){L(`${this.servicesUrl}/G2OnlineServices/GetFeeCostByStateOrYard`,this.token,{memberId:this.memberId,documentsQuantity:this.dataList.length,address:{state:e}},i=>{this.feeCost=i.FeeCost,this.requestUpdate()},()=>{})}dataListFormatted(){return this.dataList.map(e=>({...e,SaleType:`${e.SaleType}: ${e.SaleInfo}`}))}clearInterval(){this.qrcodeVisualizer.clearTime()}render(){var i;const e=[{name:"Meu Endereço",item:u`<actual-form
          @zipcode-searched-sucessfully=${o=>{this.actualForm=o.detail}}
          @on-Change=${o=>this.onChangeActualForm(o.detail.name,o.detail.value)}
          @is-edit=${o=>this.isEditActualForm=!o.detail}
          .data=${this.actualForm}
          .errors=${this.errorsActualForm}
          @save-new-address=${this.save}
          .servicesUrl=${this.servicesUrl}
        ></actual-form>`},{name:"Pátio Copart",item:u`<div class="contentSelect">
          <colibri-common-g2-select
            isLabel="Pátios"
            isPlaceholder="Selecione uma opção"
            .isChildren=${this.yardsChildren}
            @on-input=${o=>this.onChangeYardSelect(o)}
            .error=${this.errorYardSelect.Yard}
          ></colibri-common-g2-select>
        </div>`},{name:"Outro Endereço",item:u`<third-form
          @zipcode-searched-sucessfully=${o=>{this.thirdForm=o.detail,this.GetFeeCostByStateOrYard(o.detail.State)}}
          @on-Change=${o=>this.onChangeThirdForm(o.detail.name,o.detail.value)}
          .errors=${this.errorsThirdForm}
          .data=${this.thirdForm}
          .servicesUrl=${this.servicesUrl}
        ></third-form>`}];return u`
      ${this.showPixModal?u`<qrcode-visualizer
            id="qrcodeVisualizer"
            .dataQrCode=${this.dataQrCode}
            .requestId=${(i=this.dataQrCode)==null?void 0:i.requestId}
            .cancelRequest=${!0}
            .memberId=${this.memberId}
            .servicesUrl=${this.servicesUrl}
            .token=${this.token}
            @message-callback=${o=>this.messageCallback=o.detail}
          ></qrcode-visualizer>`:u` <div class="container">
          ${window.innerWidth<880?null:u`<div class="sectionStep">
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

                  ${window.innerWidth<880?null:u`<div class="observation">
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
                      <span>${z(this.feeCost)}</span>
                    </h2>

                    <colibri-common-g2-button .isDisabled=${this.isEditActualForm||this.activeStep=="Outro Endereço"&&this.thirdForm.Neighborhood==""} @onClick=${this.requestDispatchDocuments}>
                      Confirmar
                    </colibri-common-g2-button>
                  </div>
                </section>
              </div>
              </div>
              `}
    `}onChangeActualForm(e,i){this.actualForm={...this.actualForm,[e]:i}}onChangeThirdForm(e,i){this.thirdForm={...this.thirdForm,[e]:i}}onChangeYardSelect(e){this.feeCost=e.detail.id,this.yardSelected.Yard=e.detail.value}};P.styles=[Zs],A([Le("#qrcodeVisualizer")],P.prototype,"qrcodeVisualizer",2),A([m()],P.prototype,"isLoadTable",2),A([m()],P.prototype,"shippingType",2),A([m()],P.prototype,"activeStep",2),A([m()],P.prototype,"addressData",2),A([m()],P.prototype,"feeCost",2),A([m()],P.prototype,"yardsChildren",2),A([m()],P.prototype,"isEditActualForm",2),A([m()],P.prototype,"yardSelected",2),A([m()],P.prototype,"showPixModal",2),A([m()],P.prototype,"dataQrCode",2),A([m()],P.prototype,"messageCallback",2),A([m()],P.prototype,"actualForm",2),A([m()],P.prototype,"thirdForm",2),A([m()],P.prototype,"errorsActualForm",2),A([m()],P.prototype,"errorYardSelect",2),A([m()],P.prototype,"errorsThirdForm",2),A([b()],P.prototype,"dataList",2),A([b()],P.prototype,"servicesUrl",2),A([b()],P.prototype,"memberId",2),A([b({type:String})],P.prototype,"token",2),P=A([M("documents-send")],P);const en=N`
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
`;var tn=Object.defineProperty,on=Object.getOwnPropertyDescriptor,$=(t,e,i,o)=>{for(var s=o>1?void 0:o?on(e,i):e,r=t.length-1,n;r>=0;r--)(n=t[r])&&(s=(o?n(e,i,s):n(s))||s);return o&&s&&tn(e,i,s),s};let w=class extends R{constructor(){super(...arguments),this.showModal=!1,this.showModalFilters=!1,this.completionPayment=!1,this.isLoadTable=!0,this.dataListNotFormatted=[],this.dataList=[],this.showHead=!1,this.IsPaid=!0,this.showHeadMap=new Map,this.requestId=0,this.FeeIds=[],this.subTotal=0,this.selectedOptions=[],this.memberId=1024863,this.pagination={memberId:this.memberId,baseQuery:"",pageSize:20,pageNumber:1,sortField:"",sortOrder:"",totalPages:0,NumFound:0},this.vehicleId=0,this.saleType=0,this.sortBy="",this.sortAsc=!0,this.token="",this.servicesUrl="",this.selectedRows=[],this.theadDataChildTable=[{id:"-",label:"-"},{id:"FeeName",label:"Descrição cobrança"},{id:"state",label:"Situação"},{id:"DueDate",label:"Data Vencimento"},{id:"FeeAmount",label:"Valor"}]}calcularSomaTotalFeeAmount(t){let e=0;return t.forEach(i=>{e+=i.TotalFeeAmount}),z(e)}fetchData(){this.isLoadTable=!0,this.showModalFilters&&(this.showModalFilters=!1),L(`${this.servicesUrl}/G2OnlineServices/GetPendingPayments`,this.token,{memberId:this.memberId,pageSize:this.pagination.pageSize,pageNumber:this.pagination.pageNumber,vehicleId:this.vehicleId==0?0:this.vehicleId,saleType:this.saleType,sortBy:this.sortBy,sortOrder:this.sortAsc},t=>{this.isLoadTable=!1,this.pagination=this.pagination={...this.pagination,NumFound:t.pagination.NumFound,pageSize:t.pagination.pageSize,pageNumber:t.pagination.pageNumber,totalPages:t.pagination.totalPages},this.dataListNotFormatted=t.items,this.totalFeeAmount=this.calcularSomaTotalFeeAmount(t.items),this.dataList=t.items.map(e=>({...e,SaleDate:wt(e.SaleDate),OthersFeeAmount:z(e.OthersFeeAmount),TotalFeeAmount:z(e.TotalFeeAmount),DSALFeeAmount:z(e.DSALFeeAmount),BidAmount:z(e.BidAmount),ComissionFeeAmount:z(e.ComissionFeeAmount),VehicleSaleAmount:z(e.VehicleSaleAmount),InvoiceLink:e.InvoiceLink?u`<a href=${e.InvoiceLink} style="text-decoration:none"
                >Visualizar Boleto</a
              >`:null,Info:`${e.SaleTypeDescription}: ${this.renderSaleInfo(e)}`}))},()=>{})}renderSaleInfo(t){return t.SaleType==1?`${t.AuctionNumber} / ${t.LotOrder}`:`${t.BuyItNowId}`}PrintPendingPaymentsToPdf(){L(`${this.servicesUrl}/G2OnlineServices/PrintPendingPaymentsToPdf`,this.token,{items:this.dataListNotFormatted},t=>{if(t.resultCode===0&&t.content){const e=atob(t.content),i=new Array(e.length);for(let h=0;h<e.length;h++)i[h]=e.charCodeAt(h);const o=new Uint8Array(i),s=new Blob([o],{type:"application/pdf"}),r=URL.createObjectURL(s),n=new Date,a=String(n.getDate()).padStart(2,"0"),p=String(n.getMonth()+1).padStart(2,"0"),c=n.getFullYear(),l=document.createElement("a");l.style.display="none",l.href=r,l.download=`pagamentosPendentes${a}/${p}/${c}.pdf`,document.body.appendChild(l),l.click(),URL.revokeObjectURL(r),document.body.removeChild(l)}},()=>{})}ExportPendingPaymentsToExcel(){L(`${this.servicesUrl}/G2OnlineServices/ExportPendingPaymentsToExcel`,this.token,{items:this.dataListNotFormatted},t=>{if(t.resultCode===0&&t.content){const e=atob(t.content),i=new Array(e.length);for(let h=0;h<e.length;h++)i[h]=e.charCodeAt(h);const o=new Uint8Array(i),s=new Blob([o],{type:"application/vnd.ms-excel"}),r=URL.createObjectURL(s),n=new Date,a=String(n.getDate()).padStart(2,"0"),p=String(n.getMonth()+1).padStart(2,"0"),c=n.getFullYear(),l=document.createElement("a");l.style.display="none",l.href=r,l.download=`pagamentosPendentes${a}/${p}/${c}.xls`,document.body.appendChild(l),l.click(),URL.revokeObjectURL(r),document.body.removeChild(l)}},()=>{})}handleCompletionPayment(){this.completionPayment=!this.completionPayment}generateQrCode(){const t=[];this.selectedRows.forEach(e=>{e.selectedFees.forEach(i=>{t.push(...i.FeeId)})}),L(`${this.servicesUrl}/G2OnlineServices/RequestInvoice`,this.token,{feesIds:t,memberId:this.memberId},e=>{this.dataQrCode={...e.invoice,Items:e.Items},this.requestId=e.invoice.requestId,this.pagination.pageNumber=1,this.fetchData(),this.selectedRows=[],this.subTotal=0},()=>{})}handleOpenModal(){this.showModal=!this.showModal,this.showModal==!1&&this.pix.clearTime(),this.completionPayment=!1}handleOpenModalFilters(){this.showModalFilters=!this.showModalFilters}tHeadFormatted(){return window.innerWidth<880?[{label:"Código",id:"VehicleId",isSort:!0},{label:"Data da Venda",id:"SaleDate",isSort:!0},{label:"Descrição",id:"VehicleDescription"},{label:"Lance/Bem",id:"BidAmount"},{label:"Comissão",id:"ComissionFeeAmount"},{label:"DSAL/DSAP",id:"DSALFeeAmount"},{label:"Outros",id:"OthersFeeAmount"},{label:"Valor Devido",id:"TotalFeeAmount"},{label:"Tipo de Venda",id:"Info",isSort:!0},{label:"Boleto",id:"InvoiceLink"},{label:"",id:"Itens"}]:[{label:"Código",id:"VehicleId",isSort:!0},{label:"Data da Venda",id:"SaleDate",isSort:!0},{label:"Descrição",id:"VehicleDescription"},{label:"Lance/Bem",id:"BidAmount"},{label:"Comissão",id:"ComissionFeeAmount"},{label:"DSAL/DSAP",id:"DSALFeeAmount"},{label:"Outros",id:"OthersFeeAmount"},{label:"Valor Devido",id:"TotalFeeAmount"},{label:"Tipo de Venda",id:"Info",isSort:!0},{label:"Boleto",id:"InvoiceLink"},{label:"",id:"View"}]}formatDate(t){if(t==null)return"-";const e=new Date(t),i=String(e.getDate()).padStart(2,"0"),o=String(e.getMonth()+1).padStart(2,"0"),s=e.getFullYear();return`${i}/${o}/${s}`}theadDataModal(){return window.innerWidth<880?[{label:"Código",id:"VehicleId"},{label:"Tipo de Venda",id:"SaleTypeDescription"},{label:"Descrição",id:"VehicleDescription"},{label:"Valor",id:"TotalFeeAmount"},{label:"",id:"Detail"}]:[{label:"Código",id:"VehicleId"},{label:"Tipo de Venda",id:"SaleTypeDescription"},{label:"Descrição",id:"VehicleDescription"},{label:"Valor",id:"TotalFeeAmount"},{label:"",id:"View"}]}isChecked(t,e){return t.some(i=>e.FeeId.includes(i))}dataFeesList(t){var o;const e=[];return this.selectedRows.forEach(s=>{s.selectedFees.forEach(r=>{e.push(...r.FeeId)})}),(o=t==null?void 0:t.Fees)==null?void 0:o.map(s=>({"-":u`<input
        type="checkbox"
        value=${s.FeeAmount}
        @input=${r=>this.toggleCheckbox(r.target,t,s)}
        ?disabled=${!s.IsSelectable}
        .title=${s.IsSelectable?"":"Aguardando pagamento"}
        .checked=${this.isChecked(e,s)}
        class="checkbox"
      />`,FeeName:s.FeeName,state:u`<colibri-common-g2-badge
        .type=${s.IsSelectable?"blue":"warning"}
        .text=${s.IsSelectable?"Pendente":"Aguardando Pagamento"}
      ></colibri-common-g2-badge>`,DueDate:this.formatDate(s.DueDate),FeeAmount:z(s.FeeAmount)}))}async connectedCallback(){super.connectedCallback(),await super.updateComplete,this.fetchData(),this.GetMemberVehicleDocumentosFilters()}handleClick(t){this.dataList[t].Child==null?this.dataList[t]={...this.dataList[t],Child:this.childTable(this.dataList[t])}:this.dataList[t]={...this.dataList[t],Child:null},this.requestUpdate()}handleClickCheckout(t){this.selectedRows[t].Child==null?this.selectedRows[t]={...this.selectedRows[t],Child:this.tableSelectedFees(this.selectedRows[t].selectedFees)}:this.selectedRows[t]={...this.selectedRows[t],Child:null},this.requestUpdate()}async handleOnChangePagination(t,e){t==="pageSize"&&(this.pagination={...this.pagination,pageNumber:1}),this.pagination={...this.pagination,[t]:e},this.fetchData()}GetMemberVehicleDocumentosFilters(){ye(`${this.servicesUrl}/G2OnlineServices/GetMemberVehicleDocumentosFilters`,this.token,t=>{this.GetMemberVehicleDocumentosOptionsSaleType=t.SaleType.map(e=>({id:String(e.id),value:String(e.id),name:e.descricao})),this.GetMemberVehicleDocumentosOptionsSaleType.unshift({id:"0",value:"0",name:"Selecione uma opção"}),this.requestUpdate()},()=>{})}handleSortTable(t){const e=t.detail;this.sortAsc=e.sortAsc,this.sortBy=e.sortBy,this.fetchData()}filterModalResponsive(){return u`
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
    `}get formattedData(){return this.dataList.map((t,e)=>({...t,View:u` <style>
          .link {
            color: blue;
            cursor: pointer;
          }
        </style>
        <a
          class="link"
          @click=${()=>{window.innerWidth<880?console.log(""):this.handleClick(e)}}
          >Visualizar</a
        >`,Child:t.Child,Itens:u` <colibri-common-g2-table-default
        .theadData=${this.theadDataChildTable}
        .tbodyData=${this.dataFeesList(t)}
      ></colibri-common-g2-table-default>`}))}render(){var t,e,i,o,s,r;return u`
      <g2-dialog
        .isOpen=${this.showModal}
        title="Pagamentos"
        @on-close=${this.handleOpenModal}
      >
        <div class="content padding largeModalResponsive">
          ${this.completionPayment?u`<qrcode-visualizer
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
            ${this.completionPayment?null:u`<button
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
                @on-input=${n=>this.vehicleId=n.detail.value}
              ></colibri-common-g2-input>

              <colibri-common-g2-select
                class="input"
                isLabel="Tipo de venda"
                .isChildren=${this.GetMemberVehicleDocumentosOptionsSaleType}
                @on-input=${n=>this.saleType=n.detail.value}
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
                @my-page-changed=${n=>this.handleOnChangePagination("pageNumber",n.detail.current)}
                @row-per-page=${n=>this.handleOnChangePagination("pageSize",n.detail)}
              ></colibri-common-g2-pagination>
            </div>

            <colibri-common-g2-table-default
              .load=${this.isLoadTable}
              isSort
              .sortBy=${this.sortBy}
              .theadData=${this.tHeadFormatted()}
              .tbodyData=${this.formattedData}
              type="alternate"
              @my-sortBy=${n=>this.handleSortTable(n)}
            ></colibri-common-g2-table-default>

            <div class="pagination">
              <colibri-common-g2-pagination
                limit=${(s=this.pagination)==null?void 0:s.pageSize}
                total=${(r=this.pagination)==null?void 0:r.totalPages}
                offset=${this.pagination.pageNumber}
                @my-page-changed=${n=>this.handleOnChangePagination("pageNumber",n.detail.current)}
                @row-per-page=${n=>this.handleOnChangePagination("pageSize",n.detail)}
              ></colibri-common-g2-pagination>
            </div>
          </div>

          <div class="totalBalance">
            <p>Saldo total devido: ${this.totalFeeAmount}</p>

            <div class="buyButton">
              <p>Subtotal: ${z(this.subTotal)}</p>
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
    `}childTable(t){return u`
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
              ${t.InvoiceLink?u`<a
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
    `}calculateTotal(t){return t.selectedFees.reduce((e,i)=>e+i.FeeAmount,0)}formatSelectedRows(){return this.selectedRows.map((e,i)=>({VehicleId:e.VehicleId,SaleTypeDescription:`${e.SaleTypeDescription}: ${this.renderSaleInfo(e)}`,VehicleDescription:e.VehicleDescription,BuyItNowId:e.BuyItNowId,LotOrder:e.LotOrder,AuctionNumber:e.AuctionNumber,TotalFeeAmount:z(this.calculateTotal(e)),View:u`<a
        style="cursor:pointer; color:blue;"
        @click=${()=>this.handleClickCheckout(i)}
        >Visualizar</a
      >`,Child:e.Child,Detail:this.tableSelectedFees(e.selectedFees)}))}modalList(){return u`
      <p>Carrinho (${this.selectedRows.length})</p>

      <colibri-common-g2-table-default
        .theadData=${this.theadDataModal()}
        .tbodyData=${this.formatSelectedRows()}
      >
      </colibri-common-g2-table-default>

      <p class="totalPayment">
        Total a pagar: R$ ${z(this.subTotal)}
      </p>
    `}tableSelectedFees(t){const e=t.map(i=>({FeeAmount:z(i.FeeAmount),FeeName:i.FeeName}));if(window.innerWidth>880)return u`
        <tr>
          <td colspan=${this.theadDataModal().length}>
            <colibri-common-g2-table-default
              .theadData=${[{label:"Descrição cobrança",id:"FeeName"},{label:"Valor",id:"FeeAmount"}]}
              .tbodyData=${e}
            >
            </colibri-common-g2-table-default>
          </td>
        </tr>
      `}toggleCheckbox(t,e,i){const o=parseFloat(t.value);if(t.checked)this.selectedOptions.push(o),this.selectedRows.some(s=>s.VehicleId==e.VehicleId)?this.selectedRows.find(s=>s.VehicleId==e.VehicleId).selectedFees.push(i):this.selectedRows.push({...e,selectedFees:[i]}),this.subTotal+=o;else{this.subTotal-=o;const s=this.selectedRows.find(r=>r.VehicleId===e.VehicleId);s&&(s.selectedFees=s.selectedFees.filter(r=>r!==i),s.selectedFees.length===0&&(this.selectedRows=this.selectedRows.filter(r=>r.VehicleId!==e.VehicleId)))}this.subTotal=parseFloat(this.subTotal.toFixed(2)),this.requestUpdate()}};w.styles=[en],$([Le("#pix")],w.prototype,"pix",2),$([m()],w.prototype,"showModal",2),$([m()],w.prototype,"showModalFilters",2),$([m()],w.prototype,"completionPayment",2),$([m()],w.prototype,"isLoadTable",2),$([m()],w.prototype,"rowModalData",2),$([m()],w.prototype,"dataListNotFormatted",2),$([m()],w.prototype,"dataList",2),$([m()],w.prototype,"showHead",2),$([m()],w.prototype,"IsPaid",2),$([m()],w.prototype,"showHeadMap",2),$([m()],w.prototype,"requestId",2),$([m()],w.prototype,"FeeIds",2),$([m()],w.prototype,"visibleRows",2),$([m()],w.prototype,"subTotal",2),$([m()],w.prototype,"selectedOptions",2),$([m()],w.prototype,"dataQrCode",2),$([b()],w.prototype,"memberId",2),$([m()],w.prototype,"pagination",2),$([m()],w.prototype,"vehicleId",2),$([m()],w.prototype,"GetMemberVehicleDocumentosOptionsSaleType",2),$([m()],w.prototype,"saleType",2),$([b({type:String})],w.prototype,"sortBy",2),$([m()],w.prototype,"sortAsc",2),$([b({type:String})],w.prototype,"token",2),$([b()],w.prototype,"servicesUrl",2),w=$([M("payment-pending")],w);const sn=N`
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
`;var nn=Object.defineProperty,rn=Object.getOwnPropertyDescriptor,an=(t,e,i,o)=>{for(var s=o>1?void 0:o?rn(e,i):e,r=t.length-1,n;r>=0;r--)(n=t[r])&&(s=(o?n(e,i,s):n(s))||s);return o&&s&&nn(e,i,s),s};let Di=class extends R{static get styles(){return[sn]}render(){return u`
      <div class="toast" id="toast">
        <div>
          <strong>Copiado para area de transferência</strong>
        </div>
      </div>
    `}handleOnModalCard(){const t=new CustomEvent("my-close-modal");this.dispatchEvent(t)}};Di=an([M("toast-copy-paste")],Di);const ln=N`
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
`;var dn=Object.defineProperty,cn=Object.getOwnPropertyDescriptor,T=(t,e,i,o)=>{for(var s=o>1?void 0:o?cn(e,i):e,r=t.length-1,n;r>=0;r--)(n=t[r])&&(s=(o?n(e,i,s):n(s))||s);return o&&s&&dn(e,i,s),s};let D=class extends R{constructor(){super(...arguments),this.showModal=!1,this.isLoadTable=!1,this.titleModal="",this.showHead=!1,this.showHeadMap=new Map,this.vehicleId=0,this.statusId=0,this.PaymentsHistoryOption=[],this.memberId=1024863,this.pagination={memberId:this.memberId,baseQuery:"",pageSize:20,pageNumber:1,sortField:"",sortOrder:"",totalPages:0,NumFound:0},this.token="",this.servicesUrl="",this.selectedRows=[],this.theadData=[{label:"Identificação",id:"ServiceNumber"},{label:"Data de emissão",id:"CreationDateStr"},{label:"Status",id:"PaymentStatus"},{label:"Data de vencimento",id:"DueDateStr"},{label:"Data do pagamento",id:"PaymentDateStr"},{label:"Valor",id:"SaleValue"},{label:"",id:"view"}],this.subTotal=0,this.selectedOptions=[]}formatDataList(t){const e=o=>{let s;switch(o){case 1:s="warning";break;case 2:s="gray";break;case 3:s="error";break;case 4:s="yellow";break;default:s="gray"}return s};return t.items.map(o=>({...o,CreationDateStr:this.formatDate(o.CreationDate),PaymentDateStr:this.formatDate(o.PaymentDate),DueDateStr:this.formatDate(o.DueDate),SaleValue:this.formatMoney(o.SaleValue),PaymentStatus:u` <colibri-common-g2-badge
        type=${e(o.PaymentStatusID)}
        size="sm"
        text=${o.PaymentStatus}
      ></colibri-common-g2-badge>`,view:u`<a
        style="color: #1254ff; cursor: pointer;"
        @click=${()=>{this.dataQrCode={creationDate:o.CreationDate,dueDate:o.DueDate,copyPaste:o.CopyPaste,qrcode:o.QRCode,requestId:o.RequestId,requestAmount:o.RequestAmount,PaymentStatusID:o.PaymentStatusID,Items:o.Items},this.handleOpenModal()}}
        >Visualizar</a
      >`}))}fetchData(){this.showModalFilters&&(this.showModalFilters=!1),this.isLoadTable=!0,L(`${this.servicesUrl}/G2OnlineServices/GetPaymentHistory`,this.token,{memberId:this.memberId,pageSize:this.pagination.pageSize,pageNumber:this.pagination.pageNumber,vehicleId:this.vehicleId==0?0:this.vehicleId,statusId:this.statusId},t=>{this.isLoadTable=!1,this.dataListNotFormatted=t.items,this.dataList=this.formatDataList(t),this.pagination=this.pagination={...this.pagination,NumFound:t.pagination.NumFound,pageSize:t.pagination.pageSize,pageNumber:t.pagination.pageNumber,totalPages:t.pagination.totalPages},this.requestUpdate()},()=>{})}GetPaymentsHistoryFilters(){ye(`${this.servicesUrl}/G2OnlineServices/GetPaymentsHistoryFilters`,this.token,t=>{this.PaymentsHistoryOption=t.Filters.map(e=>({id:String(e.id),value:String(e.id),name:e.descricao})),this.PaymentsHistoryOption.unshift({id:"0",value:"0",name:"Selecione uma opção"}),this.requestUpdate()},()=>{})}handleOpenModal(){this.titleModalChange(),this.showModal=!this.showModal,this.showModal==!1&&(this.pix.clearTime(),this.fetchData()),this.requestUpdate()}formatDate(t){if(t==null)return"";const e=new Date(t),i=String(e.getDate()).padStart(2,"0"),o=String(e.getMonth()+1).padStart(2,"0"),s=e.getFullYear();return`${i}/${o}/${s}`}formatMoney(t){return new Intl.NumberFormat("pt-BR",{style:"currency",currency:"BRL"}).format(t)}handleOpenModalFilters(){this.showModalFilters=!this.showModalFilters}filterModalResponsive(){return u`
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
    `}async connectedCallback(){super.connectedCallback(),await super.updateComplete,this.fetchData(),this.GetPaymentsHistoryFilters()}PrintPaymentRequestsToPdf(){L(`${this.servicesUrl}/G2OnlineServices/PrintPaymentRequestsToPdf`,this.token,{items:this.dataListNotFormatted},t=>{if(t.resultCode===0&&t.content){const e=atob(t.content),i=new Array(e.length);for(let h=0;h<e.length;h++)i[h]=e.charCodeAt(h);const o=new Uint8Array(i),s=new Blob([o],{type:"application/pdf"}),r=URL.createObjectURL(s),n=new Date,a=String(n.getDate()).padStart(2,"0"),p=String(n.getMonth()+1).padStart(2,"0"),c=n.getFullYear(),l=document.createElement("a");l.style.display="none",l.href=r,l.download=`meusPagamentos${a}/${p}/${c}.pdf`,document.body.appendChild(l),l.click(),URL.revokeObjectURL(r),document.body.removeChild(l)}},()=>{})}ExportPaymentRequestsToExcel(){L(`${this.servicesUrl}/G2OnlineServices/ExportPaymentRequestsToExcel`,this.token,{items:this.dataListNotFormatted},t=>{if(t.resultCode===0&&t.content){const e=atob(t.content),i=new Array(e.length);for(let h=0;h<e.length;h++)i[h]=e.charCodeAt(h);const o=new Uint8Array(i),s=new Blob([o],{type:"application/vnd.ms-excel"}),r=URL.createObjectURL(s),n=new Date,a=String(n.getDate()).padStart(2,"0"),p=String(n.getMonth()+1).padStart(2,"0"),c=n.getFullYear(),l=document.createElement("a");l.style.display="none",l.href=r,l.download=`meusPagamentos${a}/${p}/${c}.xls`,document.body.appendChild(l),l.click(),URL.revokeObjectURL(r),document.body.removeChild(l)}},()=>{})}handleOnParams(t){this.pagination.pageNumber=t,this.fetchData()}handlePaginationSize(t){this.pagination.pageSize=t,this.fetchData()}titleModalChange(){this.dataQrCode.PaymentStatusID==2?this.titleModal="Pagamento Realizado":this.dataQrCode.PaymentStatusID==3?this.titleModal="Pagamento Cancelado":this.dataQrCode.PaymentStatusID==4?this.titleModal="Pagamento Expirado":(this.titleModal="Aguardando Pagamento",this.messageModal&&(this.titleModal="Aviso"))}updated(t){super.updated(t),t.has("messageModal")&&this.titleModalChange()}render(){var t,e,i,o,s,r,n;return u`
      <div id="copiedMessage" class="copied-message">
        Texto copiado com sucesso!
      </div>

      <g2-dialog
        .isOpen=${this.showModal}
        title=${this.titleModal}
        @on-close=${this.handleOpenModal}
      >
        ${this.showModal?u`<qrcode-visualizer
              id="pix"
              .dataQrCode=${this.dataQrCode}
              .token=${this.token}
              .servicesUrl=${this.servicesUrl}
              .requestId=${(t=this.dataQrCode)==null?void 0:t.requestId}
              .cancelRequest=${!0}
              .memberId=${this.memberId}
              @my-close-modal=${this.handleOpenModal}
              @message-callback=${a=>this.messageModal=a.detail}
            ></qrcode-visualizer>`:null}
      </g2-dialog>

      ${this.filterModalResponsive()}

      <div class="content">
        <div class="header">
          <h2 class="title">Meus Pagamentos</h2>

          <div class="header-actions">
            <button
              class="button-print"
              @click=${this.ExportPaymentRequestsToExcel}
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
              @click=${this.PrintPaymentRequestsToPdf}
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
                @on-input=${a=>this.vehicleId=a.detail.value}
              ></colibri-common-g2-input>

              <colibri-common-g2-select
                class="input"
                isLabel="Status"
                .isChildren=${this.PaymentsHistoryOption}
                @on-input=${a=>this.statusId=a.detail.value}
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
                  @my-page-changed=${a=>this.handleOnParams(a.detail.current)}
                  @row-per-page=${a=>this.handlePaginationSize(a.detail)}
                ></colibri-common-g2-pagination>
              </div>

              ${this.isLoadTable?u`
                    <colibri-common-g2-load-table></colibri-common-g2-load-table>
                  `:u`<colibri-common-g2-table-default
                    .theadData=${this.theadData}
                    .tbodyData=${this.dataList}
                    type="alternate"
                  ></colibri-common-g2-table-default>`}

              <div class="pagination">
                <colibri-common-g2-pagination
                  limit=${(s=this.pagination)==null?void 0:s.pageSize}
                  total=${(r=this.pagination)==null?void 0:r.totalPages}
                  offset=${(n=this.pagination)==null?void 0:n.pageNumber}
                  @my-page-changed=${a=>this.handleOnParams(a.detail.current)}
                  @row-per-page=${a=>this.handlePaginationSize(a.detail)}
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
    `}calculatesubTotal(){let t=0;this.selectedRows.forEach(e=>{e.selectedFees.forEach(i=>{const o=e.Fees.find(s=>s.FeeType===i);o&&(t+=parseInt(o.FeeAmount))})}),this.subTotal=t,this.requestUpdate()}copyPaste(t){navigator.clipboard.writeText(t);const e=this.shadowRoot.getElementById("copiedMessage");e.style.display="block",setTimeout(()=>{e.style.display="none"},3e3)}};D.styles=[ln],T([Le("#pix")],D.prototype,"pix",2),T([m()],D.prototype,"showModal",2),T([m()],D.prototype,"isLoadTable",2),T([m()],D.prototype,"titleModal",2),T([m()],D.prototype,"showModalFilters",2),T([m()],D.prototype,"dataListNotFormatted",2),T([m()],D.prototype,"dataList",2),T([m()],D.prototype,"showHead",2),T([m()],D.prototype,"showHeadMap",2),T([m()],D.prototype,"vehicleId",2),T([m()],D.prototype,"statusId",2),T([m()],D.prototype,"PaymentsHistoryOption",2),T([m()],D.prototype,"messageModal",2),T([b()],D.prototype,"memberId",2),T([m()],D.prototype,"pagination",2),T([b({type:String})],D.prototype,"token",2),T([b()],D.prototype,"servicesUrl",2),T([m()],D.prototype,"dataQrCode",2),T([m()],D.prototype,"subTotal",2),T([m()],D.prototype,"selectedOptions",2),D=T([M("request-payment")],D);const pn=N`
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
`;var hn=Object.defineProperty,un=Object.getOwnPropertyDescriptor,k=(t,e,i,o)=>{for(var s=o>1?void 0:o?un(e,i):e,r=t.length-1,n;r>=0;r--)(n=t[r])&&(s=(o?n(e,i,s):n(s))||s);return o&&s&&hn(e,i,s),s};let S=class extends R{constructor(){super(...arguments),this.showModal=!1,this.completionPayment=!1,this.isLoadTable=!1,this.showHead=!1,this.showHeadMap=new Map,this.memberId=1024863,this.pagination={memberId:this.memberId,baseQuery:"",pageSize:20,pageNumber:1,sortField:"",sortOrder:"",totalPages:0,numFound:0},this.selectedRows=[],this.titleModal="Aguardando Pagamento",this.vehicleId=0,this.saleStatus=0,this.saleType=0,this.token="",this.servicesUrl="",this.theadData=[{id:"-",label:"-",hoverMensage:"-"},{label:"Código",id:"VehicleId"},{label:"Tipo de Venda",id:"Info"},{label:"Ano",id:"ModelYear"},{label:"Marca",id:"Make"},{label:"Modelo",id:"Model"},{label:"Data da Venda",id:"SaleDate"},{label:"Doc Previsto",id:"DocPrevisto",hoverMensage:"mensagem do hover"},{label:"Status",id:"Status"},{label:"Local Retirada",id:"PickupLocation"},{label:"Código de Rastreio",id:"TrackingCode"}]}formatDataList(t){const e=o=>{let s;switch(o){case 1:s="warning";break;case 2:s="lime";break;case 3:s="blue";break;case 4:s="yellow";break;case 5:s="violet";break;case 6:s="gold";break;case 7:s="success";break;case 8:s="gray";break;default:s="gray"}return s};return t.items.map(o=>({...o,SaleDate:this.formatDate(o.SaleDate),DocPrevisto:u`
      <div title="Essa é a previsão de disponibilidade do documento na Copart">
        ${this.formatDate(o.DocPrevisto)}
      </div>`,SaleValue:this.formatMoney(o.SaleValue),"-":this.checkBoxTable(o),Info:`${o.SaleType}: ${o.SaleInfo}`,TrackingCode:u`<tracking-code-table
        .TrackingCode=${o.TrackingCode}
      ></tracking-code-table>`,Status:o.IsBlocked?u`<colibri-common-g2-badge
            type=${"error"}
            size="sm"
            text=${"Bloqueado"}
          ></colibri-common-g2-badge>`:u`<colibri-common-g2-badge
            type=${e(o.StatusId)}
            size="sm"
            text=${o.Status}
          ></colibri-common-g2-badge>`}))}fetchData(){this.showModalFilters&&(this.showModalFilters=!1),this.isLoadTable=!0,L(`${this.servicesUrl}/G2OnlineServices/GetMemberVehicleDocuments`,this.token,{memberId:this.memberId,pageSize:this.pagination.pageSize,pageNumber:this.pagination.pageNumber,vehicleId:this.vehicleId==0?0:this.vehicleId,statusId:this.saleStatus,saleType:this.saleType},t=>{this.isLoadTable=!1,this.dataListNotFormatted=t.items,this.dataList=this.formatDataList(t),this.pagination=this.pagination={...this.pagination,numFound:t.pagination.numFound,pageSize:t.pagination.pageSize,pageNumber:t.pagination.pageNumber,totalPages:t.pagination.totalPages},this.requestUpdate()},()=>{})}GetMemberVehicleDocumentosFilters(){ye(`${this.servicesUrl}/G2OnlineServices/GetMemberVehicleDocumentosFilters`,this.token,t=>{this.GetMemberVehicleDocumentosOptionsStatus=t.Status.map(e=>({id:String(e.id),value:String(e.id),name:e.descricao})),this.GetMemberVehicleDocumentosOptionsStatus.unshift({id:"0",value:"0",name:"Selecione uma opção"}),this.GetMemberVehicleDocumentosOptionsSaleType=t.SaleType.map(e=>({id:String(e.id),value:String(e.id),name:e.descricao})),this.GetMemberVehicleDocumentosOptionsSaleType.unshift({id:"0",value:"0",name:"Selecione uma opção"}),this.requestUpdate()},()=>{})}PrintVehicleDocumentsToPdf(){L(`${this.servicesUrl}/G2OnlineServices/PrintVehicleDocumentsToPdf`,this.token,{items:this.dataListNotFormatted},t=>{if(t.resultCode===0&&t.content){const e=atob(t.content),i=new Array(e.length);for(let h=0;h<e.length;h++)i[h]=e.charCodeAt(h);const o=new Uint8Array(i),s=new Blob([o],{type:"application/pdf"}),r=URL.createObjectURL(s),n=new Date,a=String(n.getDate()).padStart(2,"0"),p=String(n.getMonth()+1).padStart(2,"0"),c=n.getFullYear(),l=document.createElement("a");l.style.display="none",l.href=r,l.download=`documentosDosVeículos${a}/${p}/${c}.pdf`,document.body.appendChild(l),l.click(),URL.revokeObjectURL(r),document.body.removeChild(l)}},()=>{})}ExportVehicleDocumentsToExcel(){L(`${this.servicesUrl}/G2OnlineServices/ExportVehicleDocumentsToExcel`,this.token,{items:this.dataListNotFormatted},t=>{if(t.resultCode===0&&t.content){const e=atob(t.content),i=new Array(e.length);for(let h=0;h<e.length;h++)i[h]=e.charCodeAt(h);const o=new Uint8Array(i),s=new Blob([o],{type:"application/vnd.ms-excel"}),r=URL.createObjectURL(s),n=new Date,a=String(n.getDate()).padStart(2,"0"),p=String(n.getMonth()+1).padStart(2,"0"),c=n.getFullYear(),l=document.createElement("a");l.style.display="none",l.href=r,l.download=`documentosDosVeículos${a}/${p}/${c}.xls`,document.body.appendChild(l),l.click(),URL.revokeObjectURL(r),document.body.removeChild(l)}},()=>{})}toggleCheckbox(t,e){t.target.checked?this.selectedRows=[...this.selectedRows,e]:this.selectedRows=this.selectedRows.filter(o=>o.VehicleId!==e.VehicleId)}async connectedCallback(){super.connectedCallback(),await super.updateComplete,this.fetchData(),this.GetMemberVehicleDocumentosFilters(),this.addEventListener("selection-removed",t=>{const{vehicleId:e}=t.detail;this.selectedRows=this.selectedRows.filter(i=>i.VehicleId!==e)})}async handleOnChangePagination(t,e){t==="pageSize"&&(this.pagination={...this.pagination,pageNumber:1}),this.pagination={...this.pagination,[t]:e},this.fetchData()}handleShowModal(){this.showModal=!this.showModal,this.showModal!=!0&&(this.fetchData(),this.selectedRows=[],this.documentsSend.clearInterval())}handleOpenModalFilters(){this.showModalFilters=!this.showModalFilters}filterModalResponsive(){return u`
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
    `}render(){var t,e,i,o;return u`
      <g2-dialog
        .isOpen=${this.showModal}
        title=${this.messageCallback?"Aviso":this.titleModal}
        @on-close=${this.handleShowModal}
      >
        ${this.showModal?u`<documents-send
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
    `}formatDate(t){if(t===null||t===0)return"";const e=new Date(t),i=String(e.getDate()).padStart(2,"0"),o=String(e.getMonth()+1).padStart(2,"0"),s=e.getFullYear();return`${i}/${o}/${s}`}formatMoney(t){return new Intl.NumberFormat("pt-BR",{style:"currency",currency:"BRL"}).format(t)}checkBoxTable(t){return u`<input
      ?disabled=${!t.IsSelectable}
      @input=${e=>{this.toggleCheckbox(e,t)}}
      type="checkbox"
    />`}};S.styles=[pn],k([Le("#documentsSend")],S.prototype,"documentsSend",2),k([m()],S.prototype,"showModal",2),k([m()],S.prototype,"completionPayment",2),k([m()],S.prototype,"isLoadTable",2),k([m()],S.prototype,"dataList",2),k([m()],S.prototype,"dataListNotFormatted",2),k([m()],S.prototype,"isActiveClipBoard",2),k([m()],S.prototype,"showHead",2),k([m()],S.prototype,"showModalFilters",2),k([m()],S.prototype,"showHeadMap",2),k([b()],S.prototype,"memberId",2),k([m()],S.prototype,"pagination",2),k([m()],S.prototype,"dataQrCode",2),k([m()],S.prototype,"selectedRows",2),k([m()],S.prototype,"GetMemberVehicleDocumentosOptionsStatus",2),k([m()],S.prototype,"GetMemberVehicleDocumentosOptionsSaleType",2),k([m()],S.prototype,"titleModal",2),k([m()],S.prototype,"messageCallback",2),k([m()],S.prototype,"vehicleId",2),k([m()],S.prototype,"saleStatus",2),k([m()],S.prototype,"saleType",2),k([b({type:String})],S.prototype,"token",2),k([b()],S.prototype,"servicesUrl",2),S=k([M("vehicle-document")],S);const Ai=N`
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
`;var mn=Object.defineProperty,fn=Object.getOwnPropertyDescriptor,Y=(t,e,i,o)=>{for(var s=o>1?void 0:o?fn(e,i):e,r=t.length-1,n;r>=0;r--)(n=t[r])&&(s=(o?n(e,i,s):n(s))||s);return o&&s&&mn(e,i,s),s};let W=class extends R{constructor(){super(...arguments),this.isDisabledInput=!0,this.loadSkeletonInput=!1,this.zipCodeDetails={streetName:"",neighborhood:"",cityId:"",state:""},this.servicesUrl="",this.memberId=0,this.token="",this.data={AddressName:"",AddressNumber:"",ZipCode:"",Neighborhood:"",City:"",State:"",Complement:"",CityId:""},this.errors={AddressNumber:"",ZipCode:""}}static get styles(){return[Ai]}async connectedCallback(){super.connectedCallback(),await super.updateComplete}onChange(t){const e=t.detail,{name:i,value:o}=e;this.dispatchEvent(new CustomEvent("on-Change",{detail:{name:i,value:o}}))}saveNewAddress(){this.dispatchEvent(new CustomEvent("save-new-address")),this.isDisabledInput=!0}fetchAZipCode(){this.loadSkeletonInput=!0,L(`${this.servicesUrl}/G2Member/SearchZipCode`,this.token,{zipCode:this.data.ZipCode},t=>{this.data={...this.data,AddressName:t.zipCodeDetails.streetName,Neighborhood:t.zipCodeDetails.neighborhood,City:t.zipCodeDetails.cityDescription,CityId:t.zipCodeDetails.cityId,State:t.zipCodeDetails.state},this.loadSkeletonInput=!1,this.dispatchEvent(new CustomEvent("zipcode-searched-sucessfully",{detail:this.data})),this.requestUpdate()},()=>{})}render(){var t,e,i,o,s,r,n,a,p;return u`
      <div class="container">
        <colibri-common-g2-input
          isLabel="Cep"
          name="ZipCode"
          .value=${(t=this.data)==null?void 0:t.ZipCode}
          @on-input=${c=>this.onChange(c)}
          @blur=${()=>this.fetchAZipCode()}
          .error=${(e=this.errors)==null?void 0:e.ZipCode}
          .isDisabled=${this.isDisabledInput}
          type="text"
        >
        </colibri-common-g2-input>

        ${this.loadSkeletonInput?u`<ui-load-input
              isLabel="Logradouro"
              style="align-self:start"
            ></ui-load-input>`:u`<colibri-common-g2-input
              isLabel="Logradouro"
              name="name"
              value=${(i=this.data)==null?void 0:i.AddressName}
              @on-input=${c=>this.onChange(c)}
              isDisabled
              type="text"
            >
            </colibri-common-g2-input>`}

        <colibri-common-g2-input
          isLabel="Número"
          name="AddressNumber"
          value=${(o=this.data)==null?void 0:o.AddressNumber}
          @on-input=${c=>this.onChange(c)}
          .isDisabled=${this.isDisabledInput}
          .error=${(s=this.errors)==null?void 0:s.AddressNumber}
          type="text"
        >
        </colibri-common-g2-input>

        <colibri-common-g2-input
          isLabel="Complemento"
          name="Complement"
          value=${(r=this.data)==null?void 0:r.Complement}
          @on-input=${c=>this.onChange(c)}
          .isDisabled=${this.isDisabledInput}
          type="text"
        >
        </colibri-common-g2-input>

        ${this.loadSkeletonInput?u`<ui-load-input
              isLabel="Logradouro"
              style="align-self:start"
            ></ui-load-input>`:u`<colibri-common-g2-input
              isLabel="Bairro"
              name="name"
              value=${(n=this.data)==null?void 0:n.Neighborhood}
              isDisabled
              type="text"
            >
            </colibri-common-g2-input>`}
        ${this.loadSkeletonInput?u`<ui-load-input
              isLabel="Cidade"
              style="align-self:start"
            ></ui-load-input>`:u`<colibri-common-g2-input
              isLabel="Cidade"
              name="name"
              value=${(a=this.data)==null?void 0:a.City}
              isDisabled
              type="text"
            >
            </colibri-common-g2-input>`}
        ${this.loadSkeletonInput?u`<ui-load-input isLabel="Estado" class="span"></ui-load-input>`:u`<colibri-common-g2-input
              class="span"
              isLabel="Estado"
              name="State"
              value=${(p=this.data)==null?void 0:p.State}
              isDisabled
              type="text"
            >
            </colibri-common-g2-input>`}

        <div class="contentButtons secondColumn">
          ${this.isDisabledInput?null:u`<colibri-common-g2-button
                @onClick=${this.saveNewAddress}
                variant="default"
              >
                Salvar
              </colibri-common-g2-button>`}
        </div>
      </div>
    `}};Y([b()],W.prototype,"isDisabledInput",2),Y([m()],W.prototype,"loadSkeletonInput",2),Y([m()],W.prototype,"zipCodeDetails",2),Y([b()],W.prototype,"servicesUrl",2),Y([b()],W.prototype,"memberId",2),Y([b({type:String})],W.prototype,"token",2),Y([b()],W.prototype,"data",2),Y([b()],W.prototype,"errors",2),W=Y([M("actual-form")],W);var gn=Object.defineProperty,bn=Object.getOwnPropertyDescriptor,J=(t,e,i,o)=>{for(var s=o>1?void 0:o?bn(e,i):e,r=t.length-1,n;r>=0;r--)(n=t[r])&&(s=(o?n(e,i,s):n(s))||s);return o&&s&&gn(e,i,s),s};let Z=class extends R{constructor(){super(...arguments),this.zipCodeDetails={streetName:"",neighborhood:"",cityDescription:"",state:""},this.loadSkeletonInput=!1,this.servicesUrl="",this.memberId=0,this.token="",this.errors={AddressNumber:"",ZipCode:""},this.data={AddressName:"",AddressNumber:"",ZipCode:"",Neighborhood:"",City:"",State:"",Complement:"",CityId:""}}static get styles(){return[Ai]}async connectedCallback(){super.connectedCallback(),await super.updateComplete}fetchAZipCode(){this.loadSkeletonInput=!0,L(`${this.servicesUrl}/G2Member/SearchZipCode`,this.token,{zipCode:this.data.ZipCode},t=>{this.data={...this.data,AddressName:t.zipCodeDetails.streetName,Neighborhood:t.zipCodeDetails.neighborhood,City:t.zipCodeDetails.cityDescription,CityId:t.zipCodeDetails.cityId,State:t.zipCodeDetails.state},this.loadSkeletonInput=!1,this.dispatchEvent(new CustomEvent("zipcode-searched-sucessfully",{detail:this.data})),this.requestUpdate()},()=>{})}onChange(t){const e=t.detail,{name:i,value:o}=e;if(i=="ZipCode")if(isNaN(parseInt(o))){this.errors.ZipCode="Digíte apenas números!";return}else this.errors.ZipCode="";this.dispatchEvent(new CustomEvent("on-Change",{detail:{name:i,value:o}}))}render(){var t,e,i,o;return u`
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

        ${this.loadSkeletonInput?u`<ui-load-input
              isLabel="Logradouro"
              style="align-self:start"
            ></ui-load-input>`:u`<colibri-common-g2-input
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

        ${this.loadSkeletonInput?u`<ui-load-input isLabel="Bairro"></ui-load-input>`:u`<colibri-common-g2-input
              isLabel="Bairro"
              name="Neighborhood"
              @on-input=${s=>this.onChange(s)}
              .value=${(e=this.data)==null?void 0:e.Neighborhood}
              isDisabled
              type="text"
            >
            </colibri-common-g2-input>`}
        ${this.loadSkeletonInput?u`<ui-load-input
              isLabel="Cidade"
              style="align-self:end"
            ></ui-load-input>`:u`<colibri-common-g2-input
              isLabel="Cidade"
              name="City"
              @on-input=${s=>this.onChange(s)}
              .value=${(i=this.data)==null?void 0:i.City}
              isDisabled
              type="text"
            >
            </colibri-common-g2-input>`}
        ${this.loadSkeletonInput?u`<ui-load-input isLabel="Estado" class="span"></ui-load-input>`:u`<colibri-common-g2-input
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
    `}};J([m()],Z.prototype,"zipCodeDetails",2),J([m()],Z.prototype,"loadSkeletonInput",2),J([b()],Z.prototype,"servicesUrl",2),J([b()],Z.prototype,"memberId",2),J([b({type:String})],Z.prototype,"token",2),J([b()],Z.prototype,"errors",2),J([b()],Z.prototype,"data",2),J([m()],Z.prototype,"cep",2),Z=J([M("third-form")],Z)});
