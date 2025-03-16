<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <!-- Page Wrapper -->

  <div class="page-wrapper">
    <div class="content container-fluid">
      <!-- Page Header -->
      <element-breadcrumb :title="title" />
      <!-- /Page Header -->

      <div class="row">
        <!-- Timeline -->
        <div class="col-md-12">
          <div class="card">
            <div class="card-body">
              <div class="cd-horizontal-timeline">
                <div class="timeline">
                  <div class="events-wrapper">
                    <div class="events">
                      <ol>
                        <li>
                          <a href="#0" data-date="16/01/2014" class="selected">16 Jan</a>
                        </li>
                        <li><a href="#0" data-date="28/02/2014">28 Feb</a></li>
                        <li><a href="#0" data-date="20/04/2014">20 Mar</a></li>
                        <li><a href="#0" data-date="20/05/2014">20 May</a></li>
                        <li><a href="#0" data-date="09/07/2014">09 Jul</a></li>
                        <li><a href="#0" data-date="30/08/2014">30 Aug</a></li>
                        <li><a href="#0" data-date="15/09/2014">15 Sep</a></li>
                        <li><a href="#0" data-date="01/11/2014">01 Nov</a></li>
                        <li><a href="#0" data-date="10/12/2014">10 Dec</a></li>
                        <li><a href="#0" data-date="19/01/2015">29 Jan</a></li>
                        <li><a href="#0" data-date="03/03/2015">3 Mar</a></li>
                      </ol>
                      <span class="filling-line" aria-hidden="true"></span>
                    </div>
                    <!-- events -->
                  </div>
                  <ul class="cd-timeline-navigation">
                    <li><a href="#0" class="prev inactive">Prev</a></li>
                    <li><a href="#0" class="next">Next</a></li>
                  </ul>
                  <!-- cd-timeline-navigation -->
                </div>
                <!-- timeline -->
                <div class="events-content">
                  <ol>
                    <li class="selected" data-date="16/01/2014">
                      <h3><small>Title 01</small></h3>
                      <p class="m-t-40">
                        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Illum
                        praesentium officia, fugit recusandae ipsa, quia velit nulla
                        adipisci? Consequuntur aspernatur at, eaque hic repellendus sit
                        dicta consequatur quae, ut harum ipsam molestias maxime non nisi
                        reiciendis eligendi! Doloremque quia pariatur harum ea amet
                        quibusdam quisquam, quae, temporibus dolores porro doloribus.
                      </p>
                    </li>
                    <li data-date="28/02/2014">
                      <h3><small>Title 02</small></h3>
                      <p class="m-t-40">
                        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Illum
                        praesentium officia, fugit recusandae ipsa, quia velit nulla
                        adipisci? Consequuntur aspernatur at, eaque hic repellendus sit
                        dicta consequatur quae, ut harum ipsam molestias maxime non nisi
                        reiciendis eligendi! Doloremque quia pariatur harum ea amet
                        quibusdam quisquam, quae, temporibus dolores porro doloribus.
                      </p>
                    </li>
                    <li data-date="20/04/2014">
                      <h3><small>Title 03</small></h3>
                      <p class="m-t-40">
                        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Illum
                        praesentium officia, fugit recusandae ipsa, quia velit nulla
                        adipisci? Consequuntur aspernatur at, eaque hic repellendus sit
                        dicta consequatur quae, ut harum ipsam molestias maxime non nisi
                        reiciendis eligendi! Doloremque quia pariatur harum ea amet
                        quibusdam quisquam, quae, temporibus dolores porro doloribus.
                      </p>
                    </li>
                    <li data-date="20/05/2014">
                      <h3><small>Title 04</small></h3>
                      <p class="m-t-40">
                        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Illum
                        praesentium officia, fugit recusandae ipsa, quia velit nulla
                        adipisci? Consequuntur aspernatur at, eaque hic repellendus sit
                        dicta consequatur quae, ut harum ipsam molestias maxime non nisi
                        reiciendis eligendi! Doloremque quia pariatur harum ea amet
                        quibusdam quisquam, quae, temporibus dolores porro doloribus.
                      </p>
                    </li>
                    <li data-date="09/07/2014">
                      <h3><small>Title 05</small></h3>
                      <p class="m-t-40">
                        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Illum
                        praesentium officia, fugit recusandae ipsa, quia velit nulla
                        adipisci? Consequuntur aspernatur at, eaque hic repellendus sit
                        dicta consequatur quae, ut harum ipsam molestias maxime non nisi
                        reiciendis eligendi! Doloremque quia pariatur harum ea amet
                        quibusdam quisquam, quae, temporibus dolores porro doloribus.
                      </p>
                    </li>
                    <li data-date="30/08/2014">
                      <h3><small>Title 06</small></h3>
                      <p class="m-t-40">
                        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Illum
                        praesentium officia, fugit recusandae ipsa, quia velit nulla
                        adipisci? Consequuntur aspernatur at, eaque hic repellendus sit
                        dicta consequatur quae, ut harum ipsam molestias maxime non nisi
                        reiciendis eligendi! Doloremque quia pariatur harum ea amet
                        quibusdam quisquam, quae, temporibus dolores porro doloribus.
                      </p>
                    </li>
                    <li data-date="15/09/2014">
                      <h3><small>Title 07</small></h3>
                      <p class="m-t-40">
                        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Illum
                        praesentium officia, fugit recusandae ipsa, quia velit nulla
                        adipisci? Consequuntur aspernatur at, eaque hic repellendus sit
                        dicta consequatur quae, ut harum ipsam molestias maxime non nisi
                        reiciendis eligendi! Doloremque quia pariatur harum ea amet
                        quibusdam quisquam, quae, temporibus dolores porro doloribus.
                      </p>
                    </li>
                    <li data-date="01/11/2014">
                      <h3><small>Event List</small></h3>
                      <p class="m-t-40">
                        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Illum
                        praesentium officia, fugit recusandae ipsa, quia velit nulla
                        adipisci? Consequuntur aspernatur at, eaque hic repellendus sit
                        dicta consequatur quae, ut harum ipsam molestias maxime non nisi
                        reiciendis eligendi! Doloremque quia pariatur harum ea amet
                        quibusdam quisquam, quae, temporibus dolores porro doloribus.
                      </p>
                    </li>
                    <li data-date="10/12/2014">
                      <h3><small>Event Item</small></h3>
                      <p class="m-t-40">
                        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Illum
                        praesentium officia, fugit recusandae ipsa, quia velit nulla
                        adipisci? Consequuntur aspernatur at, eaque hic repellendus sit
                        dicta consequatur quae, ut harum ipsam molestias maxime non nisi
                        reiciendis eligendi! Doloremque quia pariatur harum ea amet
                        quibusdam quisquam, quae, temporibus dolores porro doloribus.
                      </p>
                    </li>
                    <li data-date="19/01/2015">
                      <h3><small>Event title</small></h3>
                      <p>
                        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Illum
                        praesentium officia, fugit recusandae ipsa, quia velit nulla
                        adipisci? Consequuntur aspernatur at, eaque hic repellendus sit
                        dicta consequatur quae, ut harum ipsam molestias maxime non nisi
                        reiciendis eligendi! Doloremque quia pariatur harum ea amet
                        quibusdam quisquam, quae, temporibus dolores porro doloribus.
                      </p>
                    </li>
                    <li data-date="03/03/2015">
                      <h3><small>Event title</small></h3>
                      <p>
                        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Illum
                        praesentium officia, fugit recusandae ipsa, quia velit nulla
                        adipisci? Consequuntur aspernatur at, eaque hic repellendus sit
                        dicta consequatur quae, ut harum ipsam molestias maxime non nisi
                        reiciendis eligendi! Doloremque quia pariatur harum ea amet
                        quibusdam quisquam, quae, temporibus dolores porro doloribus.
                      </p>
                    </li>
                  </ol>
                </div>
                <!-- .events-content -->
              </div>
            </div>
          </div>
        </div>
        <!-- /Ribbon -->
      </div>
    </div>
  </div>
  <!-- /Page Wrapper -->
</template>
<script>
export default {
  name: "TimelineComponent",

  data() {
    return {
      title: "Horizontal Timeline",
      sibling: [],
      myArray: [],
    };
  },

  mounted() {
    document.addEventListener("DOMContentLoaded", function () {
      var timelines = document.querySelectorAll(".cd-horizontal-timeline");
      var eventsMinDistance = 60;

      if (timelines.length > 0) {
        initTimelines(timelines);
      }

      function initTimelines(timelines) {
        timelines.forEach(function (timeline) {
          var timelineComponents = {};
          timelineComponents["timelineWrapper"] = timeline.querySelector(
            ".events-wrapper"
          );
          timelineComponents["eventsWrapper"] = timelineComponents[
            "timelineWrapper"
          ].querySelector(".events");
          timelineComponents["fillingLine"] = timelineComponents[
            "eventsWrapper"
          ].querySelector(".filling-line");
          timelineComponents["timelineEvents"] = timelineComponents[
            "eventsWrapper"
          ].querySelectorAll("a");
          timelineComponents["timelineDates"] = parseDate(
            timelineComponents["timelineEvents"]
          );
          timelineComponents["eventsMinLapse"] = minLapse(
            timelineComponents["timelineDates"]
          );
          timelineComponents["timelineNavigation"] = timeline.querySelector(
            ".cd-timeline-navigation"
          );
          timelineComponents["eventsContent"] = timeline.querySelector(".events-content");

          setDatePosition(timelineComponents, eventsMinDistance);
          var timelineTotWidth = setTimelineWidth(timelineComponents, eventsMinDistance);
          timeline.classList.add("loaded");

          timelineComponents["timelineNavigation"].addEventListener(
            "click",
            function (event) {
              if (event.target.classList.contains("next")) {
                updateSlide(timelineComponents, timelineTotWidth, "next");
              } else if (event.target.classList.contains("prev")) {
                updateSlide(timelineComponents, timelineTotWidth, "prev");
              }
            }
          );

          timelineComponents["eventsWrapper"].addEventListener("click", function (event) {
            if (event.target.tagName === "A") {
              event.preventDefault();
              Array.from(timelineComponents["timelineEvents"]).forEach(function (
                eventElement
              ) {
                eventElement.classList.remove("selected");
              });
              event.target.classList.add("selected");

              function updateOlderEvents(event) {
                var selectedDate = event.parentElement;

                if (selectedDate) {
                  Array.from(selectedDate.previousElementSiblings).forEach(function (
                    sibling
                  ) {
                    sibling.querySelector("a").classList.add("older-event");
                  });

                  Array.from(selectedDate.nextElementSiblings).forEach(function (
                    sibling
                  ) {
                    sibling.querySelector("a").classList.remove("older-event");
                  });
                }
              }
              updateFilling(
                event.target,
                timelineComponents["fillingLine"],
                timelineTotWidth
              );
              updateVisibleContent(event.target, timelineComponents["eventsContent"]);
            }
          });

          timelineComponents["eventsContent"].addEventListener("swipeleft", function () {
            var mq = checkMQ();
            if (mq === "mobile") {
              showNewContent(timelineComponents, timelineTotWidth, "next");
            }
          });

          timelineComponents["eventsContent"].addEventListener("swiperight", function () {
            var mq = checkMQ();
            if (mq === "mobile") {
              showNewContent(timelineComponents, timelineTotWidth, "prev");
            }
          });

          document.addEventListener("keyup", function (event) {
            if (event.key === "ArrowLeft" && elementInViewport(timeline)) {
              showNewContent(timelineComponents, timelineTotWidth, "prev");
            } else if (event.key === "ArrowRight" && elementInViewport(timeline)) {
              showNewContent(timelineComponents, timelineTotWidth, "next");
            }
          });
        });
      }

      function updateSlide(timelineComponents, timelineTotWidth, string) {
        var translateValue = getTranslateValue(timelineComponents["eventsWrapper"]);
        var wrapperWidth = parseInt(
          getComputedStyle(timelineComponents["timelineWrapper"]).width
        );
        if (string === "next") {
          translateTimeline(
            timelineComponents,
            translateValue - wrapperWidth + eventsMinDistance,
            wrapperWidth - timelineTotWidth
          );
        } else if (string === "prev") {
          translateTimeline(
            timelineComponents,
            translateValue + wrapperWidth - eventsMinDistance
          );
        }
      }

      function showNewContent(timelineComponents, timelineTotWidth, string) {
        var visibleContent = timelineComponents["eventsContent"].querySelector(
          ".selected"
        );
        var newContent =
          string === "next"
            ? visibleContent.nextElementSibling
            : visibleContent.previousElementSibling;

        if (newContent) {
          var selectedDate = timelineComponents["eventsWrapper"].querySelector(
            ".selected"
          );
          var newEvent =
            string === "next"
              ? selectedDate.parentElement.nextElementSibling.querySelector("a")
              : selectedDate.parentElement.previousElementSibling.querySelector("a");
          updateFilling(newEvent, timelineComponents["fillingLine"], timelineTotWidth);
          updateVisibleContent(newEvent, timelineComponents["eventsContent"]);
          newEvent.classList.add("selected");
          selectedDate.classList.remove("selected");
          updateOlderEvents(newEvent);
          updateTimelinePosition(string, newEvent, timelineComponents);
        }
      }

      function updateTimelinePosition(string, event, timelineComponents) {
        var eventStyle = getComputedStyle(event);
        var eventLeft = parseInt(eventStyle.left);
        var timelineWidth = parseInt(
          getComputedStyle(timelineComponents["timelineWrapper"]).width
        );
        var timelineTotWidth = parseInt(
          getComputedStyle(timelineComponents["eventsWrapper"]).width
        );
        var timelineTranslate = getTranslateValue(timelineComponents["eventsWrapper"]);

        if (
          (string === "next" && eventLeft > timelineWidth - timelineTranslate) ||
          (string === "prev" && eventLeft < -timelineTranslate)
        ) {
          translateTimeline(
            timelineComponents,
            -eventLeft + timelineWidth / 2,
            timelineWidth - timelineTotWidth
          );
        }
      }

      function translateTimeline(timelineComponents, value, totWidth) {
        var eventsWrapper = timelineComponents["eventsWrapper"];
        value = value > 0 ? 0 : value;
        value = typeof totWidth !== "undefined" && value < totWidth ? totWidth : value;
        setTransformValue(eventsWrapper, "translateX", value + "px");

        if (value === 0) {
          timelineComponents["timelineNavigation"]
            .querySelector(".prev")
            .classList.add("inactive");
        } else {
          timelineComponents["timelineNavigation"]
            .querySelector(".prev")
            .classList.remove("inactive");
        }

        if (value === totWidth) {
          timelineComponents["timelineNavigation"]
            .querySelector(".next")
            .classList.add("inactive");
        } else {
          timelineComponents["timelineNavigation"]
            .querySelector(".next")
            .classList.remove("inactive");
        }
      }

      function updateFilling(selectedEvent, filling, totWidth) {
        var eventStyle = getComputedStyle(selectedEvent);
        var eventLeft = parseInt(eventStyle.left);
        var eventWidth = parseInt(eventStyle.width);
        eventLeft = eventLeft + eventWidth / 2;
        var scaleValue = eventLeft / totWidth;
        setTransformValue(filling, "scaleX", scaleValue);
      }

      function setDatePosition(timelineComponents, min) {
        Array.from(timelineComponents["timelineDates"]).forEach(function (date, i) {
          var distance = daydiff(timelineComponents["timelineDates"][0], date);
          var distanceNorm =
            Math.round(distance / timelineComponents["eventsMinLapse"]) + 2;
          timelineComponents["timelineEvents"][i].style.left = distanceNorm * min + "px";
        });
      }

      function setTimelineWidth(timelineComponents, width) {
        var timeSpan = daydiff(
          timelineComponents["timelineDates"][0],
          timelineComponents["timelineDates"][
          timelineComponents["timelineDates"].length - 1
          ]
        );
        var timeSpanNorm = timeSpan / timelineComponents["eventsMinLapse"];
        timeSpanNorm = Math.round(timeSpanNorm) + 4;
        var totalWidth = timeSpanNorm * width;
        timelineComponents["eventsWrapper"].style.width = totalWidth + "px";
        updateFilling(
          timelineComponents["eventsWrapper"].querySelector("a.selected"),
          timelineComponents["fillingLine"],
          totalWidth
        );
        updateTimelinePosition(
          "next",
          timelineComponents["eventsWrapper"].querySelector("a.selected"),
          timelineComponents
        );
        return totalWidth;
      }

      function updateVisibleContent(event, eventsContent) {
        var eventDate = event.getAttribute("data-date");
        var visibleContent = eventsContent.querySelector(".selected");
        var selectedContent = eventsContent.querySelector(
          '[data-date="' + eventDate + '"]'
        );
        var selectedContentHeight = selectedContent.clientHeight;
        var isNext =
          Array.from(selectedContent.parentElement.children).indexOf(selectedContent) >
          Array.from(visibleContent.parentElement.children).indexOf(visibleContent);
        var classEntering = isNext ? "selected enter-right" : "selected enter-left";
        var classLeaving = isNext ? "leave-left" : "leave-right";
        // selectedContent.classList.add(classEntering);
        visibleContent.classList.add(classLeaving);
        visibleContent.addEventListener("animationend", function () {
          visibleContent.classList.remove("leave-right", "leave-left");
          selectedContent.classList.remove("enter-left", "enter-right");
        });
        eventsContent.style.height = selectedContentHeight + "px";
      }

      function updateOlderEvents(event) {
        var selectedDate = event.parentElement;
        Array.from(selectedDate.previousElementSiblings).forEach(function (sibling) {
          sibling.querySelector("a").classList.add("older-event");
        });
        Array.from(selectedDate.nextElementSiblings).forEach(function (sibling) {
          sibling.querySelector("a").classList.remove("older-event");
        });
      }

      function getTranslateValue(timeline) {
        var timelineStyle = getComputedStyle(timeline);
        var timelineTranslate =
          timelineStyle.transform ||
          timelineStyle.webkitTransform ||
          timelineStyle.mozTransform ||
          timelineStyle.msTransform ||
          timelineStyle.oTransform;

        if (timelineTranslate.indexOf("(") >= 0) {
          timelineTranslate = timelineTranslate.split("(")[1];
          timelineTranslate = timelineTranslate.split(")")[0];
          timelineTranslate = timelineTranslate.split(",");
          var translateValue = parseFloat(timelineTranslate[4]);
        } else {
          var translateValue = 0;
        }

        return translateValue;
      }

      function setTransformValue(element, property, value) {
        element.style.transform = property + "(" + value + "px)";
        element.style.webkitTransform = property + "(" + value + "px)";
        element.style.mozTransform = property + "(" + value + "px)";
        element.style.msTransform = property + "(" + value + "px)";
        element.style.oTransform = property + "(" + value + "px)";
      }

      function parseDate(events) {
        var dateArrays = [];
        Array.from(events).forEach(function (singleDate) {
          var dateComp = singleDate.getAttribute("data-date").split("T");
          var dayComp, timeComp;
          if (dateComp.length > 1) {
            dayComp = dateComp[0].split("/");
            timeComp = dateComp[1].split(":");
          } else if (dateComp[0].indexOf(":") >= 0) {
            dayComp = ["2000", "0", "0"];
            timeComp = dateComp[0].split(":");
          } else {
            dayComp = dateComp[0].split("/");
            timeComp = ["0", "0"];
          }
          var newDate = new Date(
            dayComp[2],
            dayComp[1] - 1,
            dayComp[0],
            timeComp[0],
            timeComp[1]
          );
          dateArrays.push(newDate);
        });
        return dateArrays;
      }

      function daydiff(first, second) {
        return Math.round(second - first);
      }

      function minLapse(dates) {
        var dateDistances = [];
        for (var i = 1; i < dates.length; i++) {
          var distance = daydiff(dates[i - 1], dates[i]);
          dateDistances.push(distance);
        }
        return Math.min.apply(null, dateDistances);
      }

      function elementInViewport(el) {
        var rect = el.getBoundingClientRect();
        return (
          rect.top < window.innerHeight &&
          rect.left < window.innerWidth &&
          rect.bottom > 0 &&
          rect.right > 0
        );
      }

      function checkMQ() {
        var content = window.getComputedStyle(
          document.querySelector(".cd-horizontal-timeline"),
          "::before"
        ).content;
        return content.replace(/'/g, "").replace(/"/g, "");
      }
    });
  },
};
</script>
